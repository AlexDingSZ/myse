class Student():
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return str(self.name)

    def get_age(self):
        return int(self.age)

    def get_course(self):
        max=0
        if self.scores[0]>self.scores[1]:
            max = self.scores[0]
        else:
            max = self.scores[1]
        if max >self.scores[2]:
            return max
        else:
            return self.scores[2]

studentA = Student("xiaoming ","20",[100,99,88])
studentB = Student("xiaohong ","21",[66,55,80])
print (studentA.get_name(),studentA.get_age(),studentA.get_course())
print (studentB.get_name(),studentB.get_age(),studentB.get_course())