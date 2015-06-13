#!/usr/bin/env rdmd
import std.stdio;
import std.getopt;
import std.process;
import std.conv;

void main(string[] args)
{
    bool compile, run, help;
    bool sieve;

    //Provide a default
    uint sieveSize = 10_000_000;

    //Get the args to find out which ones we should compile.
    auto projectsToCompile = getopt(args, std.getopt.config.bundling,
    "help|h", &help,
    "compile|c", &compile,
    "run|r", &run,
    "sieveSize", &sieveSize,
    "sieve",  &sieve);

    if(help)
    {
        writeln(helpText);
    }

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
            auto pid = spawnShell("./run-sieves " ~ to!string(sieveSize),
                                    stdin, stdout, stderr, null, Config.none,
                                    "./sieve-of-eratosthenes");
            wait(pid);
        }
    }
    writeln("Done.");
}

string helpText =
`--help or -h:
    Print this help text.
--compile or -c:
    Compile the selected tasks.
--run or -r:
    Run the selected tasks.
--sieve:
    Select the sieve task to run/compile.
    Optionally pass --sieveSize=<int> to specify the window to run the sieve over (0-<int>)`;
