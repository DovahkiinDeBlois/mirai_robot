from mirai import Mirai, WebSocketAdapter, \
    FriendMessage, Plain, \
    GroupMessage, Image, \
    Startup, Shutdown
from mirai import At

from mirai.models import NewFriendRequestEvent
from mirai.models.api import RespOperate

import os
import time
import random
import threading
import datetime
import asyncio
from datetime import datetime
from functools import partial

# 自写
import get_photo
import anime_recommend
import read_json
import random_draw
import image_operation
import horoscope
import problem_of_feedback
import get_bili_pic
import undercover_thesaurus
import everday60

global cause
records_time_sleep = 0
records_time_oha = 0

guess = 0
bot = Mirai(
    qq=3531733375,  # 改成你的机器人的 QQ 号
    adapter=WebSocketAdapter(
        verify_key='INITKEYtGhesePs', host='localhost', port=8090
    )
)


def time_out(r_time, n_time, out=120) -> bool:
    """
    :param r_time:  记录的时间
    :param n_time:   现在的时间
    :param out: 需要超过的时间
    :return:    bool值，如果超过了时间，就返回True，反之返回False
    """
    print("超出随机时间为", out)
    return n_time - r_time >= out


@bot.on(FriendMessage)
async def on_friend_message(event: FriendMessage):
    # print(event)
    if '指令' in str(event.message_chain):
        await bot.send(event, [Plain('123')])
    elif '搞点二次元' in str(event.message_chain) or '搞点二刺螈' in str(event.message_chain):
        await bot.send(event, [Plain('唉，我嘛？')])
        time.sleep(random.random())
        await bot.send(event, [Plain('你等一下咯~')])
        time.sleep(random.random())
        try:
            img = get_photo.gp()
            await bot.send(event, [Image(base64=img)])
        except:
            return bot.send(event, [Plain('没办法，就算是天才如我也会有被网络制裁的一天，绝对不是我没找到哦')])
    elif '抽签' in str(event.message_chain):
        time.sleep(random.random())
        return bot.send(event, [Plain('是吗？又想抽签了吗，好好好，让我看看你此刻的运势是:' + random_draw.get_draw())])
    elif '你' in str(event.message_chain) and '谁' in str(event.message_chain):
        await bot.send(event, [Image(path='./Image/To_introduce_myself.jpg')])
        time.sleep(random.random())
        return bot.send(event, [Plain('初次见面，我是游行寺夜子，你可以叫我夜子，也可以叫我夜子酱，不对，夜子酱只有清良能叫，先说好，我最讨厌的就是清良，以上。')])
    elif event.message_chain.has('wifu2x'):
        i = 0
        images = event.message_chain[Image]
        for image in images:
            i += 1
            if i > 1:
                return bot.send(event, [Plain('不要发那么多图片啦~')])
            await image.download(filename='./Image/wifu2x.jpg')
        time.sleep(random.random())
        await bot.send(event, [Plain('哼，得不到你的夸奖也无所谓啦！！！')])
        time.sleep(random.random())
        await image_operation.twico_over()
        time.sleep(random.random())
        return bot.send(event, [Image(path='./Image/wifu2x.jpg')])

    elif event.message_chain.has('线稿化'):
        print('开始线稿化')
        if event.message_chain.has('线稿化2'):
            print('线稿化2')
            i = 0
            images = event.message_chain[Image]
            for image in images:
                i += 1
                if i > 1:
                    return bot.send(event, [Plain('不要发那么多图片啦~')])
                await image.download(filename='./Image/edge.jpg')
            time.sleep(random.random())
            await bot.send(event, [Plain('哼，得不到你的夸奖也无所谓啦！！！')])
            time.sleep(random.random())

            await image_operation.edge_get_2()
            time.sleep(random.random())
            return bot.send(event, [Image(path='./Image/edge.jpg')])
        else:
            print('线稿化')
            i = 0
            images = event.message_chain[Image]
            for image in images:
                i += 1
                if i > 1:
                    return bot.send(event, [Plain('不要发那么多图片啦~')])
                await image.download(filename='./Image/edge.jpg')
            time.sleep(random.random())
            await bot.send(event, [Plain('哼，得不到你的夸奖也无所谓啦！！！')])
            time.sleep(random.random())

            await image_operation.edge_get()
            time.sleep(random.random())
            return bot.send(event, [Image(path='./Image/edge.jpg')])
    elif event.message_chain.has('问题反馈'):
        problem_of_feedback.problem_record(event.sender.nickname, str(event.message_chain))

    else:
        time.sleep(random.random())
        return bot.send(event, '嗯？怎么了？又要我帮你了吗？哼╯^╰，我就知道你离不开我')

    if '你好' in str(event.message_chain):
        return bot.send_friend_message(event.sender.id, [Plain('嘿嘿嘿')])
    elif '初次见面' in str(event.message_chain):
        return bot.send_friend_message(event.sender.id, [Plain('嘻嘻，第一次见面你好啊')])


@bot.on(GroupMessage)
async def on_group_message(event: GroupMessage):
    global guess, cause

    # print(event.message_chain)
    # print(event.sender.id)
    if (At(bot.qq) in event.message_chain or event.message_chain.has('椰子酱') or event.message_chain.has('夜子') or \
        event.message_chain.has('鱼子酱') or event.message_chain.has('叶子') or event.message_chain.has('yezi')) and \
            not event.message_chain.has('//##'):
        print(datetime.now(), "\033[1;31;46m" + event.group.name + "\033[0m",
              "\033[1;32;47m" + event.sender.member_name + "\033[0m")
        print("\033[1;31;45m" + str(event.message_chain) + "\033[0m")
        if (event.message_chain.has('搞点') or event.message_chain.has('整点') or event.message_chain.has('弄点')
            or event.message_chain.has('弄点')) \
                and (event.message_chain.has('二刺螈') or event.message_chain.has('二次元')
                     or event.message_chain.has('色图') or event.message_chain.has('涩图')):
            await bot.send(event, [Plain('唉，我嘛？')])
            await bot.send(event, [Plain('你等一下咯~')])
            try:
                m_time = time.time()
                img = get_photo.gp()
                print("\033[4;37;44m用时:%0.2f秒\033[0m" % (time.time() - m_time))
                await bot.send(event, [Image(base64=img)])
            except:
                return bot.send(event, [Plain('没办法，就算是天才如我也会有被网络制裁的一天，绝对不是我没找到哦')])
        elif '抽签' in str(event.message_chain):
            return bot.send(event, [Plain('是吗？又想抽签了吗，好好好，让我看看你此刻的运势是:' + random_draw.get_draw())])
        elif '你' in str(event.message_chain) and '谁' in str(event.message_chain):
            await bot.send(event, [Image(path='./Image/To_introduce_myself.jpg')])
            return bot.send(event, [Plain('初次见面，我是游行寺夜子，你可以叫我夜子，也可以叫我夜子酱，不对，夜子酱只有清良能叫，先说好，我最讨厌的就是清良，以上。')])
        elif event.message_chain.has('waifu2x'):
            images = event.message_chain[Image]
            if len(images) == 0:
                return bot.send(event, [Plain('笨蛋！你不给我图我要怎样做啦！')])
            await bot.send(event, [Plain('哼，得不到你的夸奖也无所谓啦！！！')])
            for image in images:
                await image.download(filename='./Image/wifu2x.jpeg', determine_type=False)
                m_time = time.time()
                img = image_operation.twico_over()
                print("\033[4;37;44m用时:%0.2f秒\033[0m" % (time.time() - m_time))
                print(type(img))
                await bot.send(event, [Image(path='./Image/wifu2x.jpg')])
            return
        elif event.message_chain.has('线稿化'):
            print('开始线稿化')
            if event.message_chain.has('线稿化2'):
                print('线稿化2')
                i = 0
                await bot.send(event, [Plain('哼，得不到你的夸奖也无所谓啦！！！')])

                images = event.message_chain[Image]
                for image in images:
                    await image.download(filename='./Image/edge.jpeg', determine_type=False)
                    m_time = time.time()
                    image_operation.edge_get_2()
                    print("\033[4;37;44m用时:%0.2f秒\033[0m" % (time.time() - m_time))
                    await bot.send(event, [Image(path='./Image/edge.jpg')])
                return
                # time.sleep(random.random())
                # await bot.send(event, [Plain('哼，得不到你的夸奖也无所谓啦！！！')])
                # time.sleep(random.random())
                # m_time = time.time()
                # image_operation.edge_get_2()
                # print("用时:%0.2f秒" % (time.time()-m_time))
                # time.sleep(random.random())
                # return bot.send(event, [Image(path='./Image/edge.jpg')])
            else:
                print('线稿化1')
                # i = 0
                images = event.message_chain[Image]
                if len(images) == 0:
                    return bot.send(event, [Plain('笨蛋！你不给我图我要怎样做啦！')])
                await bot.send(event, [Plain('哼，得不到你的夸奖也无所谓啦！！！')])
                for image in images:
                    await image.download(filename='./Image/edge.jpeg', determine_type=False)
                    m_time = time.time()
                    image_operation.edge_get()
                    print("\033[4;37;44m用时:%0.2f秒\033[0m" % (time.time() - m_time))
                    await bot.send(event, [Image(path='./Image/edge.jpg')])
                return
        elif event.message_chain.has('图像增强'):
            images = event.message_chain[Image]
            if len(images) == 0:
                return bot.send(event, [Plain('笨蛋！你不给我图我要怎样做啦！')])
            await bot.send(event, [Plain('哼，得不到你的夸奖也无所谓啦！！！')])
            for image in images:
                await image.download(filename='./Image/distinct.jpeg', determine_type=False)
                m_time = time.time()
                image_operation.img_distinct()
                print("\033[4;37;44m用时:%0.2f秒\033[0m" % (time.time() - m_time))
                await bot.send(event, [Image(path='./Image/distinct.jpg')])
            return

        elif event.message_chain.has('gif合成'):
            images = event.message_chain[Image]
            if len(images) == 0:
                return bot.send(event, [Plain('笨蛋！你不给我图我要怎样做啦！')])
            elif len(images) == 1:
                return bot.send(event, [Plain('就只有一张也要做gif嘛？')])
            else:
                await bot.send(event, [Plain('哼，得不到你的夸奖也无所谓啦！！！')])
                i = 0
                for image in images:
                    await image.download(filename='./Image/togif%d.jpeg' % i, determine_type=False)
                    i += 1
                m_time = time.time()
                image_operation.togif(i)
                print("\033[4;37;44m用时:%0.2f秒\033[0m" % (time.time() - m_time))
                return bot.send(event, [Image(path='./Image/togif.gif')])

                # image_operation.img_distinct()
        elif event.message_chain.has('举牌'):
            str_text = str(event.message_chain)
            for str_name in [
                '举牌',
                '@3531733375',
                '夜子酱',
                '夜子',
                'yezi',
                ' '
            ]:
                str_text = str_text.replace(str_name, '')
            try:
                m_time = time.time()
                if image_operation.text_in_pic(str_text):
                    print("\033[4;37;44m用时:%0.2f秒\033[0m" % (time.time() - m_time))
                    return bot.send(event, [Image(path='./Image/title_in_sign.png')])
                else:
                    print("\033[4;37;44m用时:%0.2f秒\033[0m" % (time.time() - m_time))
                    return bot.send(event, [Plain('baka！那么多字根本写不下嘛！！')])
            except UnicodeEncodeError:
                return bot.send(event, [Plain('啊，有夜子不认识的字呢。什么！你才是文盲！')])

        elif event.message_chain.has('剪刀'):
            a = random.randint(0, 2)
            # print(a)
            if a == 1:
                return bot.send(event, [Plain('石头！好耶是我赢了！')])
            elif a == 2:
                return bot.send(event, [Plain('剪刀！什么！居然是平局嘛！')])
            else:
                return bot.send(event, [Plain('布……要哇！可恶！是我输了！')])
        elif event.message_chain.has('布'):
            a = random.randint(0, 2)
            if a == 1:
                return bot.send(event, [Plain('石头！可恶！是我输了！')])
            elif a == 2:
                return bot.send(event, [Plain('剪刀！好耶是我赢了！')])
            else:
                return bot.send(event, [Plain('布！什么！居然是平局嘛！')])
        elif event.message_chain.has('石头'):
            a = random.randint(0, 2)
            if a == 1:
                return bot.send(event, [Plain('石头！什么！居然是平局嘛！')])
            elif a == 2:
                return bot.send(event, [Plain('剪刀！可恶！是我输了！')])
            else:
                return bot.send(event, [Plain('布！好耶是我赢了！')])
        elif event.message_chain.has('无奖竞猜'):
            if guess:
                return bot.send(event, [Plain('不要这样啦，还有题目没有回答呢！')])
            else:
                title, answer = read_json.get_title()
                guess = answer[4]
                cause = answer[5]
                return bot.send(event, [Plain(title + '\n' +
                                              answer[0] + '\n' +
                                              answer[1] + '\n' +
                                              answer[2] + '\n' +
                                              answer[3]
                                              )])
        elif event.message_chain.has('运势'):
            period_of_time, horo = horoscope.get_horo(event.sender.id)
            # horo = "大大大大大大大大大大大大吉！"
            if period_of_time == 1:
                return bot.send(event, [Plain('咱夜观天象，发现你的运势居然是：%s' % horo)])
            elif period_of_time == 2:
                return bot.send(event, [Plain('咱晨观天象，发现你的运势居然是：%s' % horo)])
            elif period_of_time == 3:
                return bot.send(event, [Plain('咱日观天象，发现你的运势居然是：%s' % horo)])
            elif period_of_time == 4:
                return bot.send(event, [Plain('咱暮观天象，发现你的运势居然是：%s' % horo)])

        elif (event.message_chain.has('蠢') or event.message_chain.has('笨') or
              event.message_chain.has('baka') or event.message_chain.has('八嘎') or
              event.message_chain.has('baga')):

            return bot.send(event, [Plain('说别人是笨蛋的人，自己才是笨蛋！略略略！')])

        elif event.message_chain.has('番剧推荐'):
            discourse, img = anime_recommend.get_anime()
            if img:
                return bot.send(
                    event,
                    [Image(base64=img), Plain(discourse)]
                )
            else:
                return bot.send(
                    event,
                    [Plain(discourse)]
                )
        elif event.message_chain.has('问题反馈'):
            await bot.send_friend_message(1411905376, [Plain(event.sender.member_name + ':\n' + str(event.message_chain))])
            await bot.send_friend_message(3204518437, [Plain(event.sender.member_name + ':\n' + str(event.message_chain))])

            problem_of_feedback.problem_record(event.sender.member_name, str(event.message_chain))
            return bot.send(event, [Plain('dd，您的反馈夜子已经收到并反馈给清良和神心大大了哦，相信不久之后他们一定会把我变得更好然后展示在大家面前的哦。')])

        elif event.message_chain.has('摸') and event.message_chain.has('头'):
            remsg = (
                '哇哦，别这样，咱也会害羞的啦！',
                '嘿嘿嘿QwQ',
                '这样摸头的话，会秃的哦。哦，我懂了，你是想要让我来守护群里的和平是吧！'
            )
            return bot.send(event, [Plain(random.choice(remsg))])
        elif event.message_chain.has('封面提取'):
            # print(str(event.message_chain))
            abv = str(event.message_chain)
            for str_name in [
                '封面提取',
                '@3531733375',
                '鱼',
                '椰',
                '酱',
                '夜',
                '子',
                ' '
            ]:
                abv = abv.replace(str_name, '')
            if 'bv' in abv.lower():
                is_url = get_bili_pic.get_url(get_bili_pic.b_a(abv))
            elif 'av' in abv.lower():
                is_url = get_bili_pic.get_url(eval(abv[2:]))
            elif abv.isnumeric():
                is_url = get_bili_pic.get_url(eval(abv))
            else:
                is_url = get_bili_pic.get_url(get_bili_pic.b_a(abv))
            if is_url[0] == 'h':
                return bot.send(event, [Image(url=is_url)])
            else:
                return bot.send(event, [Plain(is_url)])
        # 新闻
        elif event.message_chain.has('每日新闻'):
            datalist = everday60.get_everday60()
            message_list = []
            pic_len = 0
            text_len = 0
            for data in datalist:
                if data[0] == -1:
                    return bot.send(event, [Plain(data[1])])
                elif data[0] == 'img':
                    pic_len += 1
                    message_list.append(Image(url=data[1]))
                elif data[0] == 'text':
                    text_len += len(data[1])
                    message_list.append(Plain(data[1]))
            print('图片：', pic_len, '张，文字', text_len, '个')
            return bot.send(event, message_list)

        # elif event.message_chain.has('文字测试'):
        #     a = '高师傅你据偶爱睡觉的佛i阿娇施工i阿娇共i哈怂i的感觉哦i阿萨给i哦啊结果哦噶偶i和i哦按时间段覅哈沙雕番啊刚好合适哦啊共i会感到' \
        #         '送给和啊搜狗i好i速度高渗透奥i计划骚得很广佛i俺是个哦啊水晶琥珀覅就阿斯顿佛就OK弄求回复老咔叽iu啊是德国禁止覅拉说不定' \
        #         '发i快速韩国i哦啊四u就啊岁哦电话反馈六十九年爆发 i噶哟发爱看i设计费乃噢批六十多年房子给i浪费廓iu啊我更黑u爱上豆瓣覅石膏板i' \
        #         '发四度高洪波拍摄都i该u爱上你的福啊时代速度放缓ui四大护法是的覅欧巴死哦不贵啊说法 阿斯u的话规格不能哈桑uhas覅俗话给'
        #     print(len(a))
        #     return bot.send(event, [Plain(a)])

        else:
            return bot.send(event, random.choice([
                '嗯？怎么了？又要我帮你了吗？哼╯^╰，我就知道你离不开我',
                '夜子在哟~',
                '唔~',
                '我连宇宙的尽头都不知道，又怎么能知道你这个问题呢',
                '我連宇宙嘅盡頭都唔知，又點能知你呢個問題呢',
                '我连宇宙的尽头都不晓得，又啷个可能晓得勒贼个题目滴答案。',
                '饿连遇舟外金头抖补治倒，又咋么能治倒腻盖翁题呢',
                'ฅ^._.^ฅ',
                '（叉腰）我！不！懂！！！'
            ]))
    else:
        # if '你好' in str(event.message_chain):
        #     await bot.send(event, [Plain('嘿嘿嘿')])
        #     return bot.send(event, '你好啊！')

        if ((event.message_chain.has('涩') or event.message_chain.has('色') \
             or event.message_chain.has('瑟') or event.message_chain.has('ghs'))
                and ('色子' not in str(event.message_chain))):
            if random.random() > 0.97:
                print(datetime.now(), "\033[1;31;46m" + event.group.name + "\033[0m",
                      "\033[1;32;47m" + event.sender.member_name + "\033[0m")
                print("\033[1;31;45m" + str(event.message_chain) + "\033[0m")
                return bot.send(event, [Plain('不可以瑟瑟哦！')])


@bot.on(GroupMessage)
def on_group_message(event: GroupMessage):
    global guess, cause
    if guess:
        if all(event.message_chain.has(i) for i in guess) \
                or all(event.message_chain.has(i) for i in guess.lower()):
            guess = 0
            return bot.send(event, [Plain('嘟嘟嘟~好棒耶！答对了呢！')])
        elif 'A' in str(event.message_chain).upper() or \
                'B' in str(event.message_chain).upper() or \
                'C' in str(event.message_chain).upper() or \
                'D' in str(event.message_chain).upper():
            guess = 0
            return bot.send(event, [Plain(
                '噗噗~可惜错了呢。\n'
                + cause
            )])


@bot.on(GroupMessage)
async def i_can(event: GroupMessage):
    if (At(bot.qq) in event.message_chain or event.message_chain.has('椰子酱') or event.message_chain.has('夜子') or \
        event.message_chain.has('鱼子酱') or event.message_chain.has('叶子') or event.message_chain.has('yezi')) and \
            not event.message_chain.has('//##'):

        if ((event.message_chain.has('能') or event.message_chain.has('会')) \
            and event.message_chain.has('什么')) or event.message_chain.has('指令') \
                or event.message_chain.has('功能'):
            await bot.send(event, [Plain('咱能发送二次元图片(搞点二刺螈)\n'
                                         '还能让你抽签(抽签)\n'
                                         '当然测测今天运势的小把戏咱也可以哦！（运势）\n'
                                         '还能把图片放大(waifu2x)，线稿化(线稿化)，图像增强(图像增强),gif合成(gif合成)\n'
                                         '你还可以跟咱玩猜拳，准备好了哦，剪刀！石头！布!!!\n'
                                         '还能向咱要点简简单单的题目来做哦！（无奖竞猜）\n'
                                         '不知道最近看什么番嘛？你来让咱给你推荐也不是不行……(番剧推荐)\n'
                                         '如果夜子出现了错误！请一定要告诉夜子哟！(问题反馈)\n'
                                         '当然私聊咱咱也是可以做到的哦~')])


# @bot.on(Startup)
# async def startup(event: Startup):
#     print(repr(bot.session_info.get()))
#     return bot.send_group_message(798472944, [Plain('喵呼！夜子大人来了！')])
#
#
# @bot.on(Shutdown)
# async def startup(event: Shutdown):
#     return bot.send_group_message(798472944, [Plain('夜子要走了哦，记得想咱呀！')])
#     # print(repr(bot.session_info.get()))


# @bot.on(Startup)
# async def startup(event: Startup):
#     print(repr(bot.session_info.get()))
#     return bot.send_group_message(808066290, [Plain('喵呼！夜子大人来了！')])
#
#
# @bot.on(Shutdown)
# async def startup(event: Shutdown):
#     return bot.send_group_message(808066290, [Plain('夜子要走了哦，记得想咱呀！')])
#     # print(repr(bot.session_info.get()))


@bot.on(GroupMessage)
def on_group_message_new(event: GroupMessage):
    # print(event.sender)
    # print(event.message_chain)
    # print(event.type) # 消息来源是人还是群
    # print(event.message_chain.message_id) # 消息，这句话的id
    # print(event.sender.member_name)   # 群名称
    if event.message_chain.has('机器人') or event.message_chain.has('姬弃人'):
        if (((event.message_chain.has('能') or event.message_chain.has('会'))
             and event.message_chain.has('什么')) or event.message_chain.has('指令')):
            print(datetime.now(), "\033[1;31;46m" + event.group.name + "\033[0m",
                  "\033[1;32;47m" + event.sender.member_name + "\033[0m")
            print("\033[1;31;45m" + str(event.message_chain) + "\033[0m")
            return bot.send(event, [Plain('咱能发送二次元图片(搞点二刺螈)\n'
                                          '还能让你抽签(抽签)\n'
                                          '当然测测今天运势的小把戏咱也可以哦！（运势）\n'
                                          '还能把图片放大(wifu2x)，线稿化(线稿化)，图像增强(图像增强),gif合成(gif合成)\n'
                                          '你还可以跟咱玩猜拳，准备好了哦，剪刀！石头！布!!!\n'
                                          '还能向咱要点简简单单的题目来做哦！（无奖竞猜）\n'
                                          '不知道最近看什么番嘛？你来让咱给你推荐也不是不行……(番剧推荐)\n'
                                          '如果夜子出现了错误！请一定要告诉夜子哟！(问题反馈)\n'
                                          '当然私聊咱咱也是可以做到的哦~')])
    elif event.message_chain.has('早') and len(str(event.message_chain)) <= 3 \
            or event.message_chain.has('早上好') or event.message_chain.has('哦哈'):
        print(datetime.now(), "\033[1;31;46m" + event.group.name + "\033[0m",
              "\033[1;32;47m" + event.sender.member_name + "\033[0m")
        print("\033[1;31;45m" + str(event.message_chain) + "\033[0m")
        global records_time_oha
        now_time = time.time()
        if time_out(records_time_oha, now_time, random.randint(30, 300)):
            print("已过时间，可以说早")
            records_time_oha = now_time
            return bot.send(event, [Plain('哦哈喵~')])
        print('未超出时间，不可说早')
    elif event.message_chain.has('晚安'):
        print(datetime.now(), "\033[1;31;46m" + event.group.name + "\033[0m",
              "\033[1;32;47m" + event.sender.member_name + "\033[0m")
        print("\033[1;31;45m" + str(event.message_chain) + "\033[0m")
        global records_time_sleep
        h = time.strftime('%H', time.localtime())
        now_time = time.time()

        h = int(h)

        if time_out(records_time_sleep, now_time, random.randint(30, 300)):
            print("已过时间，可以晚安")
            records_time_sleep = now_time
            if h == 0:
                return bot.send(event, [Plain('哎呀早点睡啊，你看看现在都12点多了。快去睡吧。')])
            elif h <= 5:
                return bot.send(event, [Plain('哎呀早点睡啊，你看看现在都%d点多了。快去睡吧。' % h)])
            elif h <= 7:
                return bot.send(event, [Plain('唉？一晚上没睡嘛？早点去睡吧。')])
            elif h <= 10:
                return bot.send(event, [Plain('昨天晚上没睡好嘛？')])
            elif h <= 14:
                return bot.send(event, [Plain('嗯嗯，午睡时间到了啊！')])
            elif h <= 18:
                return bot.send(event, [Plain('真的要睡了吗？现在睡觉晚上起不来怎么办？')])
            elif h <= 20:
                return bot.send(event, [Plain('唉？睡得有点早呢？是明天有什么要紧的事情要早起嘛？')])
            else:
                return bot.send(event, [Plain('哎呀，不知不觉就是晚上%d点了呢，也是时候说晚安了，好梦呦！' % (h - 12))])
        print(f"未超出时间，上次晚安时间为：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(records_time_sleep))}", )
    elif any(str(event.message_chain) == i for i in ('骰子', '骰娘', '色子')):
        print(datetime.now(), "\033[1;31;46m" + event.group.name + "\033[0m",
              "\033[1;32;47m" + event.sender.member_name + "\033[0m")
        print("\033[1;31;45m" + str(event.message_chain) + "\033[0m")
        return bot.send(event, [Plain('%s掷出了：%d' % (event.sender.member_name, random.randint(1, 99)))])
    elif any(str(event.message_chain)[:2] == i for i in ('骰子', '骰娘', '色子')) and not event.message_chain.has('-'):
        print(datetime.now(), "\033[1;31;46m" + event.group.name + "\033[0m",
              "\033[1;32;47m" + event.sender.member_name + "\033[0m")
        print("\033[1;31;45m" + str(event.message_chain) + "\033[0m")
        if str(event.message_chain)[2:].isdigit():
            a = str(event.message_chain)[2:]
            while a[0] == '0':
                if len(a) == 1:
                    return bot.send(event, [Plain('%s掷出了：%d' % (event.sender.member_name, random.randint(0, 1)))])
                a = a[1:]
            a = eval(a)
            if a == 1:
                return bot.send(event, [Plain('%s掷出了：%d' % (event.sender.member_name, random.randint(0, a)))])
        elif str(event.message_chain)[3:].isdigit():
            a = str(event.message_chain)[3:]
            while a[0] == '0':
                if len(a) == 1:
                    return bot.send(event, [Plain('%s掷出了：%d' % (event.sender.member_name, random.randint(0, 1)))])
                a = a[1:]
            a = eval(a)
            if a == 1:
                return bot.send(event, [Plain('%s掷出了：%d' % (event.sender.member_name, random.randint(0, a)))])
        else:
            a = False
        if a:
            return bot.send(event, [Plain('%s掷出了：%d' % (event.sender.member_name, random.randint(1, a)))])


'''谁是卧底'''

# 设置初始参数
undercover_wait = False
undercover_play = False
undercover_plays = []


def undercover_init():
    global undercover_wait, undercover_g_id, \
        u_undercover_id, undercover_wait, \
        undercover_plays, undercover_play, \
        the_word, ather_word
    undercover_wait = False
    undercover_play = False
    undercover_plays = []


@bot.add_background_task()
async def undercover_bg():
    global undercover_wait, undercover_g_id, \
        u_undercover_id, undercover_wait, \
        undercover_plays, undercover_play, \
        the_word, ather_word
    while True:
        if undercover_wait:
            print('等待开始')
            if time.time() - undercover_wait > 20:
                print('等人结束，开始查看人数是否合格')
                print(len(undercover_plays))
                if len(undercover_plays) > 2:
                    print(len(undercover_plays))
                    print([id[0] for id in undercover_plays])
                    ids = [id[0] for id in undercover_plays]

                    # 查看是否都是好友
                    is_frind = []
                    for i in ids:
                        is_frind.append(await bot.get_friend(i))
                    if all(is_frind):
                        print('好友存在，准备确定卧底')
                        await bot.send_group_message(undercover_g_id, [Plain('OK!game!斯达头！！'), Image(
                            url='http://i2.hdslb.com/bfs/archive/3aa28b578c4024daa8fae7a9ceaa7c62bab3e237.jpg')])
                        u_player_id = [ids[0] for ids in undercover_plays]

                        u_undercover_id = u_player_id.pop(random.randint(0, len(u_player_id) - 1))

                        the_word = undercover_thesaurus.get()
                        ather_word = the_word.pop(random.randint(0, 1))
                        for player_id in u_player_id:
                            await bot.send_friend_message(player_id, f'你的词汇是：{the_word[0]}')
                        await bot.send_friend_message(u_undercover_id, f'你的词汇是：{ather_word}')
                        undercover_wait = False
                        undercover_play = True

                    else:
                        print('有好友不存在')
                        await bot.send_group_message(undercover_g_id, '不加夜子好友的话，夜子可不能发消息啊。')
                        undercover_init()
                else:
                    await bot.send_group_message(undercover_g_id, 'BAKA!人不够三个要怎么玩啊？')
                    undercover_init()
            else:
                await asyncio.sleep(1)
        else:
            await asyncio.sleep(1)


# 关键词触发，等待等人
@bot.on(GroupMessage)
async def undercover_G(event):
    global undercover_wait, undercover_g_id, \
        u_undercover_id, undercover_wait, \
        undercover_plays, undercover_play, \
        the_word, ather_word
    if event.message_chain.has('谁是卧底') and event.message_chain.has('开'):
        if undercover_wait or undercover_play:
            return bot.send(event, 'BAKA！已经开了哦！')

        await bot.send(event, '想来玩谁是卧底的，请扣1哦！(文字里面有1就会被记录）')
        undercover_plays.append([event.sender.id, event.sender.member_name, None])
        undercover_g_id = event.group.id
        print(undercover_g_id)

        undercover_wait = time.time()
        # 设置中断，并统计人数是否符合，检测是否存在好友，


# 开始等人
@bot.on(GroupMessage)
def undercover_et_al(event):
    global undercover_wait, undercover_g_id, \
        u_undercover_id, undercover_wait, \
        undercover_plays, undercover_play, \
        the_word, ather_word
    if undercover_wait:
        if event.message_chain.has('1') and not event.message_chain.has('@'):
            ids = [id[0] for id in undercover_plays]
            print(ids)
            if (event.sender.id not in ids) and (event.sender.id != 703798532):
                undercover_plays.append([event.sender.id, event.sender.member_name, None])


# 投票
@bot.on(GroupMessage)
async def undercover_vote(event):
    global undercover_wait, undercover_g_id, \
        u_undercover_id, undercover_wait, \
        undercover_plays, undercover_play, \
        the_word, ather_word
    if undercover_play:
        players = [(int(qq[0])) for qq in undercover_plays]
        if event.message_chain.has('投票') and \
                any(event.message_chain.has(At(qq)) for qq in players):
            # 记录谁投了谁
            try:
                vote_id = int(str(event.message_chain).strip().strip('@').strip('投票'))
                undercover_plays[players.index(event.sender.id)][2] = vote_id
            except:
                return bot.send(event, '格式错误了哦。请@出你想要投票的人+投票')

            # 判断一下剩下谁没有投票
            cont = 0
            for i in undercover_plays:
                if i[2] is None:
                    cont += 1
            if cont:
                return bot.send(event, [Plain(f'还有{cont}人没有投票哦。')])
            # 当所有人都投票了，检测的票最高的人
            else:
                vote = {}
                for i in undercover_plays:
                    if i[2] in vote:
                        vote[i[2]] += 1
                    else:
                        vote.update({i[2]: 1})
                res = []
                for key, value in vote.items():
                    if value == max(vote.values()):
                        max_key = key
                        res.append(key)

                if len(res) == 1:
                    res = int(res[0])

                else:
                    res = int(random.choice(res))
                undercover_plays.pop(players.index(int(res)))
                for i in undercover_plays:
                    i[2] = None
                await bot.send(event, [At(int(res)), Plain(f'被淘汰了,惨遭{max_key}票,残念，下次努力吧！☆（票数与别人相同，也会被随机淘汰。）')])
                if res == u_undercover_id:
                    undercover_init()
                    return bot.send(event, [Plain(f'卧底gg，游戏结束！\n卧底词：{ather_word}\n非卧底词:{the_word[0]}')])

                if len(undercover_plays) == 2:
                    undercover_init()
                    return bot.send(event, [Plain(f'游戏结束！卧底赢了！\n卧底词：{ather_word}\n非卧底词:{the_word[0]}')])

            if cont <= len(undercover_plays) // 2 - 1:
                vote = {}
                for i in undercover_plays:
                    if i[2] in vote:
                        vote[i[2]] += 1
                    else:
                        vote.update({i[2]: 1})
                res = []
                for key, value in vote.items():
                    if value == max(vote.values()):
                        max_key = key
                        res.append(key)

                if len(res) == 1:
                    res = int(res[0])
                    if max_key > len(undercover_plays) // 2 + 1:
                        for i in undercover_plays:
                            i[2] = None
                        await bot.send(event, [At(int(res)), Plain(f'被淘汰了,惨遭{max_key}票,票数过半了,残念，下次努力吧！☆')])
                        if res == u_undercover_id:
                            undercover_init()
                            return bot.send(event, [Plain(f'卧底gg，游戏结束！\n卧底词：{ather_word}\n非卧底词:{the_word[0]}')])

                        if len(undercover_plays) == 2:
                            undercover_init()
                            return bot.send(event, [Plain(f'游戏结束！卧底赢了！\n卧底词：{ather_word}\n非卧底词:{the_word[0]}')])


# 重开
@bot.on(GroupMessage)
async def undercover_re(event):
    if str(event.message_chain) == '重开':
        if undercover_wait or undercover_play:
            undercover_init()
            await bot.send(event, '夜子已经做好了重开的准备!')
        else:
            await bot.send(event, 'BAKA!BAKA！游戏都没有开好嘛！')


# 特殊性排除
# 复制粘贴的不被算作艾特
@bot.on(GroupMessage)
async def troubleshooting_at(event):
    if event.message_chain.has('投票') and \
            event.message_chain.has('@') and \
            not str(event.message_chain)[str(event.message_chain).index('@') + 1].isdigit():
        return bot.send(event, '唔，请不要复制粘贴了，还是手动@一下夜子才看的懂！')


@bot.add_background_task()
async def getnews():
    # today_finished = False # 设置变量标识今天是会否完成任务，防止重复发送
    hour = 6
    minute = 28
    # hour = 12
    # minute = 33

    while True:
        await asyncio.sleep(20)
        now = time.localtime()
        h, m = now.tm_hour, now.tm_min
        print('背景任务（新闻投放）显示时间，现在是%d时%d分。%d时%d分开始投放新闻' % (h, m, hour, minute))
        if h == hour and m == minute:  # 每天早上 7:30 发送早安
            # print(now.hour. now.minute)
            print(h, '点', m, '分, 开始投放新闻')
            data_list = everday60.get_everday60()
            message_list = []
            for data in data_list:
                if data[0] == -1:
                    # return bot.send(event, [Plain(data[1])])
                    print('投放失败，每日新闻产生延迟')
                    minute += 15
                    if minute >= 60:
                        minute -= 60
                        hour += 1
                    break
                elif data[0] == 'img':
                    message_list.append(Image(url=data[1]))
                elif data[0] == 'text':
                    message_list.append(Plain(data[1]))
            await bot.send_group_message(808066290, message_list)
            # await bot.send_group_message(798472944, message_list)
            # await bot.send_group_message(1017638290, message_list)
            # 1017638290
            hour = 6
            minute = 28
            await asyncio.sleep(70)


# 同意所有加好友申请
@bot.on(NewFriendRequestEvent)
def handle_new_friend_request(event: NewFriendRequestEvent):
    return bot.resp_new_friend_request_event(
        event_id=event.event_id,
        from_id=event.from_id,
        group_id=event.group_id,
        operate=RespOperate.ALLOW,
        message=''
    )


if __name__ == '__main__':
    bot.run()
