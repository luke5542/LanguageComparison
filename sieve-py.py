import sys
import math
import time

max = int(sys.argv[1])

start = int(round(time.time() * 1000))

primes = [False] * 2 + [True] * (max - 1)

for num in range(2, int(math.ceil(math.sqrt(max)))):
    if primes[num]:
        for square in range(int(num**2), max + 1, num):
            primes[square] = False

end = int(round(time.time() * 1000))

print("Number of primes: " + str(primes.count(True)))
print("Execution time: " + str(end - start) + "ms")
