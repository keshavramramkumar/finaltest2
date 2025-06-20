# Copyright (c) OSpectra AI Inc. All rights reserved.
# Owned by OSpectra AI
# Example: Uses OpenAI to generate a haiku using ChatGPT
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Write a haiku about the beauty of nature.",
        }
    ],
    model="gpt-4o-mini",
)

print(response.choices[0].message.content)
# Owned by OSpectra AI
