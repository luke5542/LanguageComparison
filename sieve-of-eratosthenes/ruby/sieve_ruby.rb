max = ARGV[0].to_i

time_s = Time.now

primes = Array.new(2, false) + Array.new(max - 1, true)

(2..Math.sqrt(max)).each do |num|
  (num**2..max + 1).step(num) do |square|
    primes[square] = false
  end if primes[num]
end

time_e = Time.now

puts "Number of primes: #{primes.count(true)}"
puts "Execution time: #{((time_e - time_s) * 1000).round(3)}ms"
