import requests
from bs4 import BeautifulSoup

def extract_links_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def extract_main_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        soup = BeautifulSoup(response.content, 'lxml')
        # Here you can add logic to extract the main content
        # For example, if the main content is in a specific tag
        main_content = soup.find('main')  # This is just an example
        return main_content.text if main_content else None
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_headline(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # Attempt to find the headline in an <h1> tag or <title> tag
        headline = soup.find('h1') or soup.find('title')
        return headline.text.strip() if headline else None
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def main():
    file_path = 'hrefs.txt'  # Replace with your file path
    urls = extract_links_from_file(file_path)

    for url in urls:
        # content = extract_main_content(url)
        # if content:
        #     print(f"Content from {url}:\n{content}\n")

        headline = extract_headline(url)
        if headline:
            print(f"Headline from {url}:\n{headline}\n")

if __name__ == '__main__':
    main()
