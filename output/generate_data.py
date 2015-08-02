import subprocess
import operator
import argparse

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


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--sieve", action="store",
                    default=10000000, type=int)
parser.add_argument("-r", "--runs", action="store",
                    default=1, type=int)
parser.add_argument("-c", "--compile", action="store_true")

args = parser.parse_args()

if args.compile:
    print("Compiling examples...")

    subprocess.call("./compile-all", cwd="..", stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL)

print("Running examples...")

data = []
avg_data = {}

for run in range(0, args.runs):

    if args.runs > 1:
        print("Run no. {}...".format(run + 1))

    output = subprocess.check_output(["./run-all", str(args.sieve)],
                                     cwd="..",
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

print("Generating HTML...")

# Create plot for average times
avg_data.update((key, value/args.runs) for key, value in avg_data.items())
sorted_data = sorted(avg_data.items(), key=operator.itemgetter(1))

languages = []

for language, time in sorted_data:
    languages.append(language)

# Generate data for average plot
_generate_tsv(["language", "time"], list(sorted_data), "avg")

with open("template_graph.html", 'r') as template_file:
    template = Template(template_file.read())

    with open("../benchmark.html", 'w') as output_file:
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

        output_file.write(template.safe_substitute(sieve_size=str(args.sieve)))

print("Done!")
