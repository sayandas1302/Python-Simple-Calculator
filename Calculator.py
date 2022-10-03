import PySimpleGUI as sg 
import string as st

# app constants
BACKGROUND_COLOR = '#30475E'
BUTTON_COLOR = '#F05454'
BUTTON_FONT = 'Franklin 10 bold'
BUTTON_SIZE = (6,3)

def create_window():
    '''Function to create a GUI for the calculateor'''

    # main window layout
    layout = [
        [
            sg.Text(
            '0', 
            key='-DISPLAY-', 
            font = 'Franklin 30',
            justification='right',
            expand_x=True,
            background_color=BACKGROUND_COLOR)
        ],
        [
            sg.Button('Clear', key='-CLEAR-', size=BUTTON_SIZE, font=BUTTON_FONT, expand_x=True, button_color=BUTTON_COLOR),
            sg.Button('Equal', key='-EQUAL-', size=BUTTON_SIZE, font=BUTTON_FONT, expand_x=True, button_color=BUTTON_COLOR)
        ],
        [
            sg.Button('7', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR),
            sg.Button('8', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR),
            sg.Button('9', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR),
            sg.Button('/', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR)
        ],
        [
            sg.Button('4', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR),
            sg.Button('5', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR),
            sg.Button('6', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR),
            sg.Button('*', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR)
        ],
        [
            sg.Button('1', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR),
            sg.Button('2', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR),
            sg.Button('3', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR),
            sg.Button('-', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR)
        ],
        [
            sg.Button('0', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR, expand_x=True),
            sg.Button('.', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR),
            sg.Button('+', size=BUTTON_SIZE, font=BUTTON_FONT, button_color=BUTTON_COLOR)
        ]
    ]

    return sg.Window(
        'Calculator',
        layout,
        background_color=BACKGROUND_COLOR
    )

exp_string = ''
num_string = ''
 
window = create_window()

while True:
    '''Main loop'''
    
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        '''functionality to close the window'''
        break

    if event in [x for x in st.digits]+['.']:
        '''getting digit input'''
        num_string = num_string + event
        window['-DISPLAY-'].update(num_string)

    if event in ['+', '-', '*', '/']:
        '''getting operation input'''
        exp_string = exp_string + num_string + event
        num_string = ''

    if event == '-EQUAL-':
        '''functionality after pressing the \'=\' operater'''
        exp_string = exp_string + num_string
        result = eval(exp_string)
        window['-DISPLAY-'].update(result)

    if event == '-CLEAR-':
        '''clear display functionality'''
        num_string = ''
        exp_string = ''
        window['-DISPLAY-'].update('0')

window.close()