#隐式继承
#class parent(object):
#    def implicit(self):
#        print("parent implicit()")#

#class child(parent):
#    pass#

#dad = parent()
#son = child()#

#dad.implicit()
#son.implicit()


#显式继承
#class parent(object):
#    def override(self):
#        print("parent override()")#

#class child(parent):
#    def override(self):
#        print("child override()")#

#dad = parent()
#son = child()#

#dad.override()
#son.override()

#在运行前或运行后替换
class parent(object):
    def altered(self):
        print("parent altered()")

class child(parent):
    def altered(self):
        print("child,before parent altered()")
        super(child, self).altered()   #用child,self两个参数调用super,在此返回的基础上调用altered.
        print("child,after parent altered()")

dad = parent()
son = child()

dad.altered()
son.altered()
