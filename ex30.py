ten_things = "apples oranges crows telephone light sugr"

print("wait there are not 10 things in that list. let's fix that.")

stuff = ten_things.split() #split(' ', 1)指定字符串中的分隔符对字符串进行分片，默认为所有的空字符,1为分割次数，默认-1，分割所有。返回值分割后字符串列表
more_stuff = ["day", "night", "song", "frisbee", "cron", "banana",
              "girl", "boy"]



while len(stuff) != 10:
    next_one = more_stuff.pop() #pop()根据索引删除并返回删除的元素，表示删除最后一个
    print("adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")


print("there we go: ", stuff)

print("let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff)) #join()序列中的元素以指定的字符连接生成一个新的字符串
print(''.join(stuff[3:5]))
