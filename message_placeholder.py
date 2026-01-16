from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder

chat_template=ChatPromptTemplate([
    ('system','you are behave in customer support type'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}'),
])

chat_history=[]

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())



print(chat_history)


result=chat_template.invoke({'chat_history':chat_history,'query':"where is my  refund"})

print(result)
print(result.content)

