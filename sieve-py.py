import sys
import math

max = int(sys.argv[1])

primes = [False] * 2 + [True] * (max - 1)

for num in range(2, int(math.ceil(math.sqrt(max)))):
    if primes[num]:
        for square in range(int(num**2), max + 1, num):
            primes[square] = False

print("Number of primes: " + str(primes.count(True)))
