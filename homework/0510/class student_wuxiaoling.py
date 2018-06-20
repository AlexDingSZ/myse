class student():
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def get_name(self):
        return self.name
    def get_age(self):
        return  int(self.age)
    def get_course(self):
        for i in range(0,len(self.course)):
            for j in range(i,len(self.course)):
                first=self.course[i]
                second=self.course[j]
                if first<second:
                   self.course[i]=self.course[j]
                   self.course[j]=first
        #print self.course[0]
        return int(self.course[0])
if __name__=="__main__":
    a=student("xiaoming",17.6,[79,60,89])
    #b=student("xiaoming",18,[100,99,67])
    print (a.get_name(),a.get_age(),a.get_course())
    #print (b.get_name(),b.get_age(),b.get_course())

