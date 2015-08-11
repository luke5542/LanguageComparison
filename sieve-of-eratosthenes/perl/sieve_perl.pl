use strict;
use warnings;
use Time::HiRes qw/ time /;
use Scalar::Util qw/ looks_like_number /;

my $max = $ARGV[0];

exit 1 if !looks_like_number($max);

my $start = time;

my @primes = (0) x 2;
push(@primes, (1) x ($max - 2));
my $prime_count = $max - 2;

foreach my $num (2..sqrt($max)) {
  if ($primes[$num]) {
    for (my $square = $num * $num; $square < $max + 1; $square += $num) {
      if ($primes[$square]) {
        $prime_count--;
      }
      $primes[$square] = 0;
    }
  }
}

my $end = time;
print "Number of primes: " . $prime_count . "\n";
printf("Execution time: %.3fms\n", (($end - $start) * 1000));
