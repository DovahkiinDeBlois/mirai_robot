import random

def get_draw():
    a = [
        '下下签'
        ,'下签'
        ,'中签'
        ,'上签'
        ,'上上签'
    ]
    return random.choice(a)

if __name__ == '__main__':
    get_draw()
