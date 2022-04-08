from sys import argv

script, user_name = argv
prompt = '> '

print(f"hi {user_name}, i'm the {script} script")
print("i'd like to ask you a few question.")
print(f"do you like me {user_name}")
likes = input(prompt)

print(f"where do {user_name}")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f'''
alright, so you said {likes} about
you live in {lives}. not sure where that is
you have a {computer} computer''' )
