class animal():
    def __init__(self, name): #类属性初始化
        self.name = name
    def great(self): #定义类的方法
        print("hello,iam an %s " % self.name)

#class dog():
#    def __init__(self, name):
#        self.name = name
#    def great(self):
#        print("wangwang, iam %s" % self.name)
class dog(animal): # 子类继承animal父类定义的属性
    def great(self):
        print("wangwang, iam %s " %self.name)

#animal = animal('animal')
#animal.great()
dog = dog('dog')
dog.great()


#多态，只调用父类，也可以调用子类的函数，使用更灵活
def hello(animal):
    animal.great()

t = animal("pig")
hello(t)

dog = dog("dog")
hello(dog)


# Iterators 循环
class Fib():
    def __init__(self):
        self.a, self.b =0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
fib = Fib()
for i in fib:
    if i > 10:
        break
    print(i, end='')
