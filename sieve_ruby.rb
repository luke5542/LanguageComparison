max = ARGV[0].to_i

primes = Array.new(2, false) + Array.new(max - 1, true)

(2..Math.sqrt(max)).each do |num|
  (num**2..max + 1).step(num) do |square|
    primes[square] = false
  end if primes[num]
end

puts "Number of primes: #{primes.count(true)}"
