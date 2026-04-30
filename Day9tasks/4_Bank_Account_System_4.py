class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Account: {self.acc_no}, Balance: {self.balance}")


acc = BankAccount(101, 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.display()
