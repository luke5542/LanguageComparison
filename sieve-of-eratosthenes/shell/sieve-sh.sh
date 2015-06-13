#!/bin/bash
# Based on version found at rosettacode.org

function sieve {
	typeset num=2 square max=$1
	while (( num <= max )); do
		primes[$num]=$num
		(( num++ ))
	done

	num=2
	while (( square = num * num, square <= max )); do
		if [[ -n ${primes[$num]} ]]; then
			while (( square <= max )); do
        unset primes[$square]
				(( square += num ))
			done
		fi
		(( num++ ))
	done

  echo "Number of primes:" ${#primes[*]}
}

$@
