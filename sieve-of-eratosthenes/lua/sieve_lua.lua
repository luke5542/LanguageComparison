require "table"

max = tonumber(arg[1])

if max == nil then
  os.exit(1)
end

local getTime = os.clock
local sqrt = math.sqrt
local ceil = math.ceil

local startTime = getTime()
local primes = {false, false}
for num = 2, max do
  primes[num] = true
end
local primeCount = max - 1

for num = 2, ceil(sqrt(max)) do
  if primes[num] then
    for square = num ^ 2, max + 1, num do
      if primes[square] then
        primeCount = primeCount - 1
      end
      primes[square] = false
    end
  end
end

totalTime = getTime()-startTime
print("Number of primes: " .. primeCount)
print("Execution time: " .. (totalTime*1000) .. "ms")
