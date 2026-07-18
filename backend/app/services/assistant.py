def process_message(message:str):
    return{
        "user_message":message,
        "assistant_reply":f"You said {message}"
    }