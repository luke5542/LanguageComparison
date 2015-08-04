"""
Generates benchmark plots for all examples.

Script generates plots and places in HTML file located at:
`../benchmark.html`

Can be run with the following flags:
`-b` or `--build` - this builds all source code via the Makefiles
`-s` or `--sieve` - specifies the size of the sieve for Sieve of Eratosthenes
`-r` or `--runs` - specifies number of times to run each example
"""
import subprocess
import operator
import argparse
import os

from string import Template


def _generate_tsv(data_labels, data, name):
    with open(name + ".tsv", 'w') as data_file:
        line = ""
        for label in data_labels:
            if line is not "":
                line += '\t'
            line += label

        line += '\n'
        data_file.write(line)
        line = ""
        for data_set in data:
            for item in data_set:
                if line is not "":
                    line += '\t'
                line += str(item)

            line += '\n'
            data_file.write(line)
            line = ""


def _build(directory):
    os.chdir(os.path.join("./..", directory))
    subprocess.call(["make", "cleanall"])
    subprocess.call(["make", "buildall"])


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sieve", action="store",
                    default=10000000, type=int)
parser.add_argument("-r", "--runs", action="store",
                    default=1, type=int)
parser.add_argument("-b", "--build", action="store_true")

args = parser.parse_args()

example_dirs = [example_dir for example_dir in os.listdir("./..")
                if os.path.isdir(os.path.join("./..", example_dir))
                and example_dir not in [".git", "bin", "output"]]

if args.build:
    print("Building examples...")
    for directory in example_dirs:
        _build(directory)

benchmarks = ""
for example_dir in example_dirs:
    print("Running ", example_dir, " examples...")
    example_name = example_dir.split('-')[0]

    data = []
    avg_data = {}

    for run in range(0, args.runs):

        if args.runs > 1:
            print("Run no. {}...".format(run + 1))
        os.chdir(os.path.join("./..", example_dir))
        output = subprocess \
            .check_output(["make", "SIEVESIZE=\""+str(args.sieve)+"\"",
                           "runall"],
                          stderr=subprocess.DEVNULL) \
            .decode(encoding='UTF-8')

        print("Extracting results...")

        lines = output.split('\n')

        run_data = {}
        language = None
        time = None

        for line in lines:
            if "Running" in line:
                tokens = line.split(' ')
                language = tokens[1]
                time = None

            if "Execution" in line:
                tokens = line.split(' ')
                time = tokens[2][:-2]

            if language is not None and time is not None:
                run_data[language] = float(time)

        data.append(run_data)
        for language, time in run_data.items():
            avg_data[language] = avg_data.get(language, 0) + (time / args.runs)

    os.chdir(os.path.join("../output"))
    # Create plot for average times
    avg_data.update((key, value/args.runs) for key, value in avg_data.items())
    sorted_data = sorted(avg_data.items(), key=operator.itemgetter(1))

    languages = []

    for language, time in sorted_data:
        languages.append(language)

    # Generate data for average plot
    _generate_tsv(["language", "time"],
                  list(sorted_data), example_name + "Avg")

    with open("template_graph.html", 'r') as template_file:
        template = Template(template_file.read())

        # Create plot showing results for each run if more than 1
        if args.runs > 1:
            labels = ["run"] + languages
            all_data = []

            with open("mult_runs_template.html", 'r') as runs_template_file:
                all_runs = runs_template_file.read()
                datasets = ""

                for num, run in enumerate(data):
                    run_data = ["Run " + str((num + 1))]
                    for language in languages:
                        run_data.append(run[language])

                    all_data.append(run_data)

                template = Template(template
                                    .safe_substitute(multiple_runs=all_runs))

            _generate_tsv(labels, all_data, "all_runs")
        else:
            template = Template(template.safe_substitute(multiple_runs=''))

        # Add this benchmark set of plots to the rest
        benchmarks += template.safe_substitute(example=example_name)

print("Generating HTML...")

# Construct main HTML file from individual benchmark plots
with open("main_template.html", 'r') as template_file:
    template = Template(template_file.read())
    with open("../benchmark.html", 'w') as output_file:
        output_file.write(template.safe_substitute(benchmarks=benchmarks))

print("Done!")
