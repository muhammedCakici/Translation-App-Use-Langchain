from dotenv import load_dotenv, dotenv_values

load_dotenv()

print(dotenv_values(".env").get("GEMINI_API_KEY"))
print("hello world")


