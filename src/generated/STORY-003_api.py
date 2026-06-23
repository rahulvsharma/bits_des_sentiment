from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

app = FastAPI(title="Market Sentiment Analysis")

class SentimentRequest(BaseModel):
    text: str
    source: str

class SentimentResult(BaseModel):
    text: str
    positive: float
    negative: float
    neutral: float
    compound: float

sia = SentimentIntensityAnalyzer()

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "sentiment"}

@app.post("/sentiment/analyze")
def analyze_sentiment(request: SentimentRequest) -> SentimentResult:
    scores = sia.polarity_scores(request.text)
    return SentimentResult(
        text=request.text,
        positive=scores['pos'],
        negative=scores['neg'],
        neutral=scores['neu'],
        compound=scores['compound']
    )

@app.get("/sentiment/market")
def get_market_sentiment():
    return {
        "overall": "bullish",
        "confidence": 0.85,
        "trend": "upward",
        "last_updated": "2024-01-15T10:30:00Z"
    }
