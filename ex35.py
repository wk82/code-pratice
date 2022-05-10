class animal(object):
    pass
##??
class dog(animal):
    def __init__(self, name):
        ##??
        self.name = name

##??
class cat(animal):
    def __init__(self, name):
        ##??
        self.name = name

##??
class person(object):

    def __init__(self, name):
        ##??
        self.name = name
        self.pet = None

##??
class employee(person):
    def __init__(self, name, salary):
        ##??
        super(employee, self).__init__(name)
        ##??
        self.salary = salary

class fish(animal):
    pass
##??
class salmon(fish):
    pass
##??

class halibut(fish):
    pass

## rover is-a dog
rover = dog("rover")

##??
satan = cat("satan")

##??
mary = person("mary")

##??
mary.pet = satan

##??
frank = employee("frank", 120000)
print("this is " , frank.name)

##??
frank.pet = rover


##??
flipper = fish()

##??
crouse = salmon()

##??
harry = halibut()
