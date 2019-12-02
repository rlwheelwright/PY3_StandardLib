# Sorted function can be applied to Lists, tuples, strings, dictionaries, etc.

# Least to Greatest
pointsInAGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInAGame)
print(sortedGame) # Prints lowest to highest

# Alphabetically
children = ['Sue', 'Jerry', 'Linda']
print(sorted(children))
print(sorted(['Sue', 'jerry', 'linda']))

# Key Parameters
print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(pointsInAGame, reverse=True)) # Prints highest to lowest

leaderBoard = {231: "CKL",
                123: "ABC",
                432: "JKC"}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(max(leaderBoard))) # Same as print(leaderBoard.get(432))...just better my way

students = [('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
print(sorted(students, key=lambda student:student[0])) # Prints on key of first value in tuple; Name
print(sorted(students, key=lambda student:student[1])) # Prints on key of second value in tuple; Grade
print(sorted(students, key=lambda student:student[2])) # Prints on key of third value in tuple; Age
