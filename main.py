FUNCTION = "function"
FUNCTION_ARROW = "=>"
BLOCK = "{}"
BLOCK_START = "{"
BLOCK_END = "}"
BRACKETS = "()"
BRACKET_START = "("
BRACKET_END = ")"
MOCK = "mock"
JASMINE_DESCRIBE = "describe"
JASMINE_IT = "it"
JASMINE_SPY = "jasmine.createSpy"


def create_describe(content):
    return JASMINE_DESCRIBE + BRACKET_START + content + "\n" + BRACKET_END


def create_spy(spy_name):
    return JASMINE_SPY + BRACKET_START + spy_name + BRACKET_END


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
    return content.find(FUNCTION) != -1

read_file("./random.js")
