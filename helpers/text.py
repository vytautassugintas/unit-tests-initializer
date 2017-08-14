import definitions as js


def create_describe(content):
    return js.JASMINE_DESCRIBE + js.BRACKET_START + content + "\n" + js.BRACKET_END


def create_spy(spy_name):
    return js.JASMINE_SPY + js.BRACKET_START + spy_name + js.BRACKET_END


def create_mock(service_name: str):
    return js.MOCK + service_name.capitalize()