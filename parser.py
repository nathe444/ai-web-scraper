from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

template = """You are tasked with extracting specific information from the following text content:

{dom_content}

Please follow these instructions carefully:

1. Extract Information: Only extract the information that directly matches the provided description: {parse_description}
2. No Extra Content: Do not include any additional text, comments, or explanations in your response.
3. Empty Response: If no information matches the description, return an empty string ('').
4. Direct Data Only: Your output should contain only the data that is explicitly requested, with no other text."""

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
llm = ChatGroq(temperature=0.5)

def parse_with_groq(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        messages = prompt.format_messages(
            dom_content=chunk,
            parse_description=parse_description
        )
        response = llm.invoke(messages)
        print(f"parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response.content)

    return "\n".join(parsed_results)