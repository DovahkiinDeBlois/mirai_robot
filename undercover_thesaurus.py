from random import choice, randint
thesaurus = [
    ['枕头', '抱枕', '床单', '被子'],
    ['奖牌', '金牌', '奖状', '奖品'],
    ['蝴蝶', '蜜蜂', '蜂蜜', '苍蝇', '飞蛾'],
    ['气泡', '水泡', '液泡'],
    ['胡子', '眉毛', '头发', '汗毛'],
    ['油条', '麻花', '豆浆', '包子', '牛奶', '馒头'],
    ['水盆', '水桶', '浴缸', '马桶', '茶杯'],
    # ['结婚', '恋爱'],
    ['酸菜鱼', '水煮鱼', '糖醋鱼'],
    ['薰衣草', '满天星', '勿忘我'],
    # ['小鸟游六花', '宝多六花'],
    ['雷姆', '艾米利亚', '拉姆'],
    ['自行车', '电动车', '三轮车'],
    ['红烧牛肉面', '鲜虾鱼板面', '老坛酸菜牛肉面', ''],
    ['包青天', '狄仁杰'],
    ['公交', '地铁', '轻轨'],
    ['橙汁', '椰汁', '葡萄汁', '乌龙茶', '咖啡'],
    ['恐龙', '恶龙', '飞龙'],
    ['胖次', '水手服', '死库水', '黑丝', '白丝', '巫女服', ''],
    ['霸王龙', '翼龙', '三角龙', '蜥蜴'],
    ['漫画', '动画', '小说', '游戏'],
    ['兔子', '狗', '猫猫', '鹦鹉'],
    ['蒸羊羔', '蒸熊掌', '蒸鹿耳', '焼花鸭', '烧子鹅', '卤猪卤鸭', '酱鸡腊肉'],
    # ['面目全非脚', '还我漂漂拳'],
    ['盆栽', '假山', '雕塑'],
    ['九阴白骨爪', '降龙十八掌', '五雷轰天掌', '化骨绵绵掌'],
    ['原神', '明日方舟', '王者荣耀', '喵斯快跑', 'phigros', 'cytusII', '帕斯卡契约', '黑暗之魂', ''],
    ['潜居深海的克苏鲁——章鱼哥', '黄衣之主哈斯塔——海绵宝宝', '不可名状的粉红五角星——派大星', '噩梦独眼怪——痞老板', '深居的长毛怪兽——松鼠珊迪', ],
    # ['清良老婆', '茉子老婆', '陵风奶奶', '百音盒酱', '遇事不决，泰坦神狐'],
    # ['卷积神经网络', '人工神经网络'],
    ['网易云音乐', '酷狗音乐', '酷我音乐', '咪咕音乐'],
    ['香蕉', '苹果', '大鸭梨', '橘子', '柚子', '榴莲', '甘蔗', ''],
    ['臭豆腐', '腐乳', '老干妈', ],
    ['cos', 'sin', 'tan'],
    # ['潦水尽而寒潭清', '烟光凝而暮山紫'],
    # ['落霞与孤鹜齐飞', '秋水共长天一色'],
    ['贵人鸟', '361', '安踏', '李宁'],
    ['红牛', '黄牛'],
    ['奥观海', '川建国', '拜振华'],
    ['晴天', '雨天', '雷阵雨', '多云', '雪天', '雨夹雪', ''],
    ['Fe+CuSO4═FeSO4+Cu', '3H2+Fe2O3==2Fe+3H2O'],
    ['机智的党妹', '回形针', 'LexBurner', '嘉心糖', '孙笑川', 'A-SOUL', '东百往事', 'A-SOUL'],
    ['陈睿', '蒙古上单'],
    ['哪吒', '杨戬', '沉香(宝莲灯主角)'],
    ['冰壶', '花样滑冰', '短道速滑', '冰球', '越野滑雪', '跳台滑雪'],
    ['男性', '女性', '秀吉', '朕？(fgo里秦始皇的性别，我知道你可能很迷惑，但是加油吧小伙汁！)'],
    ['肯德基', '麦当劳', '必胜客', '华莱士', '沙县小吃'],
    ['豌豆射手', '窝瓜', '樱桃炸弹', '土豆雷', '坚果墙', '毁灭菇', '机枪射手'],
    ['馒头', '包子', '饺子', '面条', '大饼', '花卷', '米饭'],
    ['太阳', '地球', '月亮'],
    # ['', ''],
    # ['', ''],
    # ['', ''],
    # ['', ''],
    # ['', ''],
]


def get():
    a = choice(thesaurus).copy()
    ls1 = a.pop(randint(0, len(a)-1))
    ls2 = a.pop(randint(0, len(a)-1))
    return [ls1, ls2]
