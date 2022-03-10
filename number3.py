import requests
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
import telegram

url = 'https://vc.ru'
r = requests.get(url)
with open('test.html', 'w', encoding="utf-8") as output_file:
  output_file.write(r.text)

with open("test.html", 'r',  encoding="utf-8") as f:
  text=f.read()
print(text)
#lxml который не работет
'''
t = html.fromstring(text)
novosti = t.xpath('//div[@class = "news_widget__content__inner"]')[0]
item_novosti= novosti.xpath('//div[@class = "l-inline"]')
for i in item_novosti:
  link = i.xpath('.//a[@data-gtm = "Popular Feed — News Widget — 1 — Click"]/a/@href')
  desc = i.xpath('.//a[@data-gtm = "Popular Feed — News Widget — 1 — Click"]/a/text()')

print(link)
print(desc)

'''
#soup

soup = BeautifulSoup(text, features="lxml")

novost=soup.find('a', {'data-gtm': 'Popular Feed — News Widget — 1 — Click'})
print(novost)
link = soup.find('a', {'data-gtm': 'Popular Feed — News Widget — 1 — Click'}).get('href')
desc=soup.find('a', {'data-gtm': 'Popular Feed — News Widget — 1 — Click'}).text
print(link)
print(desc)

#telegram

bot = telegram.Bot(token='123456789:AABBCCDDefgh_mnaviwuue_DP865Y')

bot.send_message(chat_id='@here_some_channel_to_post', text=desc+'\n'+link)