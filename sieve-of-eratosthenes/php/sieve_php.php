<?php
ini_set('memory_limit', '2G');

if(count($argv) != 2 || !is_numeric($argv[1])) {
    exit(1);
}

$max = intval($argv[1]);

$start = microtime(true);

$primes = array_merge(array(0, 0), array_fill(2, $max - 1, 1));

foreach(range(2, intval(floor(sqrt(floatval($max))))) as $num) {
    if($primes[$num] == 1) {
        // Deal with range warning...
        if(pow($num, 2) + $num > $max + 1) {
            $primes[pow($num, 2)] = 0;
        }
        else {
            foreach(range(pow($num, 2), $max + 1, $num) as $square) {
                $primes[$square] = 0;
            }
        }
    }
}

$end = microtime(true);

print("Number of primes: " . array_count_values($primes)[1] . PHP_EOL);
print("Execution time: " . round(($end - $start) * 1000, 2) . "ms" . PHP_EOL);
?>
