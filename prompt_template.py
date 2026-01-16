from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini")

template2=PromptTemplate(
    template='Geert this person  in 5 languages. The  name  of the person is {name}',
    input_variables=['name']
)

prompt=template2.invoke({'name':'nitish'})

result=model.invoke(prompt)

print(result)

print("ayush kumar")