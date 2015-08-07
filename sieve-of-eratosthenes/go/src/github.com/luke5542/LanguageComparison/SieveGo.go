package main

import (
	"fmt"
	"math"
	"os"
	"strconv"

	"github.com/fatih/stopwatch"
)

func main() {
	// Check we received at least one argument
	if len(os.Args) < 2 {
		os.Exit(1)
	}

	// Check we can convert the first argument to int successfully
	max, err := strconv.Atoi(os.Args[1])
	if err != nil {
		os.Exit(1)
	}

	// Now find all the primes
	findPrimes(max)
}

func findPrimes(max int) {
	primes := make([]bool, max, max)

	primes[0] = true
	primes[1] = true

	// Get rid of all invalid primes
	foundPrimes := max - 2
	sqrtMax := int(math.Sqrt(float64(max)))

	s := stopwatch.Start(0)
	for i := 1; i < sqrtMax; i++ {
		if !primes[i] {
			mult := i * i
			for mult < max {
				if !primes[mult] {
					foundPrimes--
					primes[mult] = true
				}
				mult = mult + i
			}
		}
	}
	s.Stop()

	fmt.Printf("Number of primes found: %v\n", foundPrimes)
	fmt.Printf("Execution time: %vms\n", s.ElapsedTime().Seconds()*1000)
}
