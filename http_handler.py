import random

import requests
from lxml import etree


def analysis_html(html):
    print(html)
    tree = etree.HTML(html)
    book_list = tree.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]')
    print(book_list)
    for book in book_list[3:13]:
        book_url = book.xpath("./div/a/@href")
        book_img = book.xpath("./div/a/img/@href")
        book_title = book.xpath("./div/a/img/@alt")
        book_rate = book.xpath("./div/div[2]/span[2]/text()")
        book_comment_num = book.xpath("./div/div[2]/span[3]/text()")
        book_author = book.xpath("./div/div[3]/text()")
        print(book_url,book_img,book_title,book_rate,book_comment_num,book_author)

class HTTP:
    ua_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"]
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "cookie":'bid=S22rJHZu_W8; ap_v=0,6.0; gr_user_id=7e9f3ba8-2cf9-43e9-a9e8-093155f8dc04; __utmc=30149280; __utma=30149280.1758892664.1659206482.1659206482.1659206482.1; __utmz=30149280.1659206482.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=8edc1ea821622317-22189f1c98d40093:T=1659207217:RT=1659207217:S=ALNI_MYwoBhKbx-O0h6y-6REJj0nCLRnJQ; __gpi=UID=0000082277dc13f0:T=1659207217:RT=1659207217:S=ALNI_MYwNvbn0ESo748Wew7vR223LZwfOQ; _ga=GA1.1.1758892664.1659206482; _ga_RXNMP372GL=GS1.1.1659207304.1.0.1659207305.59; gr_cs1_746d9fce-2b33-4354-97eb-671191d19a8b=user_id%3A0; viewed="35720728_35144587_35635836_27015617_26859123_5063808_26911464"; __utmb=30149280.34.10.1659206482'
    }
    @classmethod
    def get(cls,url, return_json=True):
        cls.headers['Referer'] = url
        r = requests.get(url,headers=cls.headers)
        print(r.text)
        if r.status_code != 200:
            return {} if return_json else ''
        analysis_html(r.text)
        return {"r.json()":"ok"} if return_json else r.text
