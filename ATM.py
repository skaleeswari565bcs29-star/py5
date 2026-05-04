class InvalidPINError(Exception):
    pass
class AccountBlockedError(Exception):
    pass
class ATM:
    def __init__(self,u,p,b):
        self.username = u
        self.password = p
        self.balance = b
        self.att=0
    def verify_pin(self):
        try:
            for i in range(3):
                try:
                    entered_pin=input("\nEnter PIN:")
                    if entered_pin == self.password:
                        print("PIN Verified Successfully")
                        self.att=0
                        return 1
                    else:
                        self.att+=1
                        raise InvalidPINError("Incorrect PIN")
                except InvalidPINError:
                    print("InvalidPINError")
            raise AccountBlockedError("Account Blocked due to 3 wrong attempts")
        except AccountBlockedError:
            print("AccountBlockedError")
            return 0
    def withdraw(self,amo):
        try:
            if self.att>=3:
                raise AccountBlockedError("Account is Blocked ")
            if amo>self.balance:
                raise Exception("Insufficient Balance")
            self.balance-=amo
            print("Withdrawal Completed")
            print("Remaining Balance:", self.balance)
        except AccountBlockedError:
            print("AccountBlockedError")
        except Exception as e:
            print(e)
u=input("Enter Username:")
p=input("Set PIN:")
b=int(input("Enter Balance:"))
a=ATM(u,p,b)
a.verify_pin()
amo=int(input("Enter amount to withdraw:"))
a.withdraw(amo)
