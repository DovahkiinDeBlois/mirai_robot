import requests

'''
先将bv号转成av号
然后请求第一个网址并设定参数aid为av号
如果该av号存在，则message为0，且在该数据的data.pic找到图片地址
如果不存在，则message为'稿件不可见'
'''


# 设定一些用来准备转化的av号，原理不明，来自https://www.zhihu.com/question/381784377/answer/1099438784
def b_a(x):
    def dec(x):
        r = 0
        for i in range(6):
            r += tr[x[s[i]]] * 58 ** i
        return (r - add) ^ xor


    def enc(x):
        x = (x ^ xor) + add
        r = list('BV1  4 1 7  ')
        for i in range(6):
            r[s[i]] = table[x // 58 ** i % 58]
        return ''.join(r)


    table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
    tr = {}
    for i in range(58):
        tr[table[i]] = i
    s = [11, 10, 3, 8, 4, 6]
    xor = 177451812
    add = 8728348608

    if isinstance(x, int):
        return enc(x)
    elif isinstance(x, str) and x[0:2].lower() == 'bv':
        return dec(x)
    elif isinstance(x, str) and x[0:2].lower() == 'av':
        return enc(eval(x[2:]))
    elif x.isnumeric():
        return enc(eval(x))


# 根据av号来返回一个url
def get_url(av):
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
        'Referer': 'https://www.bilibili.com'}
    url = f'https://api.bilibili.com/x/web-interface/view?aid={av}'


    try:
        video_data_json = requests.get(url=url, headers=headers, proxies=proxies)
    except:
        return '哼，都是网络的原因啦，才不是怪我了！'
    print(av)

    if video_data_json.json()['message'] != '0':
        return '可恶，没找到！是不是你写错了啊？'

    else:
        print(video_data_json.json())
        return video_data_json.json()['data']['pic']


if __name__ == '__main__':
    # print(get_url(41949084))
    bv='BV1xb411C7KW'
    print(get_url(b_a(bv)))
