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
        for data_set in data:
            line = ""
            for item in data_set:
                if line is not "":
                    line += '\t'
                line += str(item)

            line += '\n'
            data_file.write(line)


def _build(directory):
    os.chdir(os.path.join("./..", directory))
    subprocess.call(["make", "cleanall"])
    subprocess.call(["make", "buildall"])


def _extract_results(output):
    run_data = {}
    language = None
    time = None

    for line in output:
        if "Running" in line:
            language = line.split(' ')[1]
            time = None

        if "Execution time" in line:
            time = line.split(' ')[2][:-2]

        if language is not None and time is not None:
            run_data[language] = float(time)

    return run_data


def _benchmark_run(dir_name, runs, settings):
    print("Running", dir_name, "examples...")
    example_name = dir_name.split('-')[0]

    data = []
    avg_data = {}

    for run in range(0, runs):

        if runs > 1:
            print("Run no. {}...".format(run + 1))

        os.chdir(os.path.join("./..", dir_name))

        if dir_name == "sieve-of-eratosthenes":
            output = subprocess \
                .check_output(["make",
                               "SIEVESIZE=\"" + settings["SIEVESIZE"] + "\"",
                               "runall"],
                              stderr=subprocess.DEVNULL) \
                .decode(encoding='UTF-8')
        else:
            output = subprocess \
                .check_output(["make", "runall"],
                              stderr=subprocess.DEVNULL) \
                .decode(encoding='UTF-8')

        print("Extracting results...")

        run_data = _extract_results(output.split('\n'))

        data.append(run_data)
        for language, time in run_data.items():
            avg_data[language] = avg_data.get(language, 0) + (time / args.runs)

    os.chdir(os.path.join("../output"))

    # Create plot for average times
    sorted_data = sorted(avg_data.items(), key=operator.itemgetter(1))

    languages = []

    for language, time in sorted_data:
        languages.append(language)

    # Generate data for average plot
    _generate_tsv(["language", "time"],
                  list(sorted_data), example_name + "_avg")

    with open("template_graph.html", 'r') as template_file:
        template = Template(template_file.read())

        # Create plot showing results for each run if more than 1
        if args.runs > 1:
            labels = ["run"] + languages
            all_data = []

            with open("mult_runs_template.html", 'r') as runs_template_file:
                all_runs_template = Template(runs_template_file.read())
                all_runs = all_runs_template \
                    .safe_substitute(example=example_name)

                for num, run in enumerate(data):
                    run_data = ["Run " + str((num + 1))]
                    for language in languages:
                        run_data.append(run[language])

                    all_data.append(run_data)

                template = Template(template
                                    .safe_substitute(multiple_runs=all_runs))

            _generate_tsv(labels, all_data, example_name + "_all_runs")
        else:
            template = Template(template.safe_substitute(multiple_runs=''))

        return template.safe_substitute(example=example_name)


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

benchmarks = []

for example_dir in example_dirs:
    benchmarks.append(_benchmark_run(example_dir, args.runs,
                      {"SIEVESIZE": str(args.sieve)}))

print("Generating HTML...")
benchmarks = '\n'.join(benchmarks)

# Construct main HTML file from individual benchmark plots
with open("main_template.html", 'r') as template_file:
    template = Template(template_file.read())
    with open("../benchmark.html", 'w') as output_file:
        output_file.write(template.safe_substitute(benchmarks=benchmarks))

print("Done!")
