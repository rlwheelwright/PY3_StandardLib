# Random Module
import random

# Random Numbers
print(random.random()) # Random number between 0 and 1 (float)
decider = random.randrange(2) # Value will be between 0 and 1, but not 2
if decider == 0:
    print("HEADS")
else:
    print("TAILS")
print(decider)

# Making the random roll a string, otherwise, it will not work because it'd be a str & int
print("You rolled a: " + str(random.randrange(1, 7))) # Between 1 and 6; 7 is excluded

# Random Choices
lotteryWinners = random.sample(range(101), 5) # Random sample of 5 winners out of 100; 101 is not included
print(lotteryWinners)

possiblePets = ['cat', 'dog', 'fish', 'horse', 'guinea pig', 'lizard', 'snake', 'mouse']
print("I think you should get a " + random.choice(possiblePets) + '.')

cards = ['Jack', 'Queen', 'King', 'Ace']
random.shuffle(cards)
print(cards)
