# Command Line Arguments; input user gives from command line before execution
import sys

# Print Arguments
print("Number of arguments: ", len(sys.argv), ' arguments.')
print("Arguments ", sys.argv)

# Remove Arguments
sys.argv.remove(sys.argv[0]) # argv is a list
print("Arguments", sys.argv)

# Sum up the Arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum += number
    except Exception:
        print("Bad input")

print(sum)
