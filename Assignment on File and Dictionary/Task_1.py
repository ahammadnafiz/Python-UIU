def read_statements(file_path):

    all_lines = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line != "-":
                all_lines.append(line)

    names = []
    for i in range(0, len(all_lines), 3):
        names.append(all_lines[i])

    for i in range(len(names)):
        all_lines.remove(names[i])

    alibi = []
    behavior = []

    for i in range(len(all_lines)):
        if i % 2 == 0:
            alibi.append(all_lines[i])
        else:
            behavior.append(all_lines[i])

    sataments_list = []
    for k, v in zip(alibi, behavior):
        sataments_list.append({"alibi": k, "behavior": v})

    sataments_dict = dict(zip(names, sataments_list))

    return sataments_dict


def find_culprit(sataments_dict):

    statement = input()
    culprit = ""
    for key, value in sataments_dict.items():
        for v in value.values():
            if statement in v:
                culprit += f"{key} is the culprit because {v}"

    return culprit


def write_culprit_to_file(culprit, output_file):

    with open(output_file, "w") as c:
        c.write(culprit)

    with open(output_file, "r") as cr:
        for line in cr:
            print(line.strip())


def main():

    input_file = "statements.txt"
    output_file = "culprit.txt"

    suspects = read_statements(input_file)

    culprit_name = find_culprit(suspects)

    write_culprit_to_file(culprit_name, output_file)


if __name__ == "__main__":
    main()
