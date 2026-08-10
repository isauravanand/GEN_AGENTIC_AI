import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"

#promts

promt1="hi"
promt2="Explain Machine learning in detail"
promt3="Write a 1000 word eassy on Agentic AI"

prompts=[promt1,promt2,promt3]
for prompt in prompts:
    message={
        "role": role,
        "content": prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages, max_tokens=500)
    usage=response.usage
    print(
        f"Prompt: {prompt} --> your tokens: {usage.prompt_tokens} "
        f"completion_tokens: {usage.completion_tokens} "
        f"total_tokens: {usage.total_tokens} "
        f"Finish Reason: {response.choices[0].finish_reason}"
    )



# # message me role and content


# # print(response)

# print("#######################################\n")

# answer=response.choices[0].message.content
# print(answer)