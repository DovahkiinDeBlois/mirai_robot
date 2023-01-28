import requests
import re
import random
import base64


def gp():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    url_main = 'https://w.wallhaven.cc/'

    url = 'https://wallhaven.cc/search?q=id%3A1&sorting=random&ref=fp&seed=RUPUc7&page=1'

    soup = requests.get(url, headers=header)
    soup = soup.text

    rep = re.compile('href="https://wallhaven.cc/w/.*?"')
    pic_url = rep.findall(soup)
    i = len(pic_url)
    random_url = pic_url[random.randint(0, i-1)]
    pic_url = url_main+'full/'+random_url[29:31]+'/wallhaven-'+random_url[29:-1]
    try:
        photo = requests.get(pic_url + '.jpg', headers=header)
    except:
        photo = requests.get(pic_url + '.png', headers=header)
    print(photo)
    return base64.b64encode(photo.content).decode()





if __name__ == '__main__':
    gp()
