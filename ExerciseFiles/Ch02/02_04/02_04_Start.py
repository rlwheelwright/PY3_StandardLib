# Statistics Module; Calc mean, mode, standard deviation, etc.

# Given [2, 2, 3]
    # Mean = Average
    # Median = Midpoint
    # Mode = Most frequent value
    # Variance = avg of squared differences from the mean; number - 2.33 re: Given list numbers = 1/3
    # Standard deviation = square root of the variance = sqrt(1/3) = .57735

import statistics
import math

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]
print("Mean: " + str(statistics.mean(agesData))) # Converting to strings so it'll print
print("Median: " + str(statistics.median(agesData)))
print("Mode: " + str(statistics.mode(agesData)))
print(sorted(agesData))
print("Variance: " + str(statistics.variance(agesData)))
print("Standard Deviation: " + str(statistics.stdev(agesData)))
print(math.sqrt(statistics.variance(agesData)))
