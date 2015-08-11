import sys
import math
import time

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    exit(1)

max = int(sys.argv[1])

start = int(round(time.time() * 1000))

primes = [False] * 2 + [True] * (max - 1)

for num in range(2, int(math.ceil(math.sqrt(max)))):
    if primes[num]:
        square = num * num
        while square < max:
            primes[square] = False
            square += num

end = int(round(time.time() * 1000))

print("Number of primes: " + str(primes.count(True)))
print("Execution time: " + str(end - start) + "ms")
