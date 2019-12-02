# Calculating Length

# len() --> returns length
firstName = "Taylor"
print(len(firstName)) # returns 6 because name contains 6 chars

lastName = "Swift"
print(len(lastName)) # returns 5 because name contains 5 chars
print()
ages = [0, 11, 43, 12, 10]
print(len(ages)) # prints how many items in the list; 5
i = 0
for i in range(0, len(ages)):
    print(ages[i])
    # i += 0 # This is not necessary since we're doing for loop with a range that is pre-set
print()
print(len(["bob", "mary", "sam"])) # Returns 3
print()
candyCollection = {"bob" : 10, "mary" : 7, "sam" : 18}
print(len(candyCollection)) # Returns 3
