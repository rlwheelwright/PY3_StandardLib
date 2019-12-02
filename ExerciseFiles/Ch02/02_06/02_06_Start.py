# Itertools Part 2
    # Permutation: a way, espcially one of several possible variations,
    # in which a set or number of things can be ordered or arranged
    # Ex: 123
    # Permutations = 123 | 132 | 231 | 213 | 312 | 321
import itertools

# Permutations: Order matters - some copies with same inputs but in different order
election = {1: "Barb", 2: "Karen", 3: "Erin"}
for p in itertools.permutations(election):
    print(p) # returns just the key; not the value

for p1 in itertools.permutations(election.values()):
    print(p1)

# Combinations: Order does not matter - no copies with same inputs
    # Combination: No set will have the same exact elements as another
    # Ex: Work Eat Play; Combinations = Eat Work, Eat Play, Play Work
colorsForPainting = ['Red', 'Blue', 'Purple', 'Orange', 'Pink', 'Black', 'White', 'Cyan', 'Yellow', 'Green']
for c in itertools.combinations(colorsForPainting, 3):
    print(c)
