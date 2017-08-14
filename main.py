import definitions as js


def create_describe(content):
    return js.JASMINE_DESCRIBE + js.BRACKET_START + content + "\n" + js.BRACKET_END


def create_spy(spy_name):
    return js.JASMINE_SPY + js.BRACKET_START + spy_name + js.BRACKET_END


def read_file(path):
    functions_count = 0
    with open(path) as f:
        content = f.readlines()
    for line in content:
        if find_functions(line):
            functions_count = functions_count + 1
        print(line)
    print("functions count", functions_count)


def find_functions(content):
    return content.find(js.FUNCTION) != -1

read_file("./random.js")
