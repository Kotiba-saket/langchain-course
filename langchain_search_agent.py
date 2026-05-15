from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

load_dotenv()

llm = ChatGroq(temperature=0, model="llama-3.1-8b-instant")
tavily = TavilySearch(max_result=2)
@tool
def search(query:str) -> str:
    """
    Tool that search over internet
    Args:
        query: the query to search for
        Returns: The search result
    """
    print(f"Searching for {query}")
    return tavily.invoke(query)
llm = ChatOpenAI(model="gpt-4o")
tools = [tavily]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage("search for 3 job postings for an ai engineer using langchain in in belgium on linkedin and list their details ")})
    print(result)

if __name__ == "__main__":
    main()
  