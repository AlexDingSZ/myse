# -*- coding: UTF-8 -*-
class dog():
    name = ""
    color = ""
    speed = 0

    def __init__(self,name="common name",color ="common color",speed=5):
        self.name = name
        self.color = color
        self.speed = speed

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def run(self,min):
        distance = self.speed * min
        return "run "+str(min)+" minutes and the distance is : " + str(distance) + " m"


if __name__ == "__main__":
    my_dog = dog("wangcai","black",20)
    his_dog = dog("little yellow","yellow",15)
    print(my_dog.get_color())
    print(my_dog.get_name())
    print(my_dog.run(5))

    print(his_dog.get_color())
    print(his_dog.get_name())
    print(his_dog.run(6))

    dog2 = dog()
    print(dog2.get_color())
    print(dog2.get_name())
    print(dog2.run(6))

    dog2 = dog()
    print(dog2.get_color())
    print(dog2.get_name())
    print(dog2.run(6))

    dog2 = dog("dog3")
    print(dog2.get_color())
    print(dog2.get_name())
    print(dog2.run(6))

    dog2 = dog("dog4","color4")
    print(dog2.get_color())
    print(dog2.get_name())
    print(dog2.run(6))

