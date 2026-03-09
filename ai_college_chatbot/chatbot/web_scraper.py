import requests
from bs4 import BeautifulSoup
 
def extract_website_text(url):
    try:
        response=requests.get(url)
        soup=BeautifulSoup(response.text,"html.parser")
        paragraphs=soup.find_all("p")
        content=""

        for p in paragraphs:
            content +=p.get_text()+"\n"
        return content[:4000]
    
    except Exception as e:
        return str(e)