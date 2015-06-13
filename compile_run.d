#!/usr/bin/env rdmd
import std.stdio;
import std.getopt;
import std.process;

void main(string[] args)
{
    bool compile, run;
    bool sieve;

    //Get the args to find out which ones we should compile.
    auto projectsToCompile = getopt(args, std.getopt.config.bundling,
    "compile|c", &compile,
    "run|r", &run,
    "sieve",  &sieve);

    //Compile the selected tasks...
    if(compile)
    {
        if(sieve)
        {
            writeln("Compiling Sieves...");
            auto pid = spawnShell("./build-sieves",
                                    stdin, stdout, stderr, null, Config.none,
                                    "./sieve-of-eratosthenes");
            wait(pid);
        }
    }
    if(run)
    {
        if(sieve)
        {
            writeln("Running Sieves...");
            auto pid = spawnShell("./run-sieves",
                                    stdin, stdout, stderr, null, Config.none,
                                    "./sieve-of-eratosthenes");
            wait(pid);
        }
    }
    writeln("Done.");
}
