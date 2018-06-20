class student:
    #定义一个类
    #初始化，init构造一个实体
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores
        #给实体赋值
    def get_name(self):
        return self.name
        # print(self.name)
    def get_age(self):
        return  self.age
    def max(self):
        #max()函数为列表函数，求最大值，min（）求最小值
        return max(self.scores)
        # max = 0
        # if self.scores[0] > self.scores[1]:
        #     max = self.scores[0]
        # else:
        #     max = self.scores[1]
        # if max > self.scores[2]:
        #     return max
        # else:
        #     return  self.scores[2]
if __name__ == "__main__":
    #给实体赋值
    studentA = student("lili","17",[89,98,58])
    studentB = student("tom","18",[88,78,87])
    print(studentA.get_name())
    print(studentB.get_name())
    print(studentA.get_age())
    print(studentB.get_age())
    print(studentA.max())
    print(studentB.max())
    print(studentA,studentB)