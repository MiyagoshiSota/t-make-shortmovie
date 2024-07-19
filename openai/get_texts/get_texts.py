import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(organization='org-xbVs2KXBJkBYHu8EylNpsix1',
                project='proj_DGijuCgQp8owbF3tfUMj80T2',
                api_key=os.getenv("API_KEY"))

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": "Say this is a test"
    }],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
