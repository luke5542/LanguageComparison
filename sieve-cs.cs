using System;
using System.Diagnostics;

public class PrimeSieve
{
    public static void Main(String[] args)
    {
        var max = int.Parse(args[0]);
        Console.WriteLine(max);

        var sw = Stopwatch.StartNew();

        var primes = new bool[max];
        for (var i = 0; i < max; i++) 
        {
            primes[i] = true;
        }

        primes[0] = false;
        primes[1] = false;
        primes[2] = true;

        var foundPrimes = max - 2;
        var sqrtMax = (int) Math.Ceiling(Math.Sqrt(max));
        for(int i = 0; i < sqrtMax; i++)
        {
            if(primes[i])
            {
                int mult = i*i;
                while(mult < max)
                {
                    if(primes[mult]) {
                        foundPrimes--;
                        primes[mult] = false;
                    }
                    mult += i;
                }
            }
        }

        sw.Stop();
        Console.WriteLine("Number of primes: {0}", foundPrimes);
        Console.WriteLine("Execution time: {0}msec", sw.ElapsedMilliseconds);
    }
}