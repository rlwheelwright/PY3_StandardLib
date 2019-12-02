# Iterative Files
myFile = open("scores.txt", "r")

# Read one line at a time
print("My one line: " + myFile.readline())
myFile.seek(0) # Re-set the seek to the start of the file

# Iterate through each line of a file
for line in myFile:
    newHighScore = line.replace("BBB", "PDJ") # This does not write to that txt file!
    print(newHighScore)

myFile.close()
