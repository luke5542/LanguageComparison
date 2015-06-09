max = tonumber(arg[1])

primes = {false}
for num = 2, max do
  primes[num] = true
end
primeCount = max - 1

for num = 2, math.ceil(math.sqrt(max)) do
  if primes[num] then
    for square = num ^ 2, max + 1, num do
      if primes[square] then
        primeCount = primeCount - 1
      end
      primes[square] = false
    end
  end
end

print("Number of primes: " .. primeCount)
