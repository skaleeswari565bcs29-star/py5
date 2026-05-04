class eb:
    def __init__(self):
        self.units=int(input("enter units used:"))
    def display(self):
        a=0
        if self.units<=100:
            a="No Amount"
        if self.units>100 and self.units<=200:
            a=a+((self.units-100)*1.5)
        elif self.units>200 and self.units<=300:
            a=a+(100*1.5)+((self.units-200)*2.5)
        elif self.units>300 and self.units<=400:
            a=a+(100*1.5)+(200*2.5)+((self.units-300)*4)
        elif self.units>401:
            a=a+(100*1.5)+(200*2.5)+(300*4)+((self.units-400)*5)
        print("Units used:",self.units,"\nElecticity BillAmount:",a)
e=eb()
e.display()
