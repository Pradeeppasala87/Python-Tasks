class Staff:
    def __init__(self, name):
        self.name = name

class Professor(Staff):
    def show(self):
        print("Professor:", self.name)

class LabAssistant(Staff):
    def show(self):
        print("Lab Assistant:", self.name)

class Administrator(Staff):
    def show(self):
        print("Administrator:", self.name)

p = Professor("Dr. Rao")
l = LabAssistant("Kiran")
a = Administrator("Sita")

p.show()
l.show()
a.show()
