class student():

    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def get_name(self):
        return str(self.name)

    def get_age(self):
        return int(self.age)

    def max_course(self):
        maxcourse = max(self.course)

        '''
        maxcourse = 0
        i = 0
        while i < len(self.course):
            if maxcourse < self.course[i]:
                maxcourse = self.course[i]
            i = i + 1
        '''
        return  maxcourse

if __name__ == "__main__":
    student1 = student("张三",16,[89,70,66])
    student2 = student("李四",15,[67,92,80])
    print("姓名：" + student1.get_name() + " 年龄：" + str(student1.get_age()) + " 最高分：" + str(student1.max_course()))
    print("姓名：" + student2.get_name() + " 年龄：" + str(student2.get_age()) + " 最高分：" + str(student2.max_course()))