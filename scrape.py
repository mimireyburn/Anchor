import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import json
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI'))

def askGPT(links):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": "Review the following list of links or url extensions and identify specific strings that are likely to indicate non-article pages. Look for patterns or keywords that suggest the link is to a help page, user profile, administrative or organizational content, or other non-article pages. Exclude strings that represent broad article categories or general topics to ensure we don't accidentally filter out actual articles. The goal is to remove only those links that are definitively not articles, such as links to about pages, user accounts, settings, or corporate information. Here are some of the links:" + str(links[:100]) + "\n\n Always respond in the following format: ['string1', 'string2', 'string3'] \n\n" 
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    return response.choices[0].message.content


def makeSoup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def getHrefs(url):
    soup = makeSoup(url)
    # find all links on page 
    hrefs = [link.get('href') for link in soup.find_all('a')]
    # remove duplicates
    print(len(hrefs))
    hrefs = list(dict.fromkeys(hrefs))
    # remove empty links
    hrefs = [href for href in hrefs if href is not None]
    # remove links that start with #
    print(len(hrefs))
    hrefs = [href for href in hrefs if not href.startswith('#')]
    # remove links that only have one / 
    hrefs = [href for href in hrefs if href.count('/') > 2 ]
    print(len(hrefs))
    # remove links that don't start with base url or /
    if 'ycombinator' not in url:
        hrefs = [href for href in hrefs if href.startswith('http') or href.startswith('/')]

    print(len(hrefs))

    return hrefs


urls = ['https://www.theguardian.com', 'https://www.bbc.co.uk/news', 'https://www.theverge.com', 'https://news.ycombinator.com', 'https://www.technologyreview.com']

with open('hrefs.txt', 'w') as file:
            
    for url in urls:
        print(url)
        hrefs = getHrefs(url)
        for href in hrefs:
                if not href.startswith('http'):
                    file.write(url + href + '\n')
                else:
                    file.write(href + '\n')

file.close()