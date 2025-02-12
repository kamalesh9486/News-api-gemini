from fastapi import FastAPI, HTTPException
import google.generativeai as genai
import requests
import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Load API keys
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

# Store the latest news data globally
latest_news = ""

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to ["http://127.0.0.1:8001"] for more security
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
def fetch_news_articles(query, num_articles=5):
    """Fetches news from NewsAPI based on the query."""
    global latest_news
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        news_data = response.json()

        if news_data.get("status") != "ok":
            raise HTTPException(status_code=400, detail=news_data.get("message", "Unknown error"))

        articles = news_data.get("articles", [])[:num_articles]
        if not articles:
            return "No news articles found."

        latest_news = "\n".join([f"{i+1}. {a['title']} - {a['source']['name']} (Published: {a['publishedAt']})\n{a['description']}" for i, a in enumerate(articles)])

        return {"news": latest_news}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Network error: {str(e)}")

@app.get("/")
def home():
    return {"message": "Welcome to the AI News Chatbot API"}

@app.get("/fetch_news/")
def fetch_news(query: str):
    """API endpoint to fetch news."""
    return fetch_news_articles(query)

@app.get("/ask_news/")
def ask_about_news(user_question: str):
    """API endpoint to ask questions about fetched news."""
    global latest_news
    if not latest_news:
        raise HTTPException(status_code=400, detail="No news data available. Fetch news first.")

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            f"Based on these news articles, answer:\n\n{latest_news}\n\n"
            f"Question: {user_question}\n\n"
        )

        return {"answer": response.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")
