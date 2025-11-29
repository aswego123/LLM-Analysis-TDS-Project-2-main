import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("GOOGLE_API_KEY not found in .env file")
    exit()

try:
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content("Say: Gemini key working")

    print("Response:", response.text)
    print("\n Gemini API key is valid!")

    models = genai.list_models()
    for m in models:
        print(m.name, "-", m.description)

except Exception as e:
    print("\n Error:", e)
    print("Gemini API key is NOT working.")



