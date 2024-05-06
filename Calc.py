import PySimpleGUI as sg

total= "o"
num2 = 0
num1 = 0

sg.theme('Dark Teal 9')

layout = [  [sg.Text("Make your inquiry:")],
            [sg.Button('1', size =(3, 1)), sg.Button('2', size =(3, 1)), sg.Button('3', size =(3, 1)), sg.Button('+', size =(3, 1))],
            [sg.Button('4', size =(3, 1)), sg.Button('5', size =(3, 1)), sg.Button('6', size =(3, 1)), sg.Button('-', size =(3, 1))],
            [sg.Button('7', size =(3, 1)), sg.Button('8', size =(3, 1)), sg.Button('9', size =(3, 1)), sg.Button('*', size =(3, 1))],
            [sg.Button('(+/-)', size =(3, 1)), sg.Button('0', size =(3, 1)), sg.Button('=', size =(3, 1)), sg.Button('/', size =(3, 1))],
            [sg.Text("Answer:", size =(15, 1)), sg.Text(key ='TOTAL', size =(15, 1), background_color = "#466879")],
            [sg.Submit(), sg.Cancel()]  ]


# Create the Window
window = sg.Window("Ren's CalKinator", layout)

def opera2(operador, a, b):
    return {
        '+': lambda: a + b,
        '-': lambda: a - b,
        '*': lambda: a * b,
        '/': lambda: a / b
    }.get(operador, lambda: None)()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break 
    
    elif event == 'submit' or event == '=':
        num2 = opera2(eq,num1,num2)
        num1 = 0
        window['TOTAL'].update(num2)
        print(num2)

    elif event == '(+/-)':
        num2 *= -1
        window['TOTAL'].update(num2)
        print(num2)

    elif event == '*' or event == '+' or event == '-' or event == '/':
       num1 = num2
       num2 = 0
       print(num2)
       eq = event
       
    elif int(event)>=0 and int(event)<=9:
        num2 = num2*10 + int(event)
        window['TOTAL'].update(num2)
        print(num2)

window.close()