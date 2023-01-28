import re
import requests
import datetime
import unvcode
from bs4 import BeautifulSoup


def get_everday60():
    """
    这个函数是用来从知乎上获取每日六十秒的数据，
    先进入他所写的公众内容内，然后找寻今天的数据。
    如果今天的数据没到，返回一个空。
    :return:以元组的列表的形式返回图片地址以及文字内容,
    如果出现问题返回[(-1, str:问题原因)]
    正常[('img', str:url地址)…… ('text', str:文字内容)……]
    """
    # 文章集合地址
    # first_url = 'https://www.zhihu.com/column/c_1261258401923026944'
    # first_url = 'https://www.zhihu.com/api/v4/columns/c_1261258401923026944/items?limit=10&offset=0'
    first_url = 'https://www.zhihu.com/api/v4/columns/c_1261258401923026944/items'

    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
        'Referer': 'https://www.bilibili.com'}

    # 获取现在时间
    now = datetime.date.today()
    rep_get_url = re.compile('"excerpt":(.*?)"url": "(.*?)", "')

    data_now = requests.get(first_url, proxies=proxies, headers=headers)
    today_url = rep_get_url.findall(data_now.text.encode("utf-8").decode("unicode_escape"))

    data_now.close()
    second_url = None
    for i in today_url:
        if str(now.month) + '月' + str(now.day) + '日' in i[0]:
            second_url = i[1]
            break
    if second_url is None:
        return [-1, '今日新闻还未出现，请尽情等待']

    second_reqdata = requests.get(second_url, proxies=proxies, headers=headers)
    second_reqdata.close()
    soup_get_data = BeautifulSoup(second_reqdata.text, 'html.parser')

    rep_get_tag = re.compile('(RichText ztext Post-RichText.*?)"')
    find_tag_class_names = rep_get_tag.findall(second_reqdata.text)[0]
    print(find_tag_class_names)

    soup_get_data = soup_get_data.find(class_=find_tag_class_names)
    datalist = []
    # print(soup_get_data)
    for soup in soup_get_data:
        # print('\n********************')
        # print(soup)
        # print('********************\n')
        if soup.name == 'figure':
            datalist.append(('img', soup.img.get('src')))
            print(soup.img.get('src'))
        elif soup.name == 'p':
            # print(unvcode(soup.text)[0])
            print(type(soup.text))
            if soup.text == '':
                continue
            s, var = unvcode.unvcode(soup.text)
            print(s)
            datalist.append(('text', s + '\n'))
            # print(soup.text)
        elif soup.name == 'a':
            # print(soup.attrs['class'])
            if soup.attrs['class'][0] == 'video-box':
                # print('对的')
                datalist.append(('img', soup.get('data-poster')))
                datalist.append(('text', '视频地址:' + soup.get('href') + '\n'))
    print(datalist)

    return datalist




if __name__ == '__main__':
    message_list = get_everday60()

