import random
import time
#import nltk
import requests
from bs4 import BeautifulSoup

def scrape_and_parse(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')

    headLine = soup.find('h1').text.strip()
    # get text
    text = soup.find('div', attrs={'itemprop': 'articleBody'})
    text = text.find_all('p')

    sentences = list()

    for paragraph in text:
        tempList = list(paragraph.text.split(". "))
        for sentence in tempList:
            if(sentence != ''):
                sentences.append(sentence)

    print_content(headLine, sentences)

def print_content(headLine, sentences):
    print("Headline -> " + headLine)
    #for i in sentences:
    #    print(i)
    print(sentences[random.randint(0, len(sentences))])

url = "https://www.delfi.lt/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a', {"class":"CBarticleTitle"})

for link in links:
    scrape_and_parse(link['href'])
    time.sleep(1)
