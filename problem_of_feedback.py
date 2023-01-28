import time
import json


def problem_record(name, text):
    matter = {
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()):
            [name, text]
    }

    file = open('E:\\work\\python\\mirai\\机器人代码\\problem_gather.json', 'r+', encoding='utf-8')

    title = json.load(file)
    print(matter)
    matter.update(title)
    file.seek(0)
    file.write(json.dumps(matter))
    file.close()


if __name__ == '__main__':
    problem_record('test', 'testtest')
