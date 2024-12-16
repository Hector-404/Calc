# Import Module
from PySimpleGUI import *
import math
# import cmath

''' GUI Layout ----Creating the Layout of the Calculator, i.e., the buttons, window and the frame along with the theme, font, font size, etc.'''

layout = [
    [Text('', size=(25, 2), font=('Helvetica', 25), text_color='white', key='input', background_color='grey', pad=((5, 1), 10), justification='left', relief=RELIEF_SUNKEN, border_width=8)],
    [Button('sin', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')),Button('sin⁻¹', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')),Button('AC', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')), Button('C', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')), Button('(', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')), Button(')', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black'))],
    [Button('cos', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')),Button('cos⁻¹', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')),Button('7', size=(6, 2), font=('Helvetica', 15)), Button('8', size=(6, 2), font=('Helvetica', 15)), Button('9', size=(6, 2), font=('Helvetica', 15)), Button('/', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black'))],
    [Button('tan', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')),Button('tan⁻¹', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')),Button('4', size=(6, 2), font=('Helvetica', 15)), Button('5', size=(6, 2), font=('Helvetica', 15)), Button('6', size=(6, 2), font=('Helvetica', 15)), Button('*', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black'))],
    [Button('^', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')),Button('π', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')),Button('1', size=(6, 2), font=('Helvetica', 15)), Button('2', size=(6, 2), font=('Helvetica', 15)), Button('3', size=(6, 2), font=('Helvetica', 15)), Button('-', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black'))],
    [Button('log', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')),Button('ln', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black')),Button('.', size=(6, 2), font=('Helvetica', 15)), Button('0', size=(6, 2), font=('Helvetica', 15)), Button('=', size=(6, 2), font=('Helvetica', 15)), Button('+', size=(6, 2), font=('Helvetica', 15), button_color=('orange', 'black'))],
]

theme('DarkGrey10')

# Set PySimpleGUI
form = Window('SCIENTIFIC CALCULATOR', layout, default_button_element_size=(8,4),
              auto_size_buttons=False, grab_anywhere=True,)

# Result Value
Result = ''

# To edit the expression before the final evaluation of the expression entered by the user
def evaluation(S):
    l = len(S)
    S = S.replace('sin','math.sin')
    S = S.replace('cos','math.cos')
    S = S.replace('tan','math.tan')
    S = S.replace('math.sin⁻¹','math.asin')
    S = S.replace('math.cos⁻¹','math.acos')
    S = S.replace('math.tan⁻¹','math.atan')
    S = S.replace('π','math.pi')
    S = S.replace('^','**')
    S = S.replace('log','math.log10')
    S = S.replace('ln','math.log')
    return S
    
# Make Infinite Loop
while True:
    
    # Button Values
    event, values = form.read()

    # Check Press Button Values
    if event == 'AC':
        Result = ''
        form['input'].update(Result)
    elif event == 'C':
        Result = Result[:-1]
        form['input'].update(Result)
    elif len(Result) == 16:
        pass

    # Results
    elif event == '=':
        try:
            Result1 = evaluation(Result)
            Answer = eval(Result1)
            Answer = str(round(float(Answer), 3))
            form['input'].update(Answer)
            Result = Answer
        except:
            form['input'].update("Error")
            Result = ""
    # Close the window
    
    elif event == WIN_CLOSED:
        break
    else:
        Result += event
        
        form['input'].update(Result)
