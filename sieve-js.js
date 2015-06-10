var max = process.argv[2];

var start = new Date().getTime();

var primes = [false, false];
for (var num = 2; num <= max; num++) {
  primes[num] = true;
}

for (var num = 2; num <= Math.sqrt(max); num++) {
  if (primes[num]) {
    for (var square = Math.pow(num, 2); square < max + 1; square += num) {
      primes[square] = false;
    }
  }
}

var time = new Date().getTime() - start;

console.log('Number of primes: ' + primes.filter(function(value) {
    return value === true;
}).length);
console.log('Execution time: ' + time + 'ms');
