import requests
import re
import random
import base64


def gp():
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    url_main = 'https://w.wallhaven.cc/'

    url = 'https://wallhaven.cc/search?q=id%3A1&sorting=random&ref=fp&seed=RUPUc7&page=1'
    try:
        soup = requests.get(url, headers=header, proxies=proxies)
        soup = soup.text
    except:
        print(soup)
    print(111)

    rep = re.compile('href="https://wallhaven.cc/w/.*?"')
    pic_url = rep.findall(soup)
    i = len(pic_url)
    random_url = pic_url[random.randint(0, i-1)]
    pic_url = url_main+'full/'+random_url[29:31]+'/wallhaven-'+random_url[29:-1]

    photo = requests.get(pic_url + '.jpg', headers=header, proxies=proxies)
    a = pic_url+'.jpg'
    if photo.status_code == 404:
        a = pic_url + '.png'
        photo = requests.get(pic_url + '.png', headers=header, proxies=proxies)

    # if photo.status_code == 404:
    #     print(a)
    print(photo)
    return base64.b64encode(photo.content).decode()





if __name__ == '__main__':
    gp()
