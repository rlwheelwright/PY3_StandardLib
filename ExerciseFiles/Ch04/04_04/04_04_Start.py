# Create a Timer with the Time module
import time

run = input("Start? >")

seconds = 0

if run == "y":
    while seconds != 6:
        print(">", seconds)
        time.sleep(1)
        seconds += 1
    print("Done!")
