class muslims:
    def greetings(self):
        print("Salaam alaykum")
class others:
    def greetings(self):
        print("Good morning")
#polymorphism, method 1:
Yusuf = muslims()
Joseph = others()
def greet(obj):
    obj.greetings()
    return
greet(Yusuf)
greet(Joseph)
#polymorphism, method 2:
people = [muslims(), others()]
for x in people:
    x.greetings()