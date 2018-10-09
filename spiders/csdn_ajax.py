import requests


def get_page():
    headers = {'cookie':'',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    url = 'https://www.csdn.net/api/articles?type=more&category=home&shown_offset=0'
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            html = r.json()
            articles = html['articles']
            if len(articles) == 0:
                print(url)
            return r.json()
        return None
    except ConnectionError:
        return None


def pares_page(html):
    articles = html['articles']
    print(len(articles))
    for article in articles:
        yield article['title']


def main():
    for i in range(20):
        html = get_page()
        yield from pares_page(html)

if __name__ == '__main__':
    l = list(main())
    print(len(l))