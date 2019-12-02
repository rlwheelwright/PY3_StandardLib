r = range(0, 30)
print(type(r))
print(type(10))
print(type('a'))
print(type("Hi there"))

class Car:
    pass

class Truck(Car):
    pass

c = Car()
convert = Car()
t = Truck()
print(type(c)) # Truck
print(type(t)) # Truck
print(type(c) == type(t)) # False
print(type(c) == type(convert)) # True

print(isinstance(c, Car)) # True
print(isinstance(t, Car)) # Accounts for inheritance; returns True
if isinstance(r, range):
    print(list(r))
