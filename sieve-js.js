var max = process.argv[2];

var primes = [false, false];
for (var num = 2; num <= max; num++) {
  primes[num] = true;
}

count = max - 2;
for (var num = 2; num <= Math.sqrt(max); num++) {
  if (primes[num]) {
    for (var square = Math.pow(num, 2); square < max + 1; square += num) {
      if (primes[square]) {
        count--;
      }
      primes[square] = false;
    }
  }
}

console.log('Number of primes: ' + count);
