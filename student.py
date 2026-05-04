class student:
    def __init__(self):
        self.name=input("enter student name:")
        self.marks=[]
    def input(self):
         for i in range(5):
            m=int(input("enter student marks:"))
            self.marks.append(m)
    def display(self):
        g=''
        t=0
        for i in self.marks:
            t=t+i
            a=t/5
        if a>=90:
            g="A"
        elif a>=80:
            g="B"
        elif a>=70:
            g="C"
        elif a>=60:
            g="D"
        elif a>=50:
            g="R"
        else:
            g="F"
        print(self.name,"\tTotal:",t,"\t","Average mark:",a,"\tGrade:",g)
s=student()
s.input()
s.display()
