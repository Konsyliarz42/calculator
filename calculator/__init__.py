import logging
from .__main__ import calculate, make_correct

logging.basicConfig(
        format = '%(asctime)s | %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S',
        level = logging.DEBUG,
        handlers=[
            logging.FileHandler("debug.log", 'w', encoding='utf-8'),
        ]
    )

def simple_call(string_input: str, round_to=None):
    """Group functions to calculations.\n
    Return tuple with result and process calculation in string.\n
    The argument round_to isn't None type but intereger result will be rounded."""

    string_input = make_correct(string_input)
    result, string_output = calculate(string_input, round_to)

    return result, string_output