from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

#in the below code we use it for deploy on the local host
from fastapi import FastAPI
from langserve import add_routes

load_dotenv()

#messages =[
#   SystemMessage(content="Translate the following from Turkish to English"),
#  HumanMessage(content="Merhaba")
    
#]

system_prompt = ("Translate the following into {language}")
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt) , ("user", "{text}" )
        
    ]
)

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")
parser = StrOutputParser()

chain = prompt_template| model | parser

app=FastAPI(title="Translation App",
            version="1.0.0",
            description="Gemini"
            )

add_routes(app,
           chain,
           path="/chain"
           )

#if you write manuel output 
#print(chain.invoke({"language":"English","text":"Merhaba"}))

import uvicorn
uvicorn.run(app,host="localhost",port=8000)



