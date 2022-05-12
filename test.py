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
a = ['a', 'b', 'c']
b = ['1', '2', '3']

for sentence in a, b:
    result = sentence[:2]
    print(result)
