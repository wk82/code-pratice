from sys import exit
from random import randint
from textwrap import dedent
# 导入模块

class scene(object):    #创建scene类
    def enter(self):    #定义enter函数
        print("this scene is not yet configured.")
        print("subclass it and implement enter().")
        exit(1)

class engine(object): #创建engine类
    def __init__(self, scene_map):  
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()
class death(scene):

    quips = [
          "you died. you kinda suck at this.",
          "your mom would be proud...if she were smarter.",
          "such a luser.",
          "i have a small puppy that's better at this.",
          "you're worse than your dad's jokes."
    ]
    def enter(self):
        print(death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class centralcorridor(scene):
    def enter(self):
        print(dedent("""
            the gothons of planet percal 25 have invaded your ship and
            destroyed your entire crew. you are the last surviving member
            and your last mission is to get the neutron destruct bomb from
            the weapon armory.
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                quick on the draw you yank out your blaster and fire it
                at the gothon.
            """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                like a world class boxer you dodge, weave, slip and slide
                right as the gothon's blaster cranks a laser past your head.
            """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                lucky for you they made you learn gothon insults in the academy.
            """))
            return 'laser_weapon_armory'

        else:
            print("does not compute!")
            return 'central_corridor'

class laserweaponarmory(scene):
    def enter(self):
        print(dedent("""
            you do a dive roll into the weapon armory, crouch and scan the
            room for more gothons that might be hiding.
        """))
        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("bzzzeddd!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                the container clicks open and the seal breaks, letting gas out.
            """))
            return 'the_bridge'
        else:
            print(dedent("""
                the lock buzzes one last time and then you hear a sickening
                melting sound as the mechanism is fused together.
            """))
            return 'death'

class thebridge(scene):
    def enter(self):
        print(dedent("""
            you burst onto the bridge with the neutron destruct bomb under
            your arm and surprise 5 gothons who are trying to take control
            of the ship.
        """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                in a panic you throw the bomb at the group of gothons and make
                a leap for the door.
            """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                you point your blaster at the bomb under your arm and you
                inch backward to the door, open it, and then carefully place
                the bomb on the floor, pinting your blaster at it.
            """))
            return 'escape_pod'

        else:
            print("does not compute!")
            return "the_bridge"

class escapepod(scene):
    def enter(self):
        print(dedent("""
            you rush through the ship desperately trying to make it to the
            escape pod before the whole ship explodes.
        """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                you jump into pod {guess} and hit the eject button.
            """))
            return 'death'

        else:
            print(dedent("""
                you jump into pod {guess} and hit the eject button.
            """))
            return 'finshed'

class finished(scene):
    def enter(self):
        print("you won! good job.")
        return 'finished'

class map(object):

    scenes = {
        'central_corridor': centralcorridor(),
        'laser_weapon_armory': laserweaponarmory(),
        'the_bridge': thebridge(),
        'escape_pod': escapepod(),
        'death': death(),
        'finished': finished(),
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = map('central_corridor')
a_game = engine(a_map)
a_game.play()
