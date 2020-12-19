from .counting import calculation, convert_to_list, get_parentheses, get_first_calculation
from . import log

def make_correct(string_input: str):
    """Make corrects to string_input and return new version.\n
    Corrects:
    - Remove spaces on first and last positions.
    - Remove equal's mark on end.
    - Add multiplication's marks before parentheses."""

    marks = '(^√∛∜*/+- '
    positions = list()
    change = False

    # Remove spaces
    if string_input[0] == ' ' or string_input[-1] == ' ':
        change = True
        string_input = string_input.strip()
        log.debug("Remove spaces on first and last positions")

    # Remove equal's mark
    if string_input[-1] == '=':
        change = True
        string_input = string_input[:-1]
        log.debug("Remove equal's mark on end")

    # Add star before parentheses
    for i in range(len(string_input)):
        if string_input[i] == '(' and i > 0:
            if string_input[i - 1] not in marks:
                string_input = string_input[:i] + '*' + string_input[i:]
                positions.append(i)
    
    if positions:
        change = True
        log.debug(f"Add multiplication's marks in positions: {positions}")

    # Add info to log
    if change:
        log.debug(f"Continue with new input: '{string_input}'\n")

    return string_input


def main(string_input: str):
    """Main function of calculator.\n
    The function return tuple with result of the calculations and string of the process' calculations."""

    string_calculation = str()
    
    # Repeat if find parentheses
    while string_input.count('(') != 0:
        parentheses = get_parentheses(string_input)
        parentheses_result, parentheses_calculation = main(parentheses)
        string_calculation += parentheses_calculation + '\n\n'
        string_input = string_input.replace(f'({parentheses})', str(parentheses_result))
        log.debug(f"Replace '({parentheses})' {parentheses_result}, continue with new input: '{string_input}'")

    list_input = convert_to_list(string_input)
    
    while len(list_input) > 1:
        # Add calculation to output string
        string_calculation += ' '.join([str(element) for element in list_input]) + ' =\n'

        # Start calculating
        operation = get_first_calculation(list_input)
        operation_in_list = [index for index in range(len(list_input)) if tuple(list_input[index: index + len(operation)]) == operation][0]
        result = calculation(operation)

        list_input.insert(operation_in_list, result)

        # Remove operation from list_input
        for index in range(operation_in_list + len(operation), operation_in_list, -1):
            list_input.pop(index)

    # Add final result to output string
    string_calculation += '-'*8 + '\n= ' + str(list_input[0])

    log.debug(f"Final result: {list_input[0]}\n")
    return list_input[0], string_calculation


#================================================================
if __name__ == "__main__":
    string_input = "-6 + -7.8"
    string_input = make_correct(string_input)

    #print(get_parentheses(string_input))

    print(string_input, '= ?\n')
    print(main(string_input)[1])