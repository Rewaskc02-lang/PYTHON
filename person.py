class person:
    def __init__(self, h, w, ag):
        self.hight = h
        self.weight = w
        self.age = ag
    def display(self):
        print(self.hight, self.weight, self.age)

class Rahul(person):# Rahul inherits from person
    def __init__(self, g, b, nm, h, w, ag):  # Added h, w, ag parameters
        super().__init__(h, w, ag)  # Fixed: super() with parentheses
        self.gender = g
        self.bankbal = b
        self.name = nm
    def display(self):
        print(self.gender, self.bankbal, self.name)

s1 = Rahul("gay", 10, "yogesh", 20, 50, 20)
print(s1.age)  # This will print: 20
