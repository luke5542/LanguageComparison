import subprocess
import operator
import argparse
import random

from string import Template

# Kelly's colour series
colours = [(255, 179, 0),
           (128, 62, 117),
           (255, 104, 0),
           (166, 189, 215),
           (193, 0, 32),
           (206, 162, 98),
           (129, 112, 102),
           (0, 125, 52),
           (246, 118, 142),
           (0, 83, 138),
           (255, 122, 92),
           (83, 55, 122),
           (255, 142, 0),
           (179, 40, 81),
           (244, 200, 0),
           (127, 24, 13),
           (147, 170, 0),
           (89, 51, 21),
           (241, 58, 19),
           (35, 44, 22)]


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
            for data_line in data_set:
                for item in data_line:
                    if line is not "":
                        line += '\t'
                    line += str(item)

                line += '\n'
                data_file.write(line)
                line = ""


def _set_colours(base_colour):
    r, g, b = base_colour
    fill = "rgba({}, {}, {}, 0.2)".format(r, g, b)
    stroke = "rgba({}, {}, {}, 1)".format(r, g, b)
    point = "rgba({}, {}, {}, 1)".format(r, g, b)
    pt_stroke_colour = "#fff"
    pt_hl_fill = "#fff"
    pt_hl_stroke = "rgba({}, {}, {}, 1)".format(r, g, b)
    return [fill, stroke, point, pt_stroke_colour, pt_hl_fill, pt_hl_stroke]


def _dataset_str(run, colours, data):
    return r"""{{
  label: "{}",
  fillColor: "{}",
  strokeColor: "{}",
  pointColor: "{}",
  pointStrokeColor: "{}",
  pointHighlightFill: "{}",
  pointHighlightStroke: "{}",
  data: {}
 }},""".format(language, colours[0], colours[1],
               colours[2], colours[3], colours[4],
               colours[5], data)


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

run_data = []
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

    data = {}
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
            data[language] = float(time)

    run_data.append(data)
    for language, time in data.items():
        avg_data[language] = avg_data.get(language, 0) + time

print("Generating HTML...")

# Create plot for average times
avg_data.update((key, value/args.runs) for key, value in avg_data.items())
sorted_data = sorted(avg_data.items(), key=operator.itemgetter(1))

languages = []
times = []

for language, time in sorted_data:
    languages.append(language)
    times.append(time)

# Generate data for average plot
_generate_tsv(["language", "time"], [list(sorted_data)], "avg")

with open("template_graph.html", 'r') as template_file:
    template = Template(template_file.read())

    with open("../benchmark.html", 'w') as output_file:
        # Create plot showing results for each run if more than 1
        if args.runs > 1:
            colour_list = random.sample(colours, len(languages))

            with open("mult_runs_template.html", 'r') as runs_template_file:
                all_template = Template(runs_template_file.read())
                datasets = ""

                for lang_id, language in enumerate(languages):
                    data = []
                    for run in run_data:
                        data.append(run[language])

                    datasets += _dataset_str(language,
                                             _set_colours(
                                                colour_list[lang_id]),
                                             data)

                runs = ['Run {0}'.format(run + 1)
                        for run in list(range(0, args.runs))]

                all_runs = all_template.safe_substitute(datasets=datasets,
                                                        runs=runs)
                template = Template(template
                                    .safe_substitute(multiple_runs=all_runs))

        else:
            template = Template(template.safe_substitute(multiple_runs=''))

        output_file.write(template.safe_substitute(sieve_size=str(args.sieve)))

print("Done!")
