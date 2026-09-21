from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = """"

You are an expert in answering question about a pizza restaurant

Here are some relevant reviews : {reviews}

Here is the questions to answer : {question}

"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

result = chain.invoke({"reviews": [], "question": "que disent les avis negatives de bella vitta ? "})
print(result)