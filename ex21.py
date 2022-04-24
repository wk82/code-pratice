import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors): #定义main函数,导入文件地址，编码格式，错误处理机制
    line = language_file.readline()        #读一段language_file并将内容传递给line变量

    if line:
        print_line(line, encoding, errors)         #如果line有内容，调用print_line参数
        return main(language_file, encoding, errors) #循环调用main函数，直到line无内容

def print_line(line, encoding, errors):
    next_lang = line.strip()          #strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    raw_bytes = next_lang.encode(encoding, errors)  #errors — 这可能是给定一个不同的错误处理机制。默认的错误是“严格”strict，即编码错误提出UnicodeError
    cooked_string = raw_bytes.decode(encoding, errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")  #文件路径传给languages变量

main(languages, encoding, error) #调用main函数


# encode() 编码字符串 str.encode([encoding="utf-8"][,errors="strict"])
#error指定错误处理方式，其可选择值可以是：
#strict：遇到非法字符就抛出异常。
#ignore：忽略非法字符。
#replace：用“？”替换非法字符。
#xmlcharrefreplace：使用 xml 的字符引用
# decode() 解码字节串
