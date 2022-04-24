states = {
    'oregon': 'or',
    'florida': 'fl',
    'california': 'ca',
    'newyork': 'ny',
    'michigan': 'mi'
}

cities = {
    'ca': 'san francisco',
    'mi': 'detroit',
    'fl': 'jacksonville'
}

cities['ny'] = 'newyork'       #cities字典增加两个key
cities['or'] = 'portland'

print('-' * 10)    # 打印分隔符并打印新增加的两个key的值
print("ny state has:", cities['ny'])
print("or state has:", cities['or'])

print('-' * 10)
print("michigan's abbreviation is:", states['michigan'])
print("florida's abbreviation is:", states['florida'])

print('-' * 10)
print("michigan has:", cities[states['michigan']])
print("florida has:", cities[states['florida']])

print('-' * 10)
for state, abbrev in list(states.items()): #items()的作用是把字典中的每对key和value组成一个元组，并把这些元祖放在列表中返回。
                                           #list()将元组转换为列表
    print(f"{state} is abbreviation {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('texas') #字典 get() 函数返回指定键的值,dict.get(key, value) value可选，如果指定键的值不存在时，返回该默认值

if not state:
    print("sorry, no texas")

city = cities.get('tx', 'does not exist')
print(f"the city for the state 'tx' is: {city}")
