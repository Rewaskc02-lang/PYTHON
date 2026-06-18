class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
         #|--> Convert a function to be a static method.

# A static method does not receive an implicit first argument.
# To declare a static method, use this idiom:
    def hel():
        print("helloooooo")
    
    def get_av(self):
        sum=0
        i=0
        for x in self.marks:
            sum=sum+x
            i=i+1
        print(self.name," avg score is :",sum/i)
        
s1=Student("Rewas khatri",[10,20,40,80,90,99,99,99,99,99,99,99.100])
s1.get_av()
# to change name
s1.name="bbbjccjbc"
s1.get_av()
s1.hel()