import openai
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

def prepare_prompt(system):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system),
        ("user", "{input}")
    ])
    return prompt

def prepare_model(open_ai_key, prompt, temperature=0):
    openai.openai_key = open_ai_key
    model = ChatOpenAI(temperature=temperature)
    chain = prompt | model
    return chain

def exec_model(chain, input):
    chain.invoke({"input": input})