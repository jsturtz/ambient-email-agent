import os
from pathlib import Path

from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    # Fallback to load .env if python-dotenv is not installed yet
    env_file = Path(__file__).resolve().parent / ".env"
    if env_file.is_file():
        with open(env_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    os.environ.setdefault(key.strip(), value.strip().strip("'\""))

if not os.environ.get("GOOGLE_API_KEY") and not os.environ.get("GEMINI_API_KEY"):
    raise SystemExit(
        "Error: Missing Google Gemini API key.\n"
        "Please copy .env.example to .env and set GOOGLE_API_KEY, or export it in your environment.\n"
        "Get an API key from Google AI Studio: https://aistudio.google.com/app/apikey"
    )

model = init_chat_model("google_genai:gemini-2.5-flash")


def main():
    agent = create_deep_agent(model=model)

    result = agent.invoke({"messages": [{"role": "user", "content": "What is an LLM?"}]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()