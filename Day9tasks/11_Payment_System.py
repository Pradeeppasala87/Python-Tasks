class Payment:
    def process_payment(self):
        pass

class CreditCard(Payment):
    def process_payment(self):
        print("Paid using Credit Card")

class UPI(Payment):
    def process_payment(self):
        print("Paid using UPI")

class NetBanking(Payment):
    def process_payment(self):
        print("Paid using Net Banking")

for method in [CreditCard(), UPI(), NetBanking()]:
    method.process_payment()
