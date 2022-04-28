import random
from urllib.request import urlopen
import sys

word_url = "http://learncodethehardway.org/words.txt"
words = []

phrases = {
        "class %%%(%%%):":
            "make a class named %%% that is a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)" :
            "class %%% has a __init__ that takes self and *** params.",
        "class %%%(object):\n\tdef ***(self, @@@)":
            "class %%% has a function *** that takes self and @@@ params.",
        "*** = %%%()":
            "set *** to an instance of class %%%.",
        "***.***(@@@)":
            "from *** get the *** function, call it with params self, @@@.",
        "***.*** = '***'":
            "from *** get the *** attribute and set it to '***'."
}

if len(sys.argv) ==2 and sys.argv[1] == "english":
    phrase_first = True
else:
    phrase_first = False


for word in urlopen(word_url).readlines(): #urlopen() 读取url中内容
#readlines()读取所有行然后把它们作为一个字符串列表返回，readline()每次读取一行；返回的是一个字符串对象
#read()读取整个文件，将文件内容放到一个字符串变量
    words.append(str(word.strip(), encoding="utf-8"))  #将url中内容写入words列表
#strip()默认删除空白符（包括'\n', '\r',  '\t',  ' ')
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(words, snippet.count("%%%"))]
    #capitalize() 将字符串的第一个字母变成大写,其他字母变小写
    #random.sample的用法，多用于截取列表的指定长度的随机数，但是不会改变列表本身的排序，原型为：random.sample(列表变量, 个数)
    #count()统计字符串中某个字符出现的次数。str.count("char", start,end) 或 str.count("char")，start开始位置，默认0
    #end结束位置，默认是字符长短
    other_names = random.sample(words, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        #random.randint()的原型为：random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限
        param_names.append(', '.join(random.sample(words, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)
            #replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
        for word in other_names:
            result = result.replace("***", word, 1)
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try:
    while True:
        snippets = list(phrases.keys())
        #dict.keys() 字典key的值、dict.values() 字典value值 和 dict.items() 返回的都是视图对象
        random.shuffle(snippets)
        #andom.shuffle()如果你想将一个序列中的元素，随机打乱
        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)
            if phrase_first:
                question, answer = answer, question
            print(question)

            input('> ')
            print(f"answer: {answer}\n\n")

except EOFError:
    print("\nbye")
