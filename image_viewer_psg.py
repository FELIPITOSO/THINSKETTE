# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:57:13 2021

@author: Djaremn
"""

# IMage_Viewer

import PySimpleGUI as sg
import os.path

# Window layout of two columns

"""
key es una herramienta útil pues permite acceder a un elemnto particular
como Folder o File list, dícese de que nos referencia a un elemento
"""

file_list_column = [
    [
         sg.Text('Image Folder'),
         sg.In(size=(25,1), enable_events=True, key='-FOLDER-'),
         sg.FolderBrowse()
     ],
    [
         sg.Listbox(
             values=[], enable_events=True, size=(40,20),
             key='-FILE LIST-'
             )
     ],
    
    ]


# Esta siguientes líneas solo mostrarán el nombre del archivo escogido

image_viewer_column = [
    [sg.Text('Elige una imagen de la lista a la izquierda')],
    [sg.Text(size=(40,1), key='-TOUT-')],
    [sg.Image(key='-IMAGE')],
    ]



# Full layout 

layout = [
    [
         sg.Column(file_list_column),
         sg.VSeparator(),
         sg.Column(image_viewer_column) 
     ]
]

window = sg.Window('IMViewer', layout)


# Event loop

while True: 
    event, values = window.read()
    if event == 'No me cierres :c' or event == sg.WIN_CLOSED:
        break
    
window.closed()









