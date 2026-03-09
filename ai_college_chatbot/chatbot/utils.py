import ollama
from .web_scraper import extract_website_text

def get_ai_answer(question):
    url="https://www.einsteincollege.ac.in/"
    website_data=extract_website_text(url)
    prompt=f"""
You are a college assistant chatbot.
Use the college website information below to answer student questions.
College Information:
{website_data}

Student Questions:
{question}

Give a clear answer.

"""
    response=ollama.chat(
        model="phi3",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    answer=response["message"]["content"]

    return answer