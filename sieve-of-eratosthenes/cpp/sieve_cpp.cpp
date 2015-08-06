#include <vector>
#include <iostream>
#include <cstdlib>
#include <math.h>
#include <stdio.h>
#include <ctype.h>
#include <chrono>
using namespace std;

int main(int argc, char const** argv)
{
    if(argc != 2)
    {
        return 1;
    }

    for (int pos = 0; pos < strlen(argv[1]); pos++)
    {
        if(!isdigit(argv[1][pos]))
        {
          return 1;
        }
    }

    int max = atoi(argv[1]);

    auto begin = chrono::high_resolution_clock::now();
    vector<bool> primes (max, true);
    primes[0] = primes[1] = false;

    int numPrimes = max - 2;

    int sqrtMax = (int) ceil(sqrt(max));
    for (int i = 0; i < sqrtMax; ++i)
    {
        if (primes[i])
        {
            int mult = i * i;
            while(mult < max)
            {
                if(primes[mult]) {
                    --numPrimes;
                    primes[mult] = false;
                }
                mult += i;
            }
        }
    }

    auto end = chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count();
    cout << "Number of primes: " << numPrimes << endl;
    cout << "Execution time: " << duration << "ms" << endl;

    return 0;
}
