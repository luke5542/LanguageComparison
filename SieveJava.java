import java.util.ArrayList;

public class SieveJava
{

    public static void main(String[] args)
    {

        int max = Integer.parseInt(args[0]);

        boolean[] primes = new boolean[max];
        for(int i = 0; i < max; i++)
        {
            primes[i] = true;
        }

        primes[0] = false;
        primes[1] = false;
        primes[2] = true;

        //Faze out all invalid primes.
        int sqrtMax = (int) Math.ceil(Math.sqrt(max));
        for(int i = 0; i < sqrtMax; i++)
        {
            if(primes[i])
            {
                int mult = i*2;
                while(mult < max)
                {
                    primes[mult] = false;
                    mult += i;
                }
            }
        }

        //Grab the list of valid primes
        int foundPrimes = 0;
        for(int i = 0; i < max; i++)
        {
            if(primes[i])
            {
                foundPrimes++;
            }
        }
        System.out.println("Num Primes: " + foundPrimes);
    }
}
