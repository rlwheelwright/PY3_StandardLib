# Python Comparison Operators

# TIPS:
# == --> is equal to
# <= --> is less than or equal to
# >= --> is greater than or equal to
# < --> is less than
# > --> is greater than



# < --> is less than
print(10 < 75)
print(75 < 10)

if 10 < 75:
    print("The bigger number is bigger.")
else:
    print("Lower number is lower.")

# == --> is equal to
kitten = 10
tiger = 75

if kitten < tiger:
    print("The kitten weighs less than the tiger.")
else:
    print("Somehow, the kitten weighs more than the tiger. Hmm...")

# < --> is less than
mouse = 1
if mouse < kitten and mouse < tiger:
    print("The mouse weighs the least.")
else:
    print("The mouse is heavy! Run!")

#False --> 0
#True --> 1
# > --> is greater than
print(False > True) # Prints false; see above

# Looking for first mismatched letter
# A - Z --> 1 - 26
# > --> is greater than
print("Jennifer" > "Jenny") # Returns false; see above (i !> y)

# A - Z --> 1 - 26
# <= --> is less than or equal to
print('a' <= 'b') # a = 1, b = 2, so this is true
