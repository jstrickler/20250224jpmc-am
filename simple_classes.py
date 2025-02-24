x = 5    #  x = int(5)
colors = list()

class TechPerson:
    pass

p1 = TechPerson()
p2 = TechPerson()

print(f"{p1 = }")

class Dog:
    COLOR = "brown"
    @classmethod  # AKA (java) static method
    def jump(cls):
        print("JUMPING!!")
        print(cls.COLOR)

    def bark(self):
        print("woof! woof!")
        print(f"{self.COLOR = }")
        
    
    def wag(self):
        print("wag wag wag")

d = Dog()  # #   instance = Class(...)
print(f"{d = }")
d.bark()  # Dog.bark(d)
# Dog.bark(d)
d.wag()
# Dog.bark(Dog()) weirdness
# Dog.bark("spam") also weird
d.jump()
Dog.jump()

m = Dog()
n = m
