max = ARGV[0].to_i

primes = Array.new(2, false) + Array.new(max - 1, true)

count = max - 2
(2..Math.sqrt(max)).each do |num|
  (num**2..max + 1).step(num) do |square|
    if primes[square]
      count -= 1
    end
    primes[square] = false
  end if primes[num]
end

puts "Number of primes: #{count}"
