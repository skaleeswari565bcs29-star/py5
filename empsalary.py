class employee:
    def __init__(self):
        self.ID=int(input("enter employee ID:"))
        self.name=input("enter employee name:")
        self.basic=int(input("enter basic salary:"))
    def display(self):
        da=0.10*self.basic
        hra=0.20*self.basic
        gs=da+hra+self.basic
        print(".....Employee Details.....")
        print("Employee ID:",self.ID,"\n","Employee Name:",self.name,"\n","Employee Basic Salary:",self.basic,"\n")
        print("Dearness allowance:",da,"\n","Houserent allowance:",hra,"\n","Gross Salary:",gs)
e=employee()
e.display()
