class student:
    def _int_(self,name,rollnumber,marks):
        self.name=name
        self.rollnumber=rollnumber
        self.marks=marks

    def display(self):
        print("student name: ", self.name)
        print("student rollname:", self.rollnumber)
        print("student marks:", self.marks,end="\n\n")
s1=student("pradeep",1,100)
s2=student("francis",2,87)
s3=student("anthony",3,79)
s1.display()
s2.display()
s3.display()
        
        
