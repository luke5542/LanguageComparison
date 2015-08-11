require 'benchmark'

begin
  max = ARGV[0].to_i
  primes = nil

  time = Benchmark.realtime do
    primes = Array.new(2, false) + Array.new(max - 1, true)

    (2..Math.sqrt(max)).each do |num|
      (num * num..max + 1).step(num) do |square|
        primes[square] = false
      end if primes[num]
    end
  end

  puts "Number of primes: #{primes.count(true)}"
  puts "Execution time: #{((time) * 1000).round(3)}ms"
rescue
  exit 1
end
