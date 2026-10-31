from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Model is up and running!"}

@app.get("/predict")
def predict():
    return {"prediction": [0.98, 0.02], "status": "success"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
