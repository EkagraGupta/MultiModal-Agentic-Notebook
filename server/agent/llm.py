def chat(messages):
    last_user_message = next(
        (m["content"] for m in reversed(messages) if m["role"]=="user"), ""
    )

    return f"[llm]  I read: '{last_user_message}' - dummy right now."