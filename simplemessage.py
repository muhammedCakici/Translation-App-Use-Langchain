from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

messages =[
    SystemMessage(content="Translate the following from Turkish to English"),
    HumanMessage(content="Merhaba")
    
]

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")
parser = StrOutputParser()

chain = model | parser

print(chain.invoke(messages))


