from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.services.medical_assistant.prompt_loader import prompt_loader
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    prompt_loader.load_prompts()

@app.get("/")
def read_root():
    return {"message": "Backend Server is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000)