from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("GEMINI_API")

model=ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    api_key=api_key
)
chat_history=[
    SystemMessage(content="You are helpful ai assistant"),


]
while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        result=model.invoke('write goodbye message to user in one line')
        print(result.content)
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)