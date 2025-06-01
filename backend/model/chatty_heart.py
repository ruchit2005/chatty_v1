# %%
##Importing all our librariesimport os
#from google.colab import userdata
#api_key = userdata.get('HUGGINGFACE_API_KEY')
from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
port = int(os.environ.get("PORT", 8000))
from huggingface_hub import InferenceClient

client = InferenceClient(
        provider="hf-inference",
        api_key=api_key,
    )




# %%
app = FastAPI()
class Message(BaseModel):
    message: str
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chatty-v1-1.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# %%
## Get the MystralAI model into my project
@app.get("/")
def home():
    return {"message": "Backend is working"}

from fastapi.responses import JSONResponse

import logging

logging.basicConfig(level=logging.INFO)





@app.post("/chat")

async def chat_endpoint(message: Message):
    logging.info(f"Received message: {message.message}")
    logging.info(f"API Key Present: {bool(api_key)}")
    try:
        
        prompt = message.message
        completion = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.3",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Your name is chatty and your creator is Ruchit also known as Suzuru. "
                        "Before taking input from the user, you must introduce yourself as chatty and your creator as Ruchit. "
                        "You are a helpful after hours teacher who helps students with all their assignments and research. "
                        "You also take care of a student's well-being and guide them through studies and mental health."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                },
            ],
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

    #return {"response": completion.choices[0].message.content}
# from huggingface_hub import InferenceClient

# client = InferenceClient(
#     provider="hf-inference",
#     api_key=api_key,
# )

# completion = client.chat.completions.create(
#     model="mistralai/Mistral-7B-Instruct-v0.3",
#     messages=[

#         {
#             "role" : "system",
#             "content" : (
#                 "You are a helpful after hours teacher who help students with all their assignments and research."
#                 "You also take care of a student's well being and u help them by guiding them through studies and mental health"
#               )
#         },
#          {
#             "role": "user",
#             "content": prompt
#         },
#     ],
# )

# print(completion.choices[0].message.content)

# %%



