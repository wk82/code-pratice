import string

def check(pwd):
    #密码必须大于6个字符
    #isinstance() 函数来判断一个对象是否是一个已知的类型
    if not isinstance(pwd, str) or len(pwd) < 6:
        return "not suitable for passwd"
    #密码强度等级与包含字符等级种类的对应关系
    d = {"1": "weak", "2": "below middle", "3": "middle", "4": "strong"}
    #分布标记pwd是否包含数字，小写字母，大写字母，指定标点符号
    r = [False] * 4
    for ch in pwd:
        #是否包含数字
        if not r[0] and ch in string.digits:
            r[0] = True
        #是否包含小写字母
        elif not r[1] and ch in string.ascii_lowercase:
            r[1] = True
        #是否包含大写字母
        elif not r[2] and ch in string.ascii_uppercase:
            r[2] = True
        #是否包含标点符号
        elif not r[3] and ch in './;<>':
            r[3] = True
        #统计包含的字符种类，返回密码强度
    print(r)
    return d.get(str(r.count(True)), 'errors')


print(check('sdfefsf345.,,H'))


#String模块中的常量：
#string.digits: 生成所有数字 0~9
#string.ascii_letters 生成所有字母（大小写）
#string.lowercase：所有小写字母
#string.uppercase：所有大写字母
#string.punctuation：所有标点
#string.printable：可打印字符的字符串
