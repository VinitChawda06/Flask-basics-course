class Amimal():

    def __init__(self,fur):
        self.fur = fur
        print("Animal created")

    def report(self):
        print("Animal")
    
    def eat(self):
        print("eating!")

# Inheritance
class Dog(Amimal):
    
    def __init__(self,fur):
        # super() means the Parent class
        super().__init__(fur)
        print("Dog created")
    
    # Overriding the Animal class's report method 
    def report(self):
        print("I am a dog")


d = Dog("Silky")
d.eat()
d.report()
print(d.fur)
