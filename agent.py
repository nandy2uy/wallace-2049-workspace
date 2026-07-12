import os
from google import genai
from google.genai import types
from google.genai.errors import APIError
import wiki_tools

def run_generation(client, contents, system_instruction, available_tools, models_to_try):
    """Iterates through available models to bypass temporary 503 backend spikes."""
    for model_name in models_to_try:
        try:
            print(f"[System Engine] Attempting execution with model: {model_name}")
            response = client.models.generate_content(
                model=model_name,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    tools=available_tools,
                    temperature=0.2,
                )
            )
            return response, model_name
        except APIError as e:
            if e.code == 503:
                print(f"[!] Warning: {model_name} is overloaded (503). Attempting fallback...")
                continue
            raise e
    raise RuntimeError("All configured Gemini API models are currently experiencing high demand. Please try again in a moment.")

def get_agent_response(user_message: str, chat_history=None) -> str:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "System Error: GEMINI_API_KEY environment variable missing."

    client = genai.Client(api_key=api_key)
    
    # Priority cascade of models to handle heavy backend server spikes
    MODEL_CASCADE = ['gemini-3.1-flash-lite']
    
    available_tools = [
        wiki_tools.read_wiki_context,
        wiki_tools.search_wiki_content,
        wiki_tools.append_to_wiki
    ]

    system_instruction = (
        "You are the autonomous system administrator for a localized knowledge workspace. "
        "Your hard drive consists of a comprehensive textbook converted into markdown. "
        "Rules of Operation:\n"
        "1. Never guess mathematical formulas or text details. If the user asks about a concept, "
        "immediately use `read_wiki_context` or `search_wiki_content` to pull the ground truth.\n"
        "2. If you pull partial text and realize you need to see a deeper context to fully answer "
        "the query, call your search tool again with specific keywords before finalizing your answer.\n"
        "3. When the user introduces a valuable connection, summary, or an application of the theory, "
        "you must use `append_to_wiki` to save that state back to disk. Update the file silently "
        "and inform them it has been logged."
    )

    contents = []
    if chat_history:
        for role, text in chat_history:
            contents.append(types.Content(role=role, parts=[types.Part.from_text(text=text)]))
    
    contents.append(types.Content(role="user", parts=[types.Part.from_text(text=user_message)]))

    # Run primary execution loop with fallback handles intact
    response, active_model = run_generation(client, contents, system_instruction, available_tools, MODEL_CASCADE)

    # Check if the agent decided it executed a tool configuration
    if response.function_calls:
        for call in response.function_calls:
            tool_name = call.name
            args = call.args
            print(f"[Agent Action] Executing Tool Call: {tool_name} with args {args}")
            
            if tool_name == "read_wiki_context":
                tool_result = wiki_tools.read_wiki_context()
            elif tool_name == "search_wiki_content":
                tool_result = wiki_tools.search_wiki_content(query=args.get("query"))
            elif tool_name == "append_to_wiki":
                tool_result = wiki_tools.append_to_wiki(
                    section_title=args.get("section_title"),
                    update_content=args.get("update_content")
                )
            else:
                tool_result = "Execution Error: Unknown tool handle."

            # Construct tool feedback sequence
            tool_contents = [
                *contents,
                response.candidates[0].content,
                types.Content(
                    role="tool",
                    parts=[types.Part.from_function_response(
                        name=tool_name,
                        response={"result": tool_result}
                    )]
                )
            ]
            
            # Execute secondary output generation with the same fault-tolerant cascade
            final_response, _ = run_generation(
                client=client,
                contents=tool_contents,
                system_instruction=system_instruction,
                available_tools=available_tools,
                models_to_try=MODEL_CASCADE
            )
            return final_response.text

    return response.text