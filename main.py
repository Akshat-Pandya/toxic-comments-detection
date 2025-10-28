from fastapi import FastAPI, Request
import google.generativeai as genai
import os

app = FastAPI()

genai.configure(api_key="AIzaSyBS0gcokMgWfQPJgqhPlBFW1AxQrNdlTC8")

model = genai.GenerativeModel("gemini-2.5-flash")

@app.post("/classify")
async def classify_text(request: Request):
    data = await request.json()
    content = data.get("content", "")

    prompt = f"""
    Classify the following text into categories:
    toxic, severe_toxic, obscene, threat, insult, identity_hate.
    The text can be in English or Hindi or mixed.
    Return output in JSON format like:
    {{
      "toxic": <percentage>,
      "severe_toxic": <percentage>,
      "obscene": <percentage>,
      "threat": <percentage>,
      "insult": <percentage>,
      "identity_hate": <percentage>
    }}

    Text: "{content}"
    """

    response = model.generate_content(prompt)
    return {"result": response.text}
