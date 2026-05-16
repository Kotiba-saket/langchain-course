from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel,Field
#llm = ChatGroq(temperature=0, model="llama-3.1-8b-instant")
load_dotenv()
class Source(BaseModel):
    """Schema for a source used by the agent"""
    url:str = Field(description="The url of the source")

class AgentResponse(BaseModel):
    """Schema for the agent response with answer and responses"""
    answer:str = Field(description="The agent answer to the query")
    sources: List[Source] = Field(default_factory=list,description="the list of sources used to gererate the answer")

 
llm = ChatOpenAI(model="gpt-4o")
tools = [TavilySearch(max_result=2)]
agent = create_agent(model=llm,tools=tools,response_format=AgentResponse)

def main():
     print("Hello from langchain-course!")

     result = agent.invoke({"messages":HumanMessage("search for 3 job postings for an ai engineer using langchain in in belgium on linkedin and list their details ")})
     print(result)
 
   

if __name__ == "__main__":
    main()
  