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
        int foundPrimes = max - 2;
        int sqrtMax = (int) Math.ceil(Math.sqrt(max));
        for(int i = 0; i < sqrtMax; i++)
        {
            if(primes[i])
            {
                int mult = i*2;
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

        System.out.println("Number of primes: " + foundPrimes);
    }
}
