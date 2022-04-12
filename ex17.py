#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2},arg3: {arg3}")

#*args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this one take one arguments
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("i got nothin'.")

print_two("zed", "shaw","1")
print_two_again("zed", "shaw")
print_one("first")
print_none()
