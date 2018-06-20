from dog import dog


class husky(dog):

    def __init__(self, name, color, speed):
        dog.__init__(self, name, color,speed)

    def broken_home(self, name):
        return "把 "+ name +"拆了!"

    def run(self,miles):
        return "拉雪橇 ："+ str(miles) + " miles"


husky1 = husky("erha","black and white",30)
print(husky1.get_name())
print(husky1.get_color())
print(husky1.run(5))
print(husky1.broken_home("sofa"))
print(husky1.run(20))