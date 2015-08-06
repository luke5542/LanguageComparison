import java.util.ArrayList;
import java.text.DecimalFormat;
import java.math.RoundingMode;

public class sieve_java
{
    static void primes(int max)
    {
        DecimalFormat df = new DecimalFormat("#.###"); df.setRoundingMode(RoundingMode.CEILING);
        long startTime = System.nanoTime();

        boolean[] primes = new boolean[max];

        primes[0] = true;
        primes[1] = true;

        //Faze out all invalid primes.
        int foundPrimes = max - 2;
        int sqrtMax = (int) Math.ceil(Math.sqrt(max));
        for(int i = 0; i < sqrtMax; i++)
        {
            if(!primes[i])
            {
                int mult = i*i;
                while(mult < max)
                {
                    if(!primes[mult]) {
                        foundPrimes--;
                        primes[mult] = true;
                    }
                    mult += i;
                }
            }
        }

        long endTime = System.nanoTime();

        System.out.println("Number of primes: " + foundPrimes);
        System.out.println("Execution time: " +
          df.format((endTime - startTime)/1e6) + "ms");
    }

    public static void main(String[] args)
    {

        try {
            int max = Integer.parseInt(args[0]);
            primes(max);
        }
        catch(NumberFormatException | ArrayIndexOutOfBoundsException e) {
            System.exit(1);
        }
    }
}
