class ExceptionDemo:
    def divide(self):
        try:
            a=int(input("Enter a no:"))
            b=int(input("Enter a no:"))
            print("Division Result:",a/b)
        except ZeroDivisionError:
            print("Cannot Divide By Zero")
        except ValueError:
            print("Invalid Input")
    def access_list(self):
        try:
            n=int(input("Enter no of elems:"))
            l=[]
            print("Enter the elems:")
            for i in range(n):
                v=input()
                l.append(v)
            index=int(input("Enter index to get value:"))
            print("The element is",l[index])
        except IndexError:
            print("Index Greater Than Length of the List")
    def access_dict(self):
        try:
            d={}
            n=int(input("Enter no of items of a dict:"))
            for k in range(n):
                v=input("Enter a value:")
                d[k]=v
            print("The Dictionary Created:",d)
            key=int(input("Enter key to access value:"))
            print("Value Is ",d[key])
        except KeyError:
            print("Key  Is Not Found")
a=ExceptionDemo()
a.divide()
a.access_list()
a.access_dict()
