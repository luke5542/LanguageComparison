var max = process.argv[2];

if (isNaN(max)) {
  process.exit(1);
}

var start = new Date().getTime();

var primes = [false, false];
for (var num = 2; num < max; num++) {
  primes[num] = true;
}

var numPrimes = max - 2;

for (var num = 0; num < Math.sqrt(max); ++num) {
  if (primes[num]) {
    var square = num * num;
    while(square < max)
    {
      if(primes[square])
      {
        --numPrimes;
        primes[square] = false;
      }
      square += num;
    }
  }
}

var time = new Date().getTime() - start;

console.log('Number of primes: ' + primes.filter(function(value) {
    return value === true;
}).length);
console.log('Execution time: ' + time + 'ms');
