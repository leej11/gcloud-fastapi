# app.py
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

lookup = {
    'Liam': '30 years old',
    'Vincent': '64 years old',
}

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World from Google Cloud Run!"}

# Endpoint that takes a query parameter and returns information
@app.get("/info")
def get_info(name: Optional[str] = None):
    if name:
        return {"message": f"Hello, {name}! Welcome to Google Cloud Run with FastAPI. You are {lookup[name]}"}
    else:
        return {"message": "Hello! Provide a 'name' parameter to personalize the response."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
