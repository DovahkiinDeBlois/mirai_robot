import re
import cv2
import base64
import imageio
import numpy as np

from math import ceil
from PIL import Image, ImageFont, ImageDraw
from zhon.hanzi import punctuation


def cv_show(img, name='randomaosdjifo'):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def distinct_get(pic):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    res_clahe = clahe.apply(pic)
    return res_clahe


def twico_over():
    pic = cv2.imread('Image/wifu2x.jpeg')
    pic = cv2.pyrUp(pic)
    cv2.imwrite('Image/wifu2x.jpg', pic)
    # i = 0
    # for image in images:
    #     i += 1
    #     if i > 1:
    #         return 1
    # images.dwnload(directory='/Image/wifu2x.png')
    # 'http://gchat.qpic.cn/gchatpic_new/1411905376/808066290-2154774527-E8A98930EF7EF94BE921284CFEB712C8/0?term=2'
    # print(url)
    # pic = requests.get(url)
    # img = cv2.imdecode(np.frombuffer(pic.content, np.uint8), cv2.IMREAD_COLOR)
    #
    # pic = cv2.pyrUp(img)
    #
    # pic = pic.astype(np.uint32)
    #
    # pic = Image.fromarray(cv2.cvtColor(pic, cv2.COLOR_BGR2RGB))

    # print(pic.dtype, pic.astype(np.uint32).dtype)

    # cv2.imwrite('Image/wifu2x.jpg', pic)
    # return pic.tobytes()
    # return base64.b64encode(pic.tobytes()).decode()
    # print(type(pic))
    # print('return|', type(base64.b64encode(pic.tobytes()).decode()))
    # return base64.b64encode(pic.tobytes()).decode()


def edge_get():
    pic = cv2.imread('Image/edge.jpeg', 0)
    pic = cv2.Canny(pic, 50, 127)
    #
    # m = min(pic.shape[0:2])
    # kernel = np.ones((m // 255, m // 255), np.uint8)
    # pic = cv2.morphologyEx(pic, cv2.MORPH_CLOSE, kernel)
    pic = 255-pic
    cv2.imwrite('Image/edge.jpg', pic)
    # return 0


def edge_get_2():
    orgimg = r'Image/edge.jpeg'
    outimg = r'Image/edge.jpg'
    a = np.asarray(Image.open(orgimg).convert('L')).astype('float')

    # 根据灰度变化来模拟人类视觉的明暗程度
    depth = 10.  # 预设虚拟深度值为10 范围为0-100
    grad = np.gradient(a)  # 提取梯度值
    grad_x, grad_y = grad  # 提取x y方向梯度值 解构赋给grad_x, grad_y

    # 利用像素之间的梯度值和虚拟深度值对图像进行重构
    grad_x = grad_x * depth / 100.
    grad_y = grad_y * depth / 100.  # 根据深度调整x y方向梯度值

    # 梯度归一化 定义z深度为1. 将三个梯度绝对值转化为相对值，在三维中是相对于斜对角线A的值
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A

    # 令三维中是相对于斜对角线的值为1
    vec_el = np.pi / 2.1  # 光源俯视角度 弧度值 接近90度
    vec_az = np.pi / 4.  # 光源方位角度 弧度值 45度
    dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x轴的影响 对角线在x轴投影
    dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y轴的影响 对角线在y轴投影
    dz = np.sin(vec_el)  # 光源对z轴的影响 对角线在z轴投影

    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
    b = b.clip(0, 255)  # 为了避免数据越界，生成灰度值限制在0-255区间
    im = Image.fromarray(b.astype('uint8'))  # 图像更构
    im.save(outimg)  # 保存图片


def img_distinct():
    pic = cv2.imread('Image/distinct.jpeg')
    pic_b = pic[:, :, 0]
    pic_g = pic[:, :, 1]
    pic_r = pic[:, :, 2]

    pic_r = distinct_get(pic_r)
    pic_g = distinct_get(pic_g)
    pic_b = distinct_get(pic_b)

    pic[:, :, 0] = pic_b
    pic[:, :, 1] = pic_g
    pic[:, :, 2] = pic_r

    cv2.imwrite('Image/distinct.jpg', pic)


def togif(i):
    pic_list = []
    # try:
    for i in range(i):
        pic_list.append(cv2.imread('Image\\togif%d.jpeg' % i))
        # print(type(pic_list[i]))
        # print(pic_list[i].shape[0], '/|\\', pic_list[i].shape[1])
    # print((pic_list[i].shape[1] for i in range(len(pic_list))))
    wide = max(pic_list[i].shape[1] for i in range(len(pic_list)))
    high = max(pic_list[i].shape[0] for i in range(len(pic_list)))
    print(high, wide)
    i = 0
    for pic in pic_list:

        pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
        if pic.shape[0] / high > pic.shape[1] / wide:
            pic = cv2.resize(pic, (int(pic.shape[1] / pic.shape[0] * high), high))
        elif pic.shape[1] / wide > pic.shape[0] / high:
            pic = cv2.resize(pic, (wide, int(pic.shape[0] / pic.shape[1] * wide)))
        elif pic.shape[1] == wide and pic.shape[0] == high:
            pass
        else:
            if wide > high:
                pic = cv2.resize(pic, (high, high))
            else:
                pic = cv2.resize(pic, (wide, wide))
        pic_list[i] = cv2.copyMakeBorder(
            pic,
            int((high - pic.shape[0]) / 2),
            ceil((high - pic.shape[0]) / 2),
            int((wide - pic.shape[1]) / 2),
            ceil((wide - pic.shape[1]) / 2),
            cv2.BORDER_CONSTANT, value=(255, 255, 255)
        )

        i += 1
    # print('gif')
    imageio.mimsave('Image/togif.gif', pic_list, 'GIF', duration=0.4)


def text_in_pic(str_text):
    # 处理文字
    # 将文字转化成一行
    str_text = ''.join(str_text.split())
    print(str_text)
    bk_img = cv2.imread("Image\\Raise_a_sign.png")
    # 设置需要显示的字体
    fontpath = "font/simsun.ttc"  # 32为字体大小
    # 字体大小*文字所占字节等于文字在图片中所占用的宽度，在这里。我们的定值是896
    # 求文字可以转化成几行几列
    xy = len(str_text.encode('gbk'))
    print(str_text)
    if xy > 432:
        return 0    # 这里return
    # xy *= 2
    y = x = int(xy ** 0.5)
    # x -= 2
    if x*x != xy:
        y += 1
        if x*y != xy:
            y += 1
    if y > 18:
        y = 18
        x = xy // y + 1
    x *= 2
    y //= 2
    y += 1

    # y为最大行数
    f_size = 288 // y
    if f_size > 64:
        f_size = 64
    print(f_size)
    print(x, y)
    font = ImageFont.truetype(fontpath, f_size)
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    # 绘制文字信息<br># (100,300/350)为字体的位置，(255,255,255)为白色，(0,0,0)为黑色

    count = [0, 0, 0]
    str_list = ['']
    for str_i in str_text:
        # 如果是中文的话
        if '\u4e00' <= str_i <= '\u9fa5' or str_i in punctuation:
            count[1] += 2
        else:
            count[1] += 1

        if count[1] >= x:
            count[0] += 1
            count[1] = 0
            str_list.append('')
        str_list[count[0]] += str_i
        count[2] += 1

    i = 0
    for mystring in str_list:
        draw.text((200, 530+f_size*i), mystring, font=font, fill=(0, 0, 0))
        i += 1

    bk_img = np.array(img_pil)

    cv2.imwrite('Image/title_in_sign.png', bk_img)

    return 1


if __name__ == '__main__':
    togif(4)

