import sys
import math

max = int(sys.argv[1])

primes = [False, False] + [True] * (max - 2)

for num in range(2, math.ceil(math.sqrt(max))):
    if primes[num]:
        for square in range(int(math.pow(num, 2)), max, num):
            primes[square] = False

print("Number of primes: " + str(primes.count(True)))
