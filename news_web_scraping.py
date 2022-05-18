import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
html_parse = BeautifulSoup(res.text, 'html.parser')
links = html_parse.select('.titlelink')
subtext = html_parse.select('.subtext')


def sort_by_votes(hacker_news):
    return sorted(hacker_news, key=lambda x: x['votes'], reverse=True)


def create_custom_hacker_news(links, subtext, pages=1):
    hacker_news = []
    page = 1
    while page <= pages:
        for index, item in enumerate(links):
            title = item.getText()
            href = item.get('href', None)
            vote = subtext[index].select('.score')
            if len(vote):
                score = int(vote[0].getText().replace(' points', ''))
                if score >= 100:
                    hacker_news.append({'title': title, 'link': href, 'votes': score})
        page += 1
        res = requests.get(f'https://news.ycombinator.com/news?p={page}')
        html_parse = BeautifulSoup(res.text, 'html.parser')
        links = html_parse.select('.titlelink')
        subtext = html_parse.select('.subtext')
    return sort_by_votes(hacker_news)


pprint.pprint(create_custom_hacker_news(links, subtext, 3))
