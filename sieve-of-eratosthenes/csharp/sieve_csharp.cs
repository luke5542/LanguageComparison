using System;
using System.Diagnostics;

public class PrimeSieve
{
    static void primes(int max)
    {
        var sw = Stopwatch.StartNew();

        var primes = new bool[max];

        primes[0] = true;
        primes[1] = true;

        var foundPrimes = max - 2;
        var sqrtMax = (int)Math.Ceiling(Math.Sqrt(max));

        for (var i = 0; i < sqrtMax; i++)
        {
            if (primes[i]) continue;
            var mult = i * i;
            while (mult < max)
            {
                if (!primes[mult])
                {
                    foundPrimes--;
                    primes[mult] = true;
                }
                mult += i;
            }
        }

        sw.Stop();
        Console.WriteLine("Number of primes: {0}", foundPrimes);
        Console.WriteLine("Execution time: {0}ms", sw.ElapsedMilliseconds);
    }

    public static int Main(string[] args)
    {
        try {
            var max = int.Parse(args[0]);
            primes(max);
            return 0;
        }
        catch (FormatException) {
            return 1;
        }
        catch (OverflowException) {
            return 1;
        }
        catch (IndexOutOfRangeException) {
            return 1;
        }
    }
}
