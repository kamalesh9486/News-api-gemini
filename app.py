# # # # # # import openai
# # # # # # import requests

# # # # # # # Set API keys
# # # # # # openai.api_key = "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"
# # # # # # NEWS_API_KEY = "3de8bebf953749aaa7b47527c495089d"

# # # # # # def get_latest_news(category="general", country="us"):
# # # # # #     url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={NEWS_API_KEY}"
    
# # # # # #     response = requests.get(url)
# # # # # #     if response.status_code == 200:
# # # # # #         articles = response.json().get("articles", [])
# # # # # #         if not articles:
# # # # # #             return "No news found for this category."

# # # # # #         # Extract top 3 news headlines
# # # # # #         news_summary = "\n".join([f"{i+1}. {articles[i]['title']}" for i in range(min(3, len(articles)))])
# # # # # #         return f"Here are the latest {category} news:\n{news_summary}"
    
# # # # # #     return "Sorry, I couldn't fetch the news."

# # # # # # def chatbot(user_input):
# # # # # #     if "news" in user_input.lower():
# # # # # #         # Extract category if provided (e.g., "Tell me tech news")
# # # # # #         words = user_input.lower().split()
# # # # # #         categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
# # # # # #         category = next((word for word in words if word in categories), "general")

# # # # # #         api_response = get_latest_news(category)
# # # # # #     else:
# # # # # #         api_response = "I can fetch the latest news for you. Try asking: 'Tell me the latest tech news'."

# # # # # #     prompt = f"User asked: {user_input}\nAPI response: {api_response}\nGenerate a helpful answer:"

# # # # # #     chat_response = openai.ChatCompletion.create(
# # # # # #         model="gpt-3.5-turbo",
# # # # # #         messages=[
# # # # # #             {"role": "system", "content": "You are a helpful assistant."},
# # # # # #             {"role": "user", "content": prompt}
# # # # # #         ]
# # # # # #     )

# # # # # #     return chat_response["choices"][0]["message"]["content"]

# # # # # # # Test chatbot with a news query
# # # # # # user_input = "Tell me the latest technology news"
# # # # # # print(chatbot(user_input))
# # # # # import openai
# # # # # import requests

# # # # # # Set API keys
# # # # # openai.api_key = "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"
# # # # # NEWS_API_KEY = "3de8bebf953749aaa7b47527c495089d"

# # # # # def get_latest_news(category="general", country="us"):
# # # # #     url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={NEWS_API_KEY}"
    
# # # # #     response = requests.get(url)
# # # # #     if response.status_code == 200:
# # # # #         articles = response.json().get("articles", [])
# # # # #         if not articles:
# # # # #             return "No news found for this category."

# # # # #         # Extract top 3 news headlines
# # # # #         news_summary = "\n".join([f"{i+1}. {articles[i]['title']}" for i in range(min(3, len(articles)))])
# # # # #         return f"Here are the latest {category} news:\n{news_summary}"
    
# # # # #     return "Sorry, I couldn't fetch the news."

# # # # # def chatbot(user_input):
# # # # #     if "news" in user_input.lower():
# # # # #         words = user_input.lower().split()
# # # # #         categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
# # # # #         category = next((word for word in words if word in categories), "general")

# # # # #         api_response = get_latest_news(category)
# # # # #     else:
# # # # #         api_response = "I can fetch the latest news for you. Try asking: 'Tell me the latest tech news'."

# # # # #     prompt = f"User asked: {user_input}\nAPI response: {api_response}\nGenerate a helpful answer:"

# # # # #     chat_response = openai.chat.completions.create(  # ✅ Updated syntax
# # # # #         model="gpt-3.5-turbo",
# # # # #         messages=[
# # # # #             {"role": "system", "content": "You are a helpful assistant."},
# # # # #             {"role": "user", "content": prompt}
# # # # #         ]
# # # # #     )

# # # # #     return chat_response.choices[0].message.content  # ✅ Updated syntax

# # # # # # Test chatbot with a news query
# # # # # user_input = "Tell me the latest technology news"
# # # # # print(chatbot(user_input))
# # # # import openai

# # # # # Replace with your OpenAI API key
# # # # OPENAI_API_KEY = "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"

# # # # # Configure OpenAI client
# # # # openai.api_key = OPENAI_API_KEY

# # # # def chatbot(user_input):
# # # #     try:
# # # #         response = openai.ChatCompletion.create(
# # # #             model="gpt-3.5-turbo",  # Free-tier model
# # # #             messages=[{"role": "system", "content": "You are a helpful chatbot."},
# # # #                       {"role": "user", "content": user_input}],
# # # #             temperature=0.7
# # # #         )
# # # #         return response["choices"][0]["message"]["content"]

# # # #     except openai.error.RateLimitError:
# # # #         return "You've reached the free usage limit. Check OpenAI's billing page."

# # # # # Simple chat loop
# # # # print("Chatbot is ready! Type 'exit' to quit.")
# # # # while True:
# # # #     user_input = input("You: ")
# # # #     if user_input.lower() == "exit":
# # # #         break
# # # #     print("Chatbot:", chatbot(user_input))


# # # # import openai

# # # # # Replace with your OpenAI API key
# # # # OPENAI_API_KEY = "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"

# # # # # Configure OpenAI client
# # # # client = openai.OpenAI(api_key=OPENAI_API_KEY)

# # # # def chatbot(user_input):
# # # #     try:
# # # #         response = client.chat.completions.create(
# # # #             model="gpt-3.5-turbo",  # Free-tier model
# # # #             messages=[
# # # #                 {"role": "system", "content": "You are a helpful chatbot."},
# # # #                 {"role": "user", "content": user_input}
# # # #             ],
# # # #             temperature=0.7
# # # #         )
# # # #         return response.choices[0].message.content

# # # #     except openai.APIError as e:
# # # #         return f"OpenAI API error: {e}"
# # # #     except openai.RateLimitError:
# # # #         return "You've reached the free usage limit. Check OpenAI's billing page."
# # # #     except Exception as e:
# # # #         return f"An error occurred: {e}"

# # # # # Simple chat loop
# # # # print("Chatbot is ready! Type 'exit' to quit.")
# # # # while True:
# # # #     user_input = input("You: ")
# # # #     if user_input.lower() == "exit":
# # # #         break
# # # #     print("Chatbot:", chatbot(user_input))
# # # # import google.generativeai as genai

# # # # # Replace with your actual Gemini API key
# # # # GEMINI_API_KEY = "AIzaSyCGwNBHPB_1maOaympIMtlNVtFEftIoKec"

# # # # # Configure Gemini AI
# # # # genai.configure(api_key=GEMINI_API_KEY)

# # # # def chatbot(user_input):
# # # #     try:
# # # #         model = genai.GenerativeModel("gemini-pro")  # Use the free Gemini model
# # # #         response = model.generate_content(user_input)
# # # #         return response.text

# # # #     except Exception as e:
# # # #         return f"An error occurred: {e}"

# # # # # Simple chat loop
# # # # print("Gemini AI Chatbot is ready! Type 'exit' to quit.")
# # # # while True:
# # # #     user_input = input("You: ")
# # # #     if user_input.lower() == "exit":
# # # #         break
# # # #     print("Chatbot:", chatbot(user_input))
# # # import google.generativeai as genai
# # # import requests

# # # # Replace with your API keys
# # # GEMINI_API_KEY = "AIzaSyCGwNBHPB_1maOaympIMtlNVtFEftIoKec"
# # # NEWS_API_KEY = "3de8bebf953749aaa7b47527c495089d"

# # # # Configure Gemini AI
# # # genai.configure(api_key=GEMINI_API_KEY)

# # # def fetch_news(query, num_articles=5):
# # #     """Fetches top news articles from News API based on the query."""
# # #     url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    
# # #     try:
# # #         response = requests.get(url)
# # #         news_data = response.json()

# # #         if news_data["status"] != "ok":
# # #             return f"Error fetching news: {news_data.get('message', 'Unknown error')}"

# # #         articles = news_data.get("articles", [])[:num_articles]
# # #         if not articles:
# # #             return "No news articles found."

# # #         # Format news for Gemini AI
# # #         formatted_news = "\n".join([f"{i+1}. {a['title']} - {a['source']['name']}" for i, a in enumerate(articles)])
# # #         return formatted_news

# # #     except Exception as e:
# # #         return f"Error: {e}"

# # # def chatbot(user_input):
# # #     """Processes user input, fetches news, and generates a response using Gemini AI."""
# # #     try:
# # #         # Fetch relevant news articles
# # #         news_summary = fetch_news(user_input)
# # #         print("THIS from API",news_summary)
# # #         # Provide news context to Gemini AI
# # #         model = genai.GenerativeModel("gemini-pro")
# # #         response = model.generate_content(f"Here are the latest news articles about {user_input}:\n{news_summary}\n\nSummarize and provide insights.")
        
# # #         return response.text

# # #     except Exception as e:
# # #         return f"An error occurred: {e}"

# # # # Chatbot interaction loop
# # # print("Gemini AI News Chatbot is ready! Type 'exit' to quit.")
# # # while True:
# # #     user_input = input("You: ")
# # #     if user_input.lower() == "exit":
# # #         break
# # #     print("Chatbot:", chatbot(user_input),"NEWNEWNEW",response.text)
# # #     #print("THIS from API",news_summary)

# # # import requests

# # # NEWS_API_KEY = "3de8bebf953749aaa7b47527c495089d"

# # # def get_latest_news(category="general", country="us"):
# # #     url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={NEWS_API_KEY}"
    
# # #     response = requests.get(url)
# # #     if response.status_code == 200:
# # #         articles = response.json().get("articles", [])
# # #         if not articles:
# # #             return "No news found for this category."

# # #         # Extract top 3 news headlines
# # #         news_summary = "\n".join([f"{i+1}. {articles[i]['title']}" for i in range(min(3, len(articles)))])
# # #         return f"Here are the latest {category} news:\n{news_summary}"
    
# # #     return "Sorry, I couldn't fetch the news."

# # # # Test chatbot with a news query
# # # user_input = "Tell me the latest technology news"
# # # print(get_latest_news("business"))
# # # import google.generativeai as genai
# # # import requests


# # # GEMINI_API_KEY = "AIzaSyCGwNBHPB_1maOaympIMtlNVtFEftIoKec"
# # # NEWS_API_KEY = "3de8bebf953749aaa7b47527c495089d"

# # # def fetch_news(query, num_articles=5):
# # #     """Fetches top news articles from News API based on the query."""
# # #     url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"

# # #     try:
# # #         response = requests.get(url)
# # #         news_data = response.json()

# # #         if news_data["status"] != "ok":
# # #             return f"Error fetching news: {news_data.get('message', 'Unknown error')}"

# # #         articles = news_data.get("articles", [])[:num_articles]
# # #         if not articles:
# # #             return "No news articles found."

# # #         # Print raw news data for verification
# # #         print("\n[DEBUG] Raw News API Response:", news_data, "\n")

# # #         # Format news for Gemini AI
# # #         formatted_news = "\n".join([f"{i+1}. {a['title']} - {a['source']['name']}" for i, a in enumerate(articles)])
# # #         return formatted_news

# # #     except Exception as e:
# # #         return f"Error: {e}"
# # # def chatbot(user_input):
# # #     """Fetch news and generate a Gemini AI response."""
# # #     try:
# # #         # Fetch news articles
# # #         news_summary = fetch_news(user_input)

# # #         # Provide strict summarization instructions
# # #         model = genai.GenerativeModel("gemini-pro")
# # #         response = model.generate_content(
# # #             f"Summarize the following news strictly without adding extra details:\n\n{news_summary}"
# # #         )

# # #         return f"News Sources:\n{news_summary}\n\nSummary:\n{response.text}"

# # #     except Exception as e:
# # #         return f"An error occurred: {e}"

# # # # Chatbot interaction loop
# # # print("Gemini AI News Chatbot is ready! Type 'exit' to quit.")
# # # while True:
# # #     user_input = input("You: ")
# # #     if user_input.lower() == "exit":
# # #         break
# # #     print("Chatbot:", chatbot(user_input))

# # # import google.generativeai as genai
# # # import requests
# # # import os
# # # from dotenv import load_dotenv

# # # # Load API keys from .env file
# # # load_dotenv()
# # # GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# # # NEWS_API_KEY = os.getenv("NEWS_API_KEY")


# # # genai.configure(api_key=GEMINI_API_KEY)

# # # # Store the latest news data
# # # latest_news = ""  

# # # def fetch_news(query, num_articles=5):
# # #     """Fetches top news articles from News API based on the query."""
# # #     global latest_news  # Store news data for later interactions
# # #     url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"

# # #     try:
# # #         response = requests.get(url)
# # #         response.raise_for_status()
# # #         news_data = response.json()

# # #         if news_data.get("status") != "ok":
# # #             return f"Error fetching news: {news_data.get('message', 'Unknown error')}"

# # #         articles = news_data.get("articles", [])[:num_articles]
# # #         if not articles:
# # #             return "No news articles found."

# # #         # Store news for future questions
# # #         latest_news = "\n".join([f"{i+1}. {a['title']} - {a['source']['name']} (Published: {a['publishedAt']})\n{a['description']}" for i, a in enumerate(articles)])

# # #         return f"News Sources:\n{latest_news}"

# # #     except requests.exceptions.RequestException as e:
# # #         return f"Error: Failed to fetch news due to network issues. {e}"

# # #     except Exception as e:
# # #         return f"Error: {e}"

# # # def ask_about_news(user_input):
# # #     """Allows the user to ask questions based on the fetched news data."""
# # #     global latest_news
# # #     if not latest_news:
# # #         return "No news data available. Please fetch news first."

# # #     try:
# # #         model = genai.GenerativeModel("gemini-pro")
# # #         response = model.generate_content(
# # #             f"Based only on the following news articles, answer the question:\n\n{latest_news}\n\n"
# # #             f"Question: {user_input}\n\n"
# # #             "Only respond with information found in the news articles. If the answer is not in the news, say 'I don't have enough information from the provided news articles.'"
# # #         )

# # #         return response.text

# # #     except Exception as e:
# # #         return f"An error occurred: {e}"

# # # # Chatbot interaction loop
# # # print("Gemini AI News Chatbot is ready! Type 'fetch <topic>' to get news, 'ask <questiowh>' to inquire about it, or 'exit' to quit.")
# # # while True:
# # #     user_input = input("You: ")
# # #     if user_input.lower() == "exit":
# # #         break
# # #     elif user_input.lower().startswith("fetch "):
# # #         topic = user_input[6:].strip()
# # #         print("Fetching news...")
# # #         print("Chatbot:", fetch_news(topic))
# # #     elif user_input.lower().startswith("ask "):
# # #         question = user_input[4:].strip()
# # #         print("Chatbot:", ask_about_news(question))
# # #     else:
# # #         print("Chatbot: Invalid command. Use 'fetch <topic>' or 'ask <question>'.")


# from fastapi import FastAPI, Request
# from fastapi.responses import FileResponse, JSONResponse
# from fastapi.staticfiles import StaticFiles
# import google.generativeai as genai
# import os
# from pydantic import BaseModel
# from dotenv import load_dotenv
# import uvicorn
# # Load API keys from .env file
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# genai.configure(api_key=GEMINI_API_KEY)

# app = FastAPI()

# # Serve static files (Frontend)
# app.mount("/static", StaticFiles(directory="static"), name="static")


# def fetch_news(query, num_articles=5):
#     """Fetches top news articles from News API based on the query."""
#     global latest_news  # Store news data for later interactions
#     url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         news_data = response.json()

#         if news_data.get("status") != "ok":
#             return f"Error fetching news: {news_data.get('message', 'Unknown error')}"

#         articles = news_data.get("articles", [])[:num_articles]
#         if not articles:
#             return "No news articles found."

#         # Store news for future questions
#         latest_news = "\n".join([f"{i+1}. {a['title']} - {a['source']['name']} (Published: {a['publishedAt']})\n{a['description']}" for i, a in enumerate(articles)])

#         return f"News Sources:\n{latest_news}"

#     except requests.exceptions.RequestException as e:
#         return f"Error: Failed to fetch news due to network issues. {e}"

#     except Exception as e:
#         return f"Error: {e}"


# # Store the latest news data
# latest_news = "1. NASA Plans New Moon Mission - CNN (Published: 2025-02-10) NASA is preparing for another Artemis mission to the Moon...2. SpaceX Launches New Satellite - BBC (Published: 2025-02-09)Elon Musk's company successfully deployed new satellites..."  

# class QueryModel(BaseModel):
#     query: str

# @app.get("/")
# async def serve_home():
#     """Serve the frontend HTML page."""
#     return FileResponse("static/index.html")

# @app.post("/ask")
# async def ask_question(request: QueryModel):
#     """Process user questions based on the latest news data."""
    
#     global latest_news
#     if not latest_news:
#         return JSONResponse({"response": "No news data available. Please fetch news first."})

#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(
#             f"Based only on the following news articles, answer the question:\n\n{latest_news}\n\n"
#             f"Question: {request.query}\n\n"
#             "Only respond with information found in the news articles. If the answer is not in the news, say 'I don't have enough information from the provided news articles.'"
#         )

#         return JSONResponse({"response": response.text})

#     except Exception as e:
#         return JSONResponse({"response": f"An error occurred: {e}"})

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)


# # from fastapi import FastAPI, HTTPException
# # from fastapi.responses import JSONResponse
# # from pydantic import BaseModel
# # import google.generativeai as genai
# # import requests
# # import os
# # from dotenv import load_dotenv
# # from fastapi.staticfiles import StaticFiles

# # # Load API keys from .env file
# # load_dotenv()
# # GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# # NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# # # Configure Gemini AI
# # genai.configure(api_key=GEMINI_API_KEY)

# # # FastAPI app instance
# # app = FastAPI()

# # # # Serve static files (Frontend)
# # app.mount("/static", StaticFiles(directory="static"), name="static")


# # # Store the latest news data globally
# # latest_news = ""

# # class NewsQuery(BaseModel):
# #     query: str
# #     num_articles: int = 5

# # class Question(BaseModel):
# #     question: str

# # def fetch_news(query: str, num_articles: int = 5) -> str:
# #     """Fetches top news articles from News API and stores them."""
# #     global latest_news  
# #     url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"

# #     try:
# #         response = requests.get(url)
# #         response.raise_for_status()
# #         news_data = response.json()

# #         if news_data.get("status") != "ok":
# #             return f"Error fetching news: {news_data.get('message', 'Unknown error')}"

# #         articles = news_data.get("articles", [])[:num_articles]
# #         if not articles:
# #             return "No news articles found."

# #         # Store formatted news
# #         latest_news = "\n".join([
# #             f"{i+1}. {a['title']} - {a['source']['name']} (Published: {a['publishedAt']})\n{a['description']}"
# #             for i, a in enumerate(articles)
# #         ])
# #         return latest_news

# #     except requests.exceptions.RequestException as e:
# #         return f"Error: Failed to fetch news due to network issues. {e}"

# # @app.post("/fetch-news")
# # def get_news(news_query: NewsQuery):
# #     """API endpoint to fetch news based on user query."""
# #     news = fetch_news(news_query.query, news_query.num_articles)
# #     if "Error" in news:
# #         raise HTTPException(status_code=500, detail=news)
# #     return JSONResponse(content={"news": news})

# # @app.post("/ask-news")
# # def ask_about_news(question: Question):
# #     """API endpoint to answer questions based on fetched news."""
# #     global latest_news
# #     if not latest_news:
# #         raise HTTPException(status_code=400, detail="No news data available. Please fetch news first.")

# #     try:
# #         model = genai.GenerativeModel("gemini-pro")
# #         response = model.generate_content(
# #             f"Based only on the following news articles, answer the question:\n\n{latest_news}\n\n"
# #             f"Question: {question.question}\n\n"
# #             "Only respond with information found in the news articles. If the answer is not in the news, say 'I don't have enough information from the provided news articles.'"
# #         )

# #         return JSONResponse(content={"answer": response.text})

# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="127.0.0.1", port=8000)

import google.generativeai as genai
import requests
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


genai.configure(api_key=GEMINI_API_KEY)

# Store the latest news data
latest_news = ""  

def fetch_news(query, num_articles=5):
    """Fetches top news articles from News API based on the query."""
    global latest_news  # Store news data for later interactions
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        news_data = response.json()

        if news_data.get("status") != "ok":
            return f"Error fetching news: {news_data.get('message', 'Unknown error')}"

        articles = news_data.get("articles", [])[:num_articles]
        if not articles:
            return "No news articles found."

        # Store news for future questions
        latest_news = "\n".join([f"{i+1}. {a['title']} - {a['source']['name']} (Published: {a['publishedAt']})\n{a['description']}" for i, a in enumerate(articles)])

        return f"News Sources:\n{latest_news}"

    except requests.exceptions.RequestException as e:
        return f"Error: Failed to fetch news due to network issues. {e}"

    except Exception as e:
        return f"Error: {e}"

def ask_about_news(user_input):
    """Allows the user to ask questions based on the fetched news data."""
    global latest_news
    if not latest_news:
        return "No news data available. Please fetch news first."

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            f"Based only on the following news articles, answer the question:\n\n{latest_news}\n\n"
            f"Question: {user_input}\n\n"
            "Only respond with information found in the news articles. If the answer is not in the news, say 'I don't have enough information from the provided news articles.'"
        )

        return response.text

    except Exception as e:
        return f"An error occurred: {e}"

# Chatbot interaction loop
print("Gemini AI News Chatbot is ready! Type 'fetch <topic>' to get news, 'ask <questiowh>' to inquire about it, or 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower().startswith("fetch "):
        topic = user_input[6:].strip()
        print("Fetching news...")
        print("Chatbot:", fetch_news(topic))
    elif user_input.lower().startswith("ask "):
        question = user_input[4:].strip()
        print("Chatbot:", ask_about_news(question))
    else:
        print("Chatbot: Invalid command. Use 'fetch <topic>' or 'ask <question>'.")
