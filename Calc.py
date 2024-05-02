import PySimpleGUI as sg

layout = [  [sg.Text("Enter a number")],
            [sg.Text('Num 1', size =(15, 1)), sg.InputText()],
            [sg.Text('Num 2', size =(15, 1)), sg.InputText()],
            [sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/')],
            [sg.Submit(), sg.Cancel()]  ]


# Create the Window
window = sg.Window('Hello Example', layout)

def opera2(operador, a, b):
    return {
        '+': lambda: a + b,
        '-': lambda: a - b,
        '*': lambda: a * b,
        '/': lambda: a / b
    }.get(operador, lambda: None)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break 
    
    if event == 'submit':
        opera2()

    if event == '*' or event == '+' or event == '-' or event == '/':
       num1 = values[0]
       num2 = values[1]
       eq = event
       total = opera2(eq,num1,num2)
       print(total)

      #  break
    # if user closes window or clicks cancel


   

window.close()