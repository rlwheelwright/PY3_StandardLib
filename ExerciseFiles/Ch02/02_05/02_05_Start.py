# Itertools; allows us to iterate and go through our data in different ways
import itertools

# Infinite Counting
for x in itertools.count(50, 2):
    print(x)
    if x == 60:
        break
    elif x%2 == 0:
        print("PARTY TIME!")
    else:
        break

# Infinite Cycling
x = 0
for c in itertools.cycle("RACECAR"):
    print(c)
    x += 1
    if x > 14:
        break

y = 0
for c in itertools.cycle([1,2,3,4]):
    print(c)
    y = y + 1
    if y > 20:
        break

# Infinite Repeating
z = 0
for r in itertools.repeat(True):
    print(r)
    z += 1
    if z > 19:
        break
