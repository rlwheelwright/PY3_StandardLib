# Math Module Part I
import math

# Constants
print(math.pi)
print(math.e)
print(math.nan) # not a number
print(math.inf) # infinity
print(-math.inf) # negative infinity

# Trigonometry
obst_direction = math.cos(math.pi / 4)
print(obst_direction)
print(math.sin(math.pi / 4))
# Cosine # measures adjacent side over hypotenuse
# Sine # opposite side over hypotenuse

# Ceiling and Floor
cookies = 10.3
candy = 7
print(math.ceil(cookies)) # = 11 cookies; the .3 is the 1
print(math.ceil(candy)) # = 7

age = 47.9
otherAge = 47
print(math.floor(age)) # = 47
print(math.floor(otherAge)) # = 47
