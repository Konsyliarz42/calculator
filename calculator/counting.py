import re, logging

log = logging.getLogger('log')

remove_comma = lambda arg: arg if arg%1 else int(arg)   #float(2.0) => int(2), float(2.5) => float(2.5)

def get_parentheses(string_input: str):
    """Return first parentheses or empty string."""

    parentheses = string_input[string_input.find('(') + 1: string_input.rfind(')')]

    if parentheses.count('(') > 0:
        if parentheses.index('(') > parentheses.index(')'):
            parentheses = parentheses[: parentheses.find(')')]
        else:
            parentheses = parentheses[parentheses.find('(') + 1: parentheses.find(')')]

    log.debug(f"Detect parentheses: '({parentheses})'")
    return parentheses


def convert_to_list(string_input: str):
    """Return list of the numbers and marks."""

    _numbers = r"[-]?(\d+([.]\d+)?)"
    _marks = r"[√∛∜^*/+-]"

    regular = re.compile(f"({_numbers}|{_marks})")
    founded = [x[0] for x in re.findall(regular, string_input)]

    # Change numbers from string to float type
    for i in range(len(founded)):
        try:
            founded[i] = float(founded[i])
            founded[i] = remove_comma(founded[i])
        except ValueError:
            pass

    log.debug(f"The function generate list of elements: {founded}")
    return founded


def get_first_calculation(list_input: list):
    """Return calculation in tuple type, which should be first.\n
    If the function finds nothing return None.\n
    Calculation's order:
    1. ^ or √, ∛, ∜
    2. * or /
    3. + or -"""

    order = ['^√∛∜', '*/', '+-']

    for marks in order:
        for mark in list_input:
            if str(mark) in marks:
                index = list_input.index(mark)

                if mark in '√∛∜':
                    operation = tuple(list_input[index: index + 2])
                else:
                    operation = tuple(list_input[index - 1: index + 2])

                log.debug(f"Next calculation: {operation}")
                return operation

    return None


def calculation(tuple_input: tuple, round_to=None):
    """Return result of the calculation."""

    if len(tuple_input) == 2:
        mark = tuple_input[0]
        number_first = tuple_input[1]
        number_second = 2 + '√∛∜'.index(mark)
    else:
        mark = tuple_input[1]
        number_first = tuple_input[0]
        number_second = tuple_input[2]

    result = None

    # Order first
    if mark == '^':
        result = number_first**number_second
    elif mark in '√∛∜':
        result = number_first**(1/number_second)

    # Order second
    elif mark == '*':
        result = number_first*number_second
    elif mark == '/':
        result = number_first/number_second

    # Order Third 
    elif mark == '+':
        result = number_first + number_second
    elif mark == '-':
        result = number_first - number_second

    # Round
    if round_to != None:
        result = round(result, round_to)

    return remove_comma(result)
