import os
from dotenv import load_dotenv
from groq import Groq


def load_api_key() -> str:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in the environment")
    return api_key


def build_messages() -> list[dict[str, str]]:
    return [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Please respond with a short, polite answer.",
        },
    ]


def main() -> None:
    api_key = load_api_key()
    client = Groq(api_key=api_key)
    model = "llama-3.3-70b-versatile"
    messages = build_messages()
    response = client.chat.completions.create(model=model, messages=messages, temperature=0)

    print("#######################################\n")
    answer = response.choices[0].message.content
    print(answer)


if __name__ == "__main__":
    main()
