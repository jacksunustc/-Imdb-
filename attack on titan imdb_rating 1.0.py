import requests
from bs4 import BeautifulSoup
from baitrans import *
import time
url = 'https://www.imdb.com/title/tt2560140/episodes?ref_=tt_ov_epl'
while True:
    try:
        req = requests.get(url)
    except Exception:
        print("访问失败,正在尝试继续访问")
        continue
    else:
        print("巨人最终季Imdb评分-------------")
        print("标题，评分，评分人数")
        html = BeautifulSoup(req.text, 'html.parser')
        root = html.find(class_="list detail eplist")
        texts = root.contents
        for enter_ in texts:
            if enter_ == '\n':
                texts.remove('\n')

        class show():
            name = []
            rate = []
            rate_number = []
            contents = []

        Aot = show()

        def change_show(show,
                        name,
                        rate='None',
                        rate_number='None',
                        contents='None'):
            show.name.append(name)
            show.rate.append(rate)
            show.rate_number.append(rate_number)
            show.contents.append(contents)

        for epis, index in zip(texts, range(0, len(texts))):
            list_ = list(epis.stripped_strings)
            if list_[-1] == "Be the first one to add a plot.":
                if len(list_) == 6:
                    change_show(Aot, list_[3])
                else:
                    change_show(Aot, list_[2])
            elif len(list_) == 4 or list_[4] == 'Rate':
                change_show(Aot, list_[2], contents=list_[-1])
            else:
                change_show(Aot, list_[2], list_[3], list_[4], list_[-1])
        for index_,n, r, r_n, c in zip(range(1,len(texts)+1),Aot.name, Aot.rate, Aot.rate_number,
                                Aot.contents):
            print(index_,':'+n + ',' + r + ',' + r_n)
        break
input()