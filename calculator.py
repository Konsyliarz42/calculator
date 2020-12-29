import PySimpleGUI as sg
import json
from calculator import simple_call
from calculator.counting import convert_to_list

DEFAULT_LANGUAGE = 'ENGLISH'
AUTHORS = ', '.join(["Tomasz Kordiak"])
VERSION = '4.0'

SIZE_WINDOW = (16*32, 16*15)
SIZE_BUTTONS = (18, 1) # Auto: None
SIZE_BUTTONS_NUMBERS = (3, 1)

ROUND_LIST = [None] + [x for x in range(9)]

# Create window
layout = [
    # Main rowpy 
    [
        sg.Text("Calculations:", size=(48, 1), justification='left'),
        sg.Text("Round to:"),
        sg.Spin(ROUND_LIST, key='round_to', size=(8, 1))
    ],
    [
        sg.InputText(key='string_input', size=(48, 2)),
        sg.Button('Calculate', size=SIZE_BUTTONS)
    ],

    # Input and output row
    [
        sg.Multiline(key='string_output', size=(34, 8), disabled=True, background_color='LightSteelBlue'),
        sg.Frame(title='', layout=[
            [sg.Button(x, size=SIZE_BUTTONS_NUMBERS, key=f'_{x}') for x in range(7, 10)],
            [sg.Button(x, size=SIZE_BUTTONS_NUMBERS, key=f'_{x}') for x in range(4, 7)],
            [sg.Button(x, size=SIZE_BUTTONS_NUMBERS, key=f'_{x}') for x in range(1, 4)],
            [
                sg.Button('.', size=SIZE_BUTTONS_NUMBERS, key='_.'),
                sg.Button('0', size=SIZE_BUTTONS_NUMBERS, key='_0'),
                sg.Button('+/-', size=SIZE_BUTTONS_NUMBERS, key='_+/-')
            ]
        ]),
        sg.Frame(title='', layout=[
            [
                sg.Button('xⁿ', size=SIZE_BUTTONS_NUMBERS, key='_^'),
                sg.Button('×', size=SIZE_BUTTONS_NUMBERS, key='_*')
            ],
            [
                sg.Button('√', size=SIZE_BUTTONS_NUMBERS, key='_√'),
                sg.Button('÷', size=SIZE_BUTTONS_NUMBERS, key='_/')
            ],
            [
                sg.Button('∛', size=SIZE_BUTTONS_NUMBERS, key='_∛'),
                sg.Button('+', size=SIZE_BUTTONS_NUMBERS, key='_ + ')
            ],
            [
                sg.Button('∜', size=SIZE_BUTTONS_NUMBERS, key='_∜'),
                sg.Button('-', size=SIZE_BUTTONS_NUMBERS, key='_ - ')
            ]
        ])
    ],

    # End row
    [sg.HorizontalSeparator()],
    [
        sg.Text(key='author', text='by ' + AUTHORS),
        sg.Text(key='version', text='v' + VERSION, size=(64, 1), justification='right')
    ],
]

window = sg.Window('Calculator', layout,
    return_keyboard_events = True,
    size = SIZE_WINDOW,
    font = ('Cambria', 10),
    text_justification='center'
)

# Run
while True:
    event, values = window.read()

    # Exit
    if event == sg.WINDOW_CLOSED:
        break

    # Print using buttons
    if event[0] == '_' and len(event) > 1:
        add_value = event[1:]
        
        if add_value == '+/-':
            list_input = convert_to_list(values['string_input'].replace(',', '.'))
            last_number = None
            number_position = -1

            if type(list_input[-1]) in (float, int):
                last_number = list_input[-1] * -1

                if len(list_input) > 1:
                    number_position = values['string_input'].rfind(str(list_input[-2]))

                    if values['string_input'][number_position + 1] == ' ':
                        number_position += 1

                x = values['string_input'][:number_position + 1] + str(last_number)
                window['string_input'].update(x)

        else:
            window['string_input'].update(values['string_input'] + add_value)

    # Calculate if click button or press enter
    if event == 'Calculate' or event == '\r':
        try:
            result, string_output = simple_call(
                string_input = values['string_input'],
                round_to = values['round_to']
            )
            window['string_output'].update(string_output)
        except (TypeError, IndexError, ZeroDivisionError):
            window['string_output'].update('False')
        finally:
            event = 'Enter:13'

    print("event:", event, "| values:", values)

# Close window
window.close()