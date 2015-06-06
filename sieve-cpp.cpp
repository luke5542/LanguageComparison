#include <vector>
#include <iostream>
#include <cstdlib>
#include <math.h>
#include <stdio.h>

int main(int argc, char const** argv)
{
    if (argc != 2)
    {
        return 1;
    }

    int max = std::atoi(argv[1]);
    int count = 0;

    std::vector<bool> primes (max, true);
    primes[0] = primes[1] = false;

    int sqrtMax = (int) ceil(sqrt(max));
    for (int i = 0; i < sqrtMax; ++i)
    {
        if (primes[i])
        {
            int mult = i << 1;
            count++;
            while(mult < max)
            {
                primes[mult] = false;
                mult += i;
            }
        }
    }

    int numPrimes = 0;
    for (int i = 0; i < max; ++i) {
        if (primes[i]) {
            numPrimes++;
        }
    }

    std::cout << numPrimes << std::endl;

    return 0;
}
