import random
import time


def get_horo(numb):
    date = eval(time.strftime('%Y%m%d', time.localtime()))

    random.seed(numb+date)
    horo = random.random()
    print("horo%.4f" % horo)
    h = time.strftime('%H', time.localtime())
    if h[0] == '0':
        h = h[1]
    h = eval(h)
    if h < 3 or h > 19:
        Period_of_time = 1
    elif 3 <= h < 7:
        Period_of_time = 2
    elif 7 <= h < 17:
        Period_of_time = 3
    elif 17 <= h <= 19:
        Period_of_time = 4

    if horo <= 0.1:
        return Period_of_time, '大凶'
    elif horo <= 0.35:
        return Period_of_time, '凶'
    elif horo <= 0.65:
        return Period_of_time, '中'
    elif horo <= 0.9:
        return Period_of_time, '吉'
    else:
        return Period_of_time, '大吉'


if __name__ == '__main__':
    get_horo(1411905376)
