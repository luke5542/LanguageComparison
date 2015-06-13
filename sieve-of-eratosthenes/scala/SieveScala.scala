import Math._
import Array._

object SieveScala {
  def main(args: Array[String]) {
    var max = Integer.parseInt(args(0));

    val start = System.currentTimeMillis;

    var primes = tabulate[Boolean](max)((i) => i > 1);

    //Faze out all invalid primes.
    var foundPrimes = max - 2;
    var sqrtMax = Math.ceil(Math.sqrt(max)).toInt;
    for(i <- 0 to sqrtMax-1)
    {
        if(primes(i))
        {
            var mult = i*i;
            while(mult < max)
            {
                if(primes(mult)) {
                    foundPrimes -= 1;
                    primes(mult) = false;
                }
                mult += i;
            }
        }
    }

    var end = System.currentTimeMillis;

    println("Num Primes: " + foundPrimes);
    println("Execution time: " + (end - start) + "ms");
  }
}
