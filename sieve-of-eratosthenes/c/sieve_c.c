#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char const** argv)
{
    if (argc != 2)
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

    unsigned int max = atoi(argv[1]);
    unsigned int arraySize = max * sizeof(unsigned char);
    clock_t begin = clock();

    unsigned char *primes = malloc(arraySize);
    memset(primes, 0x01, arraySize);
    primes[0] = primes[1] = 0x00;

    unsigned int numPrimes = max - 2;
    int sqrtMax = (int) ceil(sqrt(max));
    for (unsigned int i = 0; i < sqrtMax; ++i)
    {
        if (primes[i])
        {
            unsigned int mult = i * i;
            while(mult < max)
            {
                if(primes[mult]) {
                    --numPrimes;
                    primes[mult] = 0x00;
                }
                mult += i;
            }
        }
    }

    clock_t end = clock();
    float duration = (((float)end - (float)begin) / 1000000.0F ) * 1000;
    printf("Number of primes: %i\n", numPrimes);
    printf("Execution time: %fms\n", duration);

    free(primes);

    return 0;
}
