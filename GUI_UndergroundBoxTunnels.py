# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:44:21 2020

@author: USER
"""

import PySimpleGUI as sg
import numpy as np
from pickle import load

# ADD TITLE COLOUR ,title_color='white'
sg.theme('Dark Blue 3')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Developed by Hoang Dac Nguyen')],
            [sg.Text('University of Nevada Reno, USA')],
            [sg.Text('Email: dhoang@unr.edu')],
            [sg.Text('Accelerated damage state assessment of underground box tunnels using machine learning')],
            [sg.Text('Van-Quang Nguyen, Hoang D. Nguyen, Floriana Petrone, and Dunhee Park')],
              
            [sg.Frame(layout=[
            [sg.Text('B/H (-)',size=(15, 1)),sg.InputText(key='-f1-',size=(30, 1)),sg.Text('1.0-3.0')],
            [sg.Text('D (m)',size=(15, 1)), sg.InputText(key='-f2-',size=(30, 1)),sg.Text('3.0-12.0')],
            [sg.Text('F (-)',size=(15, 1)), sg.InputText(key='-f3-',size=(30, 1)),sg.Text('0.06-7.43')],
            [sg.Text('ASI (g*s)',size=(15, 1)), sg.InputText(key='-f6-',size=(30, 1)),sg.Text('0.08-1.07')],
            [sg.Text('VSI (m)',size=(15, 1)), sg.InputText(key='-f8-',size=(30, 1)),sg.Text('0.19-5.80')],
            [sg.Text('Sa(T1) (g)',size=(15, 1)), sg.InputText(key='-f5-',size=(30, 1)),sg.Text('0.16-3.27')],
            [sg.Text('Sv(T1) (m/s)',size=(15, 1)), sg.InputText(key='-f7-',size=(30, 1)),sg.Text('7.23-169.62')],
            [sg.Text('Sd(T1) (m)',size=(15, 1)),sg.InputText(key='-f4-',size=(30, 1)),sg.Text('0.28-10.26')]],title='Input variables')],
            [sg.Frame(layout=[   
            [sg.Text('Damage state (None, slight, moderate, or extensive)',size=(39, 1)), sg.InputText(key='-OP-',size=(15, 1))]],title='Output')],
            [sg.Button('Predict'),sg.Button('Cancel')] 
            

            
            ]

# Create the Window
window = sg.Window('RAPID DAMAGE-STATE ASSESSMENT OF UNDERGROUND BOX TUNNELS', layout)

filename = 'BestModel_LBM.sav'
loaded_model = load(open(filename, 'rb'))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    #window['-OP-'].update('Please fill all the input parameters')
    if event == 'Predict':
        #window['-OP-'].update(values[0])
        #break
        if values['-f1-'] == '' or values['-f2-'] == '' or values['-f3-'] == '' or values['-f4-'] == '' or values['-f5-'] == '' or values['-f6-'] == '' or values['-f7-'] == '' or values['-f8-'] == '':

            window['-OP-'].update('Please fill all the input parameters')

        else:

            x_test=np.array([[float(values['-f1-']),float(values['-f2-']), float(values['-f3-']),float(values['-f4-']),float(values['-f5-']),values['-f6-'],values['-f7-'],values['-f8-']]])
            y_pred_disp = loaded_model.predict(x_test)
            if y_pred_disp == 1:
                window['-OP-'].update(("None"))
            elif y_pred_disp == 2:
                window['-OP-'].update(("Slight"))
            elif y_pred_disp == 3:
                window['-OP-'].update(("Moderate"))
            else:
                window['-OP-'].update(("Extensive"))   
                    
            

window.close()
