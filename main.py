import os
from dotenv import load_dotenv
from groq import Groq

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables
groq_api_key = os.getenv("GROQ_API_KEY")


def user_prompt(message, description=""):
    client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )
    msg_value = "I need name suggestion for my restaurant name and the cuisine we will be serving is {}. Please give me a name and why I need to use it.".format(message)
    if description != "":
        description = "I also want you to name it in such a way that it matches my feeling with the idea. Also give me a tagline which I can use for adversitement. Idea is {}".format(description)
        
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": msg_value+" "+description,
            }
        ],
        model="llama3-8b-8192",
    )
    print(chat_completion)
    return chat_completion.choices[0].message.content