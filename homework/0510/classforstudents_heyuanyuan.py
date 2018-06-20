#coding:utf-8

class student():
    def __init__(self,name,age,scores):
        self.name=name
        self.age=age
        self.scores=scores

    def get_name(self):
        name=self.name
        return str(name)

    def get_age(self):
        age=self.age
        return int(age)

    def get_highest_score(self):
        scores=self.scores
        for score_A in list(scores):
            for score_B in list(scores):
                if score_A>=score_B:
                    highscore=score_A
                else:
                    highscore=score_B
        return "%s's highest score is"%self.name+" "+str(highscore)

if __name__=="__main__":
    James=student("James",20,[86,67,89])
    Ken=student('Ken',19,[87,98,99])
    print (James.get_age())
    print (Ken.get_name())
    print (James.get_highest_score())
    print (Ken.get_highest_score())
