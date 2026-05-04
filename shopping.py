class smart:
    def __init__(self):
        self.items=[]
    def getinput(self,n):
        for i in range (n):
            i_name=input("\nEnter item name:")
            qu=int(input("Enter quantity:"))
            p=int(input("Enter price:"))
            self.items.append((i_name,qu,p))
    def sub(self):
        self.st=[]
        for i in range(len(self.items)):
            s=self.items[i][1]*self.items[i][2]
            self.st.append(s)
        print("Subtotal:")
        for i in range(len(self.st)):
            print("item {}:{}".format(i+1, self.st[i]), end='  ')
        return self.st
    def tot(self):
        t=0
        for i in range(0,len(self.st)):
            t=t+self.st[i]
        print("\nTotal:",t)
        if t>3000:
            d=t*(10/100)
            t=t-d
            print("After discount:",t)
        else:
            d=0
            t=t+d
            print("After discount:",t)
        g=t*(5/100)
        t=t+g
        print("gst:",g)
        print("Final Amount:",t)
n=int(input("Enter no of items:"))
b=smart()
b.getinput(n)
print("\nBill...")
b.sub()
b.tot()
