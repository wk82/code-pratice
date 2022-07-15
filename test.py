#class FooParent(object):
#    def __init__(self):
#        self.parent = 'I\'m the parent.'
#        print ('Parent')#

#    def bar(self,message):
#        print ("%s from Parent" % message)#

#class FooChild(FooParent):
#    def __init__(self):
#        super(FooChild,self).__init__()
#        print ('Child')#

#    def bar(self,message):
#        super(FooChild, self).bar(message)
#        print ('Child bar fuction')
#        print (self.parent)#

#if __name__ == '__main__':
#    fooChild = FooChild()
#    fooChild.bar('HelloWorld')

#def sum(*argv):
#    a, b = argv
#    return 'death'#

#print(sum(2, 4))

#a = open('/Users/kw/Downloads/aws725822194243/ak:sk/fudan.csv').read()
#print(a.split(',')[2])
#=========================
#a = ['a', 'b', 'c']
#b = ['1', '2', '3']#

#for sentence in a, b:
#    result = sentence[:2]
#    print(result)
#===========================


#class other(object):#

#    def override(self):
#        print("other override()")#

#    def implicit(self):
#        print("other implicit()")#

#    def altered(self):
#        print("other altered()")#

#class child(other):#

#    def altered():
#        print("child, before other altered()")
#        super(child, self).altered()
#        print("child, after other altered()")#
#

#son = child()
#son.implicit()
#son.override()
#son.altered()
#lexicon = gonorth
#print(lexicon.scan())

file = "-c               紧凑而不是漂亮的输出;-n               使用`null`作为单个输入值;-e               根据输出设置退出状态代码;-s               将所有输入读取（吸取）到数组中；应用过滤器;-r               输出原始字符串，而不是JSON文本;-R               读取原始字符串，而不是JSON文本;-C               为JSON着色;-M               单色（不要为JSON着色）;-S               在输出上排序对象的键;--tab            使用制表符进行缩进;--arg a v将变量$a设置为value<v>;--argjson a v将变量$a设置为JSON value<v>;--slurpfile a f  将变量$a设置为从<f>读取的JSON文本数组;--rawfile a f    将变量$a设置为包含<f>内容的字符串;--args           其余参数是字符串参数，而不是文件;--jsonargs       其余的参数是JSON参数，而不是文件;--               终止参数处理;"

fuhao = input("分割符号:")
print(fuhao)
string = file.split(fuhao)
for i in string :
    print(i)
