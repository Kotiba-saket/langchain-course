<<<<<<< HEAD
import os
=======

>>>>>>> d287944 (RAG)
from operator import itemgetter

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
<<<<<<< HEAD
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

print("Initializing components...")

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI()

vectorstore = PineconeVectorStore(
    index_name=os.environ["INDEX_NAME"], embedding=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

prompt_template = ChatPromptTemplate.from_template(
    """Answer the question based only on the following context:

{context}

Question: {question}

Provide a detailed answer:"""
)


def format_docs(docs):
    """Format retrieved documents into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)


# ============================================================================
# IMPLEMENTATION 1: Without LCEL (Simple Function-Based Approach)
# ============================================================================
def retrieval_chain_without_lcel(query: str):
    """
    Simple retrieval chain without LCEL.
    Manually retrieves documents, formats them, and generates a response.

    Limitations:
    - Manual step-by-step execution
    - No built-in streaming support
    - No async support without additional code
    - Harder to compose with other chains
    - More verbose and error-prone
    """
    # Step 1: Retrieve relevant documents
    docs = retriever.invoke(query)

    # Step 2: Format documents into context string
    context = format_docs(docs)

    # Step 3: Format the prompt with context and question
    messages = prompt_template.format_messages(context=context, question=query)

    # Step 4: Invoke LLM with the formatted messages
    response = llm.invoke(messages)

    # Step 5: Return the content
    return response.content


# ============================================================================
# IMPLEMENTATION 2: With LCEL (LangChain Expression Language) - BETTER APPROACH
# ============================================================================
def create_retrieval_chain_with_lcel():
    """
    Create a retrieval chain using LCEL (LangChain Expression Language).
    Returns a chain that can be invoked with {"question": "..."}

=======
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import os
load_dotenv()
print("Intializing Components...")


embedding = OpenAIEmbeddings()
llm = ChatOpenAI()
vectorestore = PineconeVectorStore(
    embedding=embedding,
    index_name=os.environ.get("INDEX_NAME")
)

retrierver = vectorestore.as_retriever(search_kwargs={"k": 3})

prompt_template = ChatPromptTemplate.from_template(
    """"Answer the question based only in the following context :
    {context}
    Question: {question}
    Provide a detailed answers:"""
)

def format_docs(docs):
    """Format the retrieved documents into a string."""
    return "\n\n".join(doc.page_content for doc in docs)
#=================================================================
# Implementaion1 : Without LCEL
#=================================================================
def retriever_chain_without_lcel(query : str):
    """Simple retriever chain without LCE.
    Manuwally retrieves documents, formats them, and generate a response.
    Limitations: 
    - manual step by step execution
    - No build in streaming support
    - no async support without additional code
    - Header to compse with other chains
    - Moer verbose and error-prone"""

    docs = retrierver.invoke(query)
    context = format_docs(docs)
    messages = prompt_template.format_messages(context=context, question=query)
    response = llm.invoke(messages)
    return response.content


#=================================================================
# Implementaion1 : With LCEL
#=================================================================
#   
def retriever_chain_with_lcel():
    """Create a retriever chain using LCEL
    returns a chahin that can be invoked without {"question": query} 
     
>>>>>>> d287944 (RAG)
    Advantages over non-LCEL approach:
    - Declarative and composable: Easy to chain operations with pipe operator (|)
    - Built-in streaming: chain.stream() works out of the box
    - Built-in async: chain.ainvoke() and chain.astream() available
    - Batch processing: chain.batch() for multiple inputs
    - Type safety: Better integration with LangChain's type system
    - Less code: More concise and readable
    - Reusable: Chain can be saved, shared, and composed with other chains
    - Better debugging: LangChain provides better observability tools
    """
<<<<<<< HEAD
    retrieval_chain = (
        RunnablePassthrough.assign(
            context=itemgetter("question") | retriever | format_docs
=======
     # when we use the the pip langchain automaticaly convert te py (format_docs) function into runnablelambda 
    retrierver_chain = (
        RunnablePassthrough.assign(
            context=itemgetter("question") | retrierver | format_docs
>>>>>>> d287944 (RAG)
        )
        | prompt_template
        | llm
        | StrOutputParser()
    )
<<<<<<< HEAD
    return retrieval_chain


if __name__ == "__main__":
    print("Retrieving...")

    # Query
    query = "what is Pinecone in machine learning?"

    # ========================================================================
    # Option 0: Raw invocation without RAG
    # ========================================================================
    print("\n" + "=" * 70)
    print("IMPLEMENTATION 0: Raw LLM Invocation (No RAG)")
    print("=" * 70)
    result_raw = llm.invoke([HumanMessage(content=query)])
    print("\nAnswer:")
    print(result_raw.content)

    # ========================================================================
    # Option 1: Use implementation WITHOUT LCEL
    # ========================================================================
    print("\n" + "=" * 70)
    print("IMPLEMENTATION 1: Without LCEL")
    print("=" * 70)
    result_without_lcel = retrieval_chain_without_lcel(query)
    print("\nAnswer:")
    print(result_without_lcel)

    # ========================================================================
    # Option 2: Use implementation WITH LCEL (Better Approach)
    # ========================================================================
    print("\n" + "=" * 70)
    print("IMPLEMENTATION 2: With LCEL - Better Approach")
    print("=" * 70)
    print("Why LCEL is better:")
    print("- More concise and declarative")
    print("- Built-in streaming: chain.stream()")
    print("- Built-in async: chain.ainvoke()")
    print("- Easy to compose with other chains")
    print("- Better for production use")
    print("=" * 70)

    chain_with_lcel = create_retrieval_chain_with_lcel()
    result_with_lcel = chain_with_lcel.invoke({"question": query})
    print("\nAnswer:")
    print(result_with_lcel)
=======
    return retrierver_chain
    
if __name__ == '__main__':
    print("Retrieving...")
    query = "what is the Pinecone in machine learning?"

    # result_without_lcel = retriever_chain_without_lcel(query)
    # print(result_without_lcel)

    print("*" * 50)
    print("Using LCEL...")
    retrierver_chain = retriever_chain_with_lcel()
    result_with_lcel = retrierver_chain.invoke({"question": query})
    print(result_with_lcel)



>>>>>>> d287944 (RAG)
