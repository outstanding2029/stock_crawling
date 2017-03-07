import datetime
import requests
import time
from lxml import html

keyword_list = ['투자']
target_url = 'http://finance.naver.com/item/news_news.nhn?code=%s&page='

def AnalyzePage(code):
    if code is None:
        return
        
    page = requests.get(target_url % code)
    tree = html.fromstring(page.text);
    d = datetime.date.today()

    date_text = ''
    title_text = ''
    for i in range(3, 8):
        try:
            date_text = tree.xpath('/html/body/table[1]/tr[%d]/td[1]/span/text()' % i)[0]
            title_text = tree.xpath('/html/body/table[1]/tr[%d]/td[2]/a/text()' % i)[0]
        except:
            print('Error : ' + code)
            return

    date = date_text.split(' ')[0].split('.')
    if int(date[0]) == d.year and int(date[1]) == d.month and int(date[2]) == d.day:
        for keyword in keyword_list:
            idx = title_text.find(keyword)
            if idx != -1:
                print(code + ' : ' + title_text)

in_file = open('code.txt', 'r')
lines = in_file.read().split('\n')
for line in lines:
    AnalyzePage(line)
in_file.close()
