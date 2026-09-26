from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import joblib

# Create FastAPI app
app = FastAPI(
    title="Fake News Detection API",
    description="API for detecting fake news using Machine Learning",
    version="1.0.0"
)

# 1. Enable CORS so Next.js frontend can communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production-এ নির্দিষ্ট URL দিতে পারেন (যেমন: ["http://localhost:3000"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model and TF-IDF vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


@app.get("/")
def home():
    return {
        "message": "Fake News Detection API is running!"
    }


@app.post("/predict")
def predict(news: str = Form(...)):  # 2. Form(...) ব্যবহার করা হয়েছে Form Data রিসিভ করার জন্য

    # Convert news text into TF-IDF features
    news_tfidf = vectorizer.transform([news])

    # Make prediction
    prediction = model.predict(news_tfidf)[0]

    # Convert prediction result to readable text (e.g., "Fake News" or "Real News")
    # প্রয়োজন অনুযায়ী লেবেল পরিবর্তন করে নিতে পারেন
    result_label = "Fake News" if int(prediction) == 1 else "Real News"

    return {
        "prediction": result_label
    }