import subprocess

from string import Template

print("Compiling examples...")

subprocess.call("./compile-all", cwd="..", stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL)


print("Running examples...")

output = subprocess.check_output("./run-all",
                                 cwd="..",
                                 stderr=subprocess.DEVNULL) \
                                 .decode(encoding='UTF-8')
print(output)

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
        data[language] = time

languages = []
times = []

for language, time in data.items():
    languages.append(language)
    times.append(time)

print("Generating HTML...")

with open("template_graph.html", 'r') as template_file:
    template = Template(template_file.read())

    with open("../benchmark.html", 'w') as output_file:
        output_file.write(template.safe_substitute(languages=languages,
                          data=times))
