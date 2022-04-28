import string

def check(pwd):
    #密码必须大于6个字符
    if not isinstance(pwd, str) or len(pwd) < 6:
        return "not suitable for passwd"
    #密码强度等级与包含字符等级种类的对应关系
    d = {"1": "weak", "2": "below middle", "3": "middle", "4": "strong"}
    #分布标记pwd是否包含数字，小写字母，大写字母，指定标点符号
    r = [False] * 4
    for ch in pwd:
        #是否包含数字
        if ch in string.digits:
            r[0] = True
        #是否包含小写字母
        elif ch in string.ascii_lowercase:
            r[1] = True
        #是否包含大写字母
        elif ch in string.ascii_uppercase:
            r[2] = True
        #是否包含标点符号
        elif ch in './;<>':
            r[3] = True
        #统计包含的字符种类，返回密码强度
    print(r)
    return d.get(str(r.count(True)), 'errors')


print(check('sejhHljk12'))
