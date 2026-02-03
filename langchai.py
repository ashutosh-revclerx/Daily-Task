# ==========================================================
# Super Comprehensive LLM
# LangChain + Gemini
# - Dynamic Prompt Templates
# - Temperature & Determinism
# - Output Parsers (Text + JSON)
# ==========================================================

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import BaseModel, Field

# 🔑 Set your Google API Key
os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY_HERE"

# ----------------------------------------------------------
# 1️⃣ Define a structured JSON schema using Pydantic
# ----------------------------------------------------------
class ExplanationSchema(BaseModel):
    topic: str = Field(description="Topic being explained")
    summary: str = Field(description="Concise technical explanation")
    key_points: list[str] = Field(description="Important bullet points")

def main():
    # ------------------------------------------------------
    # 2️⃣ Initialize Gemini with controlled randomness
    # ------------------------------------------------------
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2  # 🔒 Lower = more deterministic
    )

    # ------------------------------------------------------
    # 3️⃣ Dynamic prompt template (variable injection)
    # ------------------------------------------------------
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a precise, technical AI assistant. "
            "Follow instructions strictly and avoid unnecessary verbosity."
        ),
        (
            "human",
            "Explain the topic '{topic}' in a concise and technical manner."
        )
    ])

    # ------------------------------------------------------
    # 4️⃣ TEXT output chain (clean string)
    # ------------------------------------------------------
    text_chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    # ------------------------------------------------------
    # 5️⃣ JSON output chain (strict structured output)
    # ------------------------------------------------------
    json_parser = JsonOutputParser(pydantic_object=ExplanationSchema)

    json_prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a precise, technical AI assistant. "
            "Respond ONLY in valid JSON that matches the provided schema."
        ),
        (
            "human",
            "Explain the topic '{topic}'.\n{format_instructions}"
        )
    ]).partial(format_instructions=json_parser.get_format_instructions())

    json_chain = (
        json_prompt
        | llm
        | json_parser
    )

    # ------------------------------------------------------
    # 6️⃣ Invoke both chains
    # ------------------------------------------------------
    topic = "LangChain"

    text_response = text_chain.invoke({"topic": topic})
    json_response = json_chain.invoke({"topic": topic})

    # ------------------------------------------------------
    # 7️⃣ Display results
    # ------------------------------------------------------
    print("\n===== CLEAN TEXT OUTPUT =====\n")
    print(text_response)

    print("\n===== STRUCTURED JSON OUTPUT =====\n")
    print(json_response)

if __name__ == "__main__":
    main()
