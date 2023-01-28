import random
import requests
from bs4 import BeautifulSoup
import base64
import re


def get_anime():
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}

    url_main = 'http://bangumi.tv/'
    url_suffix_page = '/anime/browser?sort=rank&page='
    page = 1
    url_suffix_anime = '/subject/'

    rep = re.compile('&nbsp;1&nbsp;/&nbsp;([0-9]*?)&nbsp;')
    page_max = []
    while len(page_max) == 0:
        soup = requests.get(
            url_main+url_suffix_page+str(page),
            headers=header,
            proxies=proxies
        )
        soup.close()

        soup = soup.text

        page_max = rep.findall(soup)
    # print(page_max)
    page_max = int(page_max[0])

    page_max = page_max//5

    page = random.randint(1, page_max)
    anime_num = []

    while len(anime_num) < 3:
        soup = requests.get(
            url_main + url_suffix_page + str(page),
            headers=header,
            proxies=proxies
        )
        soup.close()
        soup = soup.text

        # print(soup)

        rep = re.compile('<a href="/subject/(\d*?)" class="l">')
        anime_num = rep.findall(soup)
    # print(anime_num)

    random_num = str(random.choice(anime_num))
    print(random_num)
    # random_num = str(221227)
    # random_num = str(490)
    # random_num = str(14877)
    # random_num = str(254895)
    # random_num = str(72266)
    # random_num = str(322967)
    # random_num = str(2215)
    # random_num = str(206925)


    jp_name = []
    while len(jp_name) == 0:
        soup = requests.get(
            url_main+url_suffix_anime+random_num,
            headers=header,
            proxies=proxies
        )
        soup.close()
        soup = soup.content.decode('utf-8')
        # print(soup)

        # 获取原始名字
        rep = re.compile('<title>(.+?) | Bangumi')
        jp_name = rep.findall(soup)
    # 获取中文名字
    rep = re.compile('中文名: </span>(.*?)</li>')
    cn_name = rep.findall(soup)
    # 获取话数
    rep = re.compile('话数: </span>(\d*?)</li>')
    blues = rep.findall(soup)
    # 放送时间
    rep = re.compile('放送开始: </span>(.*?)</li>')
    date = rep.findall(soup)
    if len(date) == 0:
        rep = re.compile('上映年度: </span>(.*?)</li>')
        date = rep.findall(soup)

    # 获取评分
    rep = re.compile('rage">(.*?)<')
    number = rep.findall(soup)

    # 获取简介
    # rep = re.compile(u':summary">(.*)<')
    # introduce = rep.findall(soup)
    bssoup = BeautifulSoup(soup, "html.parser")
    introduce = bssoup.find(id='subject_summary')
    # print(introduce)
    if introduce:
        introduce = introduce.get_text()
    # 获得图片
    url_img = bssoup.find('img', class_='cover')
    # print(url_img)
    if url_img:
        # print(url_img['src'])
        url_img = 'http:'+url_img['src']
        # print(url_img)
        img = requests.get(url_img, headers=header, proxies=proxies)
        img.close()
        print('get')
    else:
        img = 0
        print('noget')

    # print(jp_name, cn_name, blues, number, date)
    # print(introduce)
    # print(type(introduce))

    discourse = '番名：'+jp_name[0]

    if cn_name:
        discourse += '\n中文名：'+cn_name[0]
    if blues:
        discourse += '\n共计%d集' % int(blues[0])
    if number:
        discourse += '\n评分：' + number[0]
    if date:
        discourse += '\n放送时间：' + date[0]
    if introduce:
        discourse += '\n简介：\n' + introduce

    print(discourse)
    try:
        if img.status_code == 200:
            return discourse, base64.b64encode(img.content).decode()
        # return discourse, url_img
        else:
            return discourse, 0
    except AttributeError:
        return discourse, 0


if __name__ == '__main__':
    get_anime()

