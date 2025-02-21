#Parent class
class calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return (self.x + self.y)
#inheritance
class Add(calculator):
    def __init__(self, x, y):
        super().__init__(x, y)
    def result(self):
        return (self.x + self.y)
test_1 = Add(13, 4)
#Composition
addition = calculator(10, 15)
class add_comp:
    def __init__(self, addition):
        self.addition = addition
    def result(self):
        return self.addition.add()
test_2 = add_comp(addition)
print (f"inheritance: {test_1.result()}")
print(f"Composition: {test_2.result()}")
print(test_1.add())