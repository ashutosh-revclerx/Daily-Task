# ==========================================================
# Streaming Output with LangChain + Gemini
# - Prompt Template
# - Deterministic Temperature
# - Token-by-token Streaming
# ==========================================================

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# 🔑 Set your Google API Key
os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY_HERE"

def main():
    # ------------------------------------------------------
    # 1️⃣ Initialize Gemini with streaming enabled
    # ------------------------------------------------------
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,   # deterministic
        streaming=True     # 🔥 ENABLE STREAMING
    )

    # ------------------------------------------------------
    # 2️⃣ Dynamic prompt template
    # ------------------------------------------------------
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a precise, technical AI assistant. "
            "Explain concepts clearly and concisely."
        ),
        (
            "human",
            "Explain the topic '{topic}' in a concise technical manner."
        )
    ])

    # ------------------------------------------------------
    # 3️⃣ Create streaming chain
    # ------------------------------------------------------
    chain = prompt | llm

    # ------------------------------------------------------
    # 4️⃣ Stream output token-by-token
    # ------------------------------------------------------
    topic = "LangChain streaming output"

    print("\n===== STREAMING RESPONSE =====\n")

    for chunk in chain.stream({"topic": topic}):
        # Each chunk is an AIMessageChunk
        if chunk.content:
            print(chunk.content, end="", flush=True)

    print("\n\n===== STREAM COMPLETE =====")

if __name__ == "__main__":
    main()
