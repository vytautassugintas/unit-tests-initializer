import definitions as js


def read_file(path):
    functions_count = 0
    with open(path) as f:
        content = f.readlines()
    for line in content:
        if find_functions(line):
            functions_count = functions_count + 1
        print(line)
    print("functions count", functions_count)


def write_file(path, file_name):
    return ""


def find_functions(content):
    return content.find(js.FUNCTION) != -1

read_file("./random.js")
