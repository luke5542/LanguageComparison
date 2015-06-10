require "table"

max = tonumber(arg[1])

startTime = os.clock()
primes = {false, false, false}
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

totalTime = os.clock()-startTime
print("Number of primes: " .. primeCount)
print("Execution time: " .. (totalTime*1000) .. "ms")