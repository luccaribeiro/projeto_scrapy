import requests
from lxml import html

url = 'https://news.ycombinator.com/'
response = requests.get(url)

tree = html.fromstring(response.content)

titulos = tree.xpath('//tr[@class="athing"]//td[@class="title"]//span[@class="titleline"]/a/text()')

# Exibindo os títulos extraídos
for titulo in titulos:
    print(titulo)