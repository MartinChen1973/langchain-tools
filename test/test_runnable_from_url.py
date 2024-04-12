from src.retriever.LangchainRetriever import LangChainRetriever
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def test_runnable_from_url(url):
    runnable = LangChainRetriever.create_runnable_from_url(url)
    template = "仅依赖下面的context回答用户的问题:\n{context}\n\nQuestion: {question}\n"
    prompt = ChatPromptTemplate.from_template(template)
    model = ChatOpenAI()
    output_parser = StrOutputParser()

    chain = runnable | prompt | model | output_parser

    question = "Can Langsmith help with testing?"
    result = chain.invoke(question)
    assert "Yes" in result
    print("✔ Assertion succeeded (Url Runnable): 'Yes' is in the result")