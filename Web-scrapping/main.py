import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
url = "https://habr.com/ru/articles/"

headers = Headers(browser="chrome", os="win", headers=True)

def statii_habr():
    response = requests.get(url, headers=headers.generate())
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article', class_='tm-articles-list__item')

    for article in articles:
        date_tag = article.find('time')
        pub_date = date_tag['datetime'][:10] if date_tag else 'Дата не найдена'

        title_tag = article.find('h2')
        title = title_tag.get_text(strip=True) if title_tag else 'Без заголовка'

        # Ссылка на статью
        link_tag = title_tag.find('a') if title_tag else None
        link = 'https://habr.com'  + link_tag['href'] if link_tag and 'href' in link_tag.attrs else ''

        preview_tag = article.find('div', class_='article-formatted-body')
        preview_text = preview_tag.get_text(strip=True).lower() if preview_tag else ''

        full_text = (title + ' ' + preview_text).lower()

        if any(keyword in full_text for keyword in KEYWORDS):
            print(f"{pub_date} – {title} – {link}")

if __name__ == '__main__':
    statii_habr()