import random
import PySimpleGUI as sg


def password_generator(pw_len):
    password = "".join(random.sample(chars, pw_len))
    return password

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|!\"£$%&/()=?^é*ç°§;:_è+òàù,.-[]@#{}"
sg.theme('DarkPurple3')

layout = [[sg.Text('Password Generator', font=('Roboto', 20), justification='center')],
          [sg.Text('Set password length: ', size=(15, 1)), sg.InputText(size=(15, 1), key='length')],
          [sg.Text('Your password: '), sg.Input(disabled=True, text_color=sg.theme_text_color(), disabled_readonly_background_color=sg.theme_text_element_background_color(), key='-RESULT-'), ],
          [sg.Button('Generate', size=(15, 1)), sg.Button('Exit', size=(15, 1))]]

window = sg.Window('Password Generator', layout)

while(True):
    event, values = window.read()
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break
    elif event == 'Generate':
        pw_len = int(values['length'])
        window['-RESULT-'].update(password_generator(pw_len))

window.close()