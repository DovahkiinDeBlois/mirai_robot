import os
import json
import random


def get_title():

    file = open('E:\\work\\python\\mirai\\机器人代码\\title.json', 'r+')

    title = json.load(file)
    # print(type(title))
    title = dict(title)
    keys = list(title.keys())
    key = str(random.choice(keys))
    # print(key, '\n', title[key])

    file.close()
    return key, title[key]


if __name__ == '__main__':
    print(get_title())
