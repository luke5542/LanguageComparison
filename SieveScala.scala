import Math._
import Array._

object SieveScala {
  def main(args: Array[String]) {
    var max = Integer.parseInt(args(0));

    var primes = tabulate[Boolean](max)((i) => i > 1);

    //Faze out all invalid primes.
    var sqrtMax = Math.ceil(Math.sqrt(max)).toInt;
    for(i <- 0 to sqrtMax-1)
    {
        if(primes(i))
        {
            var mult = i*2;
            while(mult < max)
            {
                primes(mult) = false;
                mult += i;
            }
        }
    }

    //Grab the list of valid primes
    var foundPrimes = 0;
    for(i <- 0 to max-1)
    {
        if(primes(i))
        {
            foundPrimes += 1;
        }
    }
    println("Num Primes: " + foundPrimes);
  }

  /*def findPrimes(max: Int) {
      var primes = tabulate[Boolean](max)((i) => i > 2)
  }*/
}
