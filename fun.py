# def sum(a,b):
#     print(a+b)

# def sum1(a,b,c):
#     print(a+b+c)

# sum(5,5)
# sum1(5,6,5)


class complex:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        p=self.x+other.x
        q=self.y+other.y
        return complex(p,q)
    
    def display(self):
        print(self.x,"+ i",self.y)

a=complex(3,2)
b=complex(4,6)
c=a+b
print(c.x,c.y)

c.display()