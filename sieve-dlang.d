module sieve;

import std.stdio;
import std.array;
import std.conv;
import std.math;

void main(char[][] args)
{
    int max = to!int(args[1]);

    bool[] primes = new bool[max];
    primes[2..max] = true;
    primes[0..2] = false;

    //Faze out all invalid primes.
    int sqrtMax = cast(int) ceil(sqrt(cast(float) max));
    foreach(int i; 0 .. sqrtMax)
    {
        if(primes[i])
        {
            int mult = i << 1;
            while(mult < max)
            {
                primes[mult] = false;
                mult += i;
            }
        }
    }

    int i = 0;
    foreach(b; primes)
    {
        if(b)
        {
            i++;
        }
    }

    writeln("Num Primes: ", i);
}
