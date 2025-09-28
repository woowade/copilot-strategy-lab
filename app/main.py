# main.py
from fastapi import FastAPI
from consumer import start_consumer

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await start_consumer()

@app.get("/health")
def health():
    return {"status": "ok"}
