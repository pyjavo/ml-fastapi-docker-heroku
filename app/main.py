from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    '''Function that calls the predict method from the model

    Args:
        - payload's text should a string type

    Output:
        - language: The output should also be a string
    '''
    language = predict_pipeline(payload.text)
    return {"language": language}
