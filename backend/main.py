from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"message":"Bank Risk API"}

@app.post("/predict-risk")
def predict_risk():
    return {
        "risk_score":0.8,
        "decision":"REVIEW"
    }