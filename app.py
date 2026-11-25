"""LangChain Q&A Assistant (command line) using Google Gemini."""

import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------- Settings ----------
MODEL_NAME = "gemini-3.7-flash"  # change this line if Google renames the model
MAX_TURNS = 5                    # remember only the last 5 exchanges

# ---------- API key (read from the .env file, never written in code) ----------
load_dotenv(override=True)
if not os.getenv("GOOGLE_API_KEY"):
    raise SystemExit("GOOGLE_API_KEY is missing. Copy .env.example to .env and add your key.")

# ---------- Prompt template (with a slot for conversation history) ----------
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful Q&A assistant. Answer clearly in simple language, "
     "in under 150 words. If you are not sure, say so instead of guessing."),
    MessagesPlaceholder("history"),
    ("human", "{question}"),
])

# ---------- Model and chain: prompt -> model -> plain text ----------
llm = ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=0.3)
chain = prompt | llm | StrOutputParser()

history = []


def to_text(answer):
    """Make sure the answer is a plain string, whatever format the model returns."""
    if isinstance(answer, str):
        return answer
    if isinstance(answer, list):
        parts = []
        for part in answer:
            if isinstance(part, dict):
                parts.append(part.get("text", ""))
            else:
                parts.append(str(part))
        return "".join(parts)
    return str(answer)


def ask(question):
    """Send one question to the model and return a readable answer."""
    global history

    question = question.strip()

    # Handle empty questions
    if not question:
        return "Please type a question."

    # Handle API errors without crashing the program
    try:
        answer = to_text(chain.invoke({"question": question, "history": history}))
    except Exception as e:
        reason = str(e).replace("\n", " ")[:200]
        return (f"Sorry, the API call failed ({type(e).__name__}). "
                f"Check your key, model name, internet or rate limit. Details: {reason}")

    # Save the exchange and keep the history short
    history += [HumanMessage(content=question), AIMessage(content=answer)]
    history = history[-MAX_TURNS * 2:]
    return answer


def main():
    print("Q&A Assistant ready. Type 'quit' to exit.")
    while True:
        try:
            q = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if q.strip().lower() in ("quit", "exit"):
            print("Goodbye!")
            break
        print("\nAssistant:", ask(q))


if __name__ == "__main__":
    main()