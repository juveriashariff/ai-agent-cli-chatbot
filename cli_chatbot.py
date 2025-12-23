
import openai
#from dotenv import load_dotenv
#load_dotenv()
import os
from openai import OpenAI
from prompt_toolkit import prompt


//test

# Load your key from the environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# load your key from the .env file (or real env if present)
# openai.api_key = os.getenv("OPENAI_API_KEY")
#test

def chat():
    print("🤖 Welcome to your CLI Chatbot! (type 'exit' to quit)")
    history = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user_input = prompt("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break

        history.append({"role": "user", "content": user_input})

        # Original, pre-v1 interface
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=history
 )


        bot_reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": bot_reply})
        print("Charles:", bot_reply)

if __name__ == "__main__":
    chat()
 