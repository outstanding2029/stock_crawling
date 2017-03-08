import datetime
import requests
import time
from lxml import html

import db_api
import mail_api
import rest_api

TARGET_URL = 'http://finance.naver.com/item/news_news.nhn?code=%s&page='
STOCK_URL = 'http://finance.naver.com/item/news.nhn?code=%s'

CODE_FILE_NAME = 'code.txt'

KEYWORD_LIST = ['투자', '억 규모', '억원 규모']
REPLACE_LIST = ['성공투자', '투자증권', '투자권유', '투자의견', '투자자', 'NH투자', '투자 배급', '투자 세미나']

def analyze_page(code):
    if code is None:
        return None

    page = requests.get(TARGET_URL % code)
    tree = html.fromstring(page.text);
    d = datetime.date.today()
    for i in range(3, 8):
        try:
            date_text = tree.xpath('/html/body/table[1]/tr[%d]/td[1]/span/text()' % i)[0]
            title_text = tree.xpath('/html/body/table[1]/tr[%d]/td[2]/a/text()' % i)[0]
        except:
            return None

        date = date_text.split(' ')[0].split('.')
        if int(date[0]) == d.year and int(date[1]) == d.month and int(date[2]) == d.day:
            for target in REPLACE_LIST:
                title_text = title_text.replace(target, '')

            for keyword in KEYWORD_LIST:
                idx = title_text.find(keyword)
                if idx != -1 and db_api.is_exist(code) == None:
                    db_api.insert(code, title_text)
                    return title_text
    return None

def analyze():
    in_file = open(CODE_FILE_NAME, 'r')
    lines = in_file.read().split('\n')
    message = ''
    for line in lines:
        result = analyze_page(line)
        if result is not None:
            message = message + line + ' : ' + result + ' / ' + STOCK_URL % line + '\n'
    in_file.close()
    return message

while True:
    message = analyze()
    if len(message) != 0:
        mail_api.send_mail('stock', message)
