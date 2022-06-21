
class Atm:
    def __init__(self,card_number, pin, balance):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
    def CashWithdrawl(self):
        widthraw = float(input("Enter the Amount to be widthrawed"))
        self.balance = self.balance-widthraw
        print(self.balance)
    def Enquiry(self):
        print("The available balance is "+self.balance)
def main():
    transaction = Atm(123456789, 1239, 10000)
    transaction.CashWithdrawl()
    transaction.Enquiry()

