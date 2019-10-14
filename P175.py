class Person:
    def __init__(self):
        self.name = "bob"
    
    

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(another_bob is bob)

Shelly = Person()
not_bob = Shelly
print(bob is not_bob)
