class Product:
    def __init__(self, name):
        self.name = name

class ElectronicProduct(Product):
    def __init__(self, name, warranty):
        super().__init__(name)
        self.warranty = warranty

class MobilePhone(ElectronicProduct):
    def __init__(self, name, warranty, brand):
        super().__init__(name, warranty)
        self.brand = brand

    def display(self):
        print(self.name, self.brand, self.warranty)

m = MobilePhone("Smartphone", "1 year", "Samsung")
m.display()
