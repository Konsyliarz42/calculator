import PySimpleGUI as sg
import json
from calculator import simple_call

DEFAULT_LANGUAGE = 'ENGLISH'
AUTHORS = ', '.join(["Tomasz Kordiak"])
VERSION = '1.0'

SIZE_WINDOW = (16*32, 16*15)
SIZE_BUTTONS = (16, 1) # Auto: None
SIZE_BUTTONS_NUMBERS = (3, 1)

ROUND_LIST = [None] + [x for x in range(9)]

# Create window
layout = [
    # Main row
    [
        sg.Text("Calculations:", size=(42, 1)),
        sg.Text("Round to:"),
        sg.Spin(ROUND_LIST, key='round_to', size=(8, 1))
    ],
    [
        sg.InputText(key='string_input', size=(48, 1)),
        sg.Button('Calculate', size=SIZE_BUTTONS)
    ],

    # Input and output row
    [
        sg.Multiline(key='string_output', size=(32, 8), disabled=True, background_color='LightSteelBlue'),
        sg.Frame(title='', layout=[
            [sg.Button(x, size=SIZE_BUTTONS_NUMBERS, key=f'_{x}') for x in range(7, 10)],
            [sg.Button(x, size=SIZE_BUTTONS_NUMBERS, key=f'_{x}') for x in range(4, 7)],
            [sg.Button(x, size=SIZE_BUTTONS_NUMBERS, key=f'_{x}') for x in range(1, 4)],
            [
                sg.Button('.', size=SIZE_BUTTONS_NUMBERS, key='_.'),
                sg.Button('0', size=SIZE_BUTTONS_NUMBERS, key='_0'),
                sg.Button('+/-', size=SIZE_BUTTONS_NUMBERS, key='+/-')
            ]
        ]),
        sg.Frame(title='', layout=[
            [sg.Button('^', size=SIZE_BUTTONS_NUMBERS, key='_^'), sg.Button('*', size=SIZE_BUTTONS_NUMBERS, key='_ * ')],
            [sg.Button(u'\N{SQUARE ROOT}', size=SIZE_BUTTONS_NUMBERS, key=u'_\N{SQUARE ROOT}'), sg.Button('/', size=SIZE_BUTTONS_NUMBERS, key='_ / ')],
            [sg.Button(u'\N{CUBE ROOT}', size=SIZE_BUTTONS_NUMBERS, key=u'_\N{CUBE ROOT}'), sg.Button('+', size=SIZE_BUTTONS_NUMBERS, key='_ + ')],
            [sg.Button(u'\N{FOURTH ROOT}', size=SIZE_BUTTONS_NUMBERS, key=u'_\N{FOURTH ROOT}'), sg.Button('-', size=SIZE_BUTTONS_NUMBERS, key='_ - ')]
        ])
    ],

    # End row
    [
        sg.HorizontalSeparator()
    ],
    [
        sg.Text(key='author', text='by ' + AUTHORS),
        sg.Text(key='version', text='v' + VERSION, size=SIZE_WINDOW, justification='right')
    ],
]

window = sg.Window('Calculator', layout, return_keyboard_events=True, size=SIZE_WINDOW)

# Run
while True:
    event, values = window.read()
    print("event:", event, "| values:", values)

    # Exit
    if event == sg.WINDOW_CLOSED:
        break

    # Print using buttons
    if (event[0] == '_' and len(event) > 1) or event in ['.', '+/-']:
        if event == '+/-':
            window['string_input'].update(values['string_input'] + ' -')
        else:
            window['string_input'].update(values['string_input'] + event[1:])

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

# Close window
window.close()