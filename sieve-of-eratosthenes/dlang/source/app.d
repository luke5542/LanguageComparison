module sieve;

import std.stdio;
import std.array;
import std.conv;
import std.math;
import std.datetime;
import std.c.stdlib;

void main(char[][] args)
{
    int max;
    try
    {
        max = to!int(args[1]);
    }
    catch(Exception e)
    {
        exit(1);
    }

    StopWatch sw;
    sw.start();

    bool[] primes = new bool[max];
    primes[2..max] = true;
    primes[0..2] = false;

    int primeCount = max - 2;
    //Faze out all invalid primes.
    int sqrtMax = cast(int) ceil(sqrt(cast(float) max));
    foreach(int i; 0 .. sqrtMax)
    {
        if(primes[i])
        {
            int mult = i * i;
            while(mult < max)
            {
                if(primes[mult]) {
                    --primeCount;
                    primes[mult] = false;
                }
                mult += i;
            }
        }
    }
    auto time = sw.peek().msecs;

    writeln("Number of primes: ", primeCount);
    writeln("Execution time: ", time, "ms");
}
