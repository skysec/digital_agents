from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def prepare_prompt(system):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system),
        ("user", "{input}")
    ])
    return prompt

def prepare_model(openai_api_key, prompt, temperature=0):
    output_parser = StrOutputParser()
    model = ChatOpenAI(openai_api_key=openai_api_key,model="gpt-4-0613", temperature=temperature)
    chain = (
        {"input": RunnablePassthrough()} 
        | prompt
        | model
        | output_parser
    )
    return chain

def exec_model(chain, input):
    result = chain.invoke({"input": input})
    return result

def load_system(system):
    with open(system, 'r') as f:
        system = f.read()
    return system

def summarize(system, input, open_ai_key, temperature=0):
    system = load_system(system)
    prompt = prepare_prompt(system)
    model = prepare_model(open_ai_key, prompt, temperature)
    result = exec_model(model, input)
    return result