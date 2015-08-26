open Core.Std

let main =
  if Array.length Sys.argv < 2 then begin
    print_endline "Error: missing argument (number)";
    exit 1
  end;

  let max = int_of_string Sys.argv.(1) in
  let start = Time.now () in

  let primes = Array.create max true in
  let prime_count = ref (max - 2) in

  primes.(0) <- false;
  if max > 1 then primes.(1) <- false;

  for i = 0 to max |! Float.of_int |! sqrt |! Float.to_int do
    if primes.(i) then
      let mult = ref (i*i) in
      while !mult < max do
        if primes.(!mult) then begin
          prime_count := !prime_count - 1;
          primes.(!mult) <- false
        end;
        mult := !mult + i
      done
  done;

  let dur = Time.(diff (now ()) start) in

  Printf.printf "Number of primes: %i\n" !prime_count;
  Printf.printf "Execution time: %fms\n" (Time.Span.to_ms dur)
