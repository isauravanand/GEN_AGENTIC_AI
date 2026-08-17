import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key missing")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"


def llm_ans(prompt):
    message = {
        "role": "user",
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    ans = response.choices[0].message.content

    return ans


bad_prompt = """
You are an AI customer-support ticket classifier.

ROLE:
You are an expert customer-support analyst. Your job is to understand customer complaints and classify them accurately.

TASK:
Analyze the user's complaint and classify it into exactly one of these categories:
- Technical Issue
- Payment Issue
- Account Issue
- Delivery Issue
- Product Issue
- General Complaint

Also determine the priority:
- Low
- Medium
- High
- Critical

CONSTRAINTS:
1. Return exactly one category.
2. Return exactly one priority.
3. Do not invent information that is not present in the complaint.
4. Base the classification only on the user's message.
5. If multiple categories seem possible, choose the category that is most directly related to the main problem.
6. Keep the reason concise, within 2 sentences.
7. Do not include unnecessary explanations or additional fields.

OUTPUT FORMAT:
in one word only , if not from the categories , return OTHER 

USER COMPLAINT:
my girlfriend left me    
"""

print(llm_ans(bad_prompt))