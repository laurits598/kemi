import PySimpleGUI as sg
import periodictable as pt
import numpy as np
import dataElements as de
#import dataSubstances as ds
import os
from PIL import Image
import io


#defaultIMG = "C:/Users/Laurits/Desktop/Kemi/elementsImages/atom.png"
directory = "C:/Users/Laurits/Desktop/Kemi/elementsImages/"
    

def layout3update(combo, Gs, imgID):
    place = 0
    for x in range(0,len(Gs)):
        if str(Gs[x][1]) in str(combo):
            place = x

    image = de.getImage(imgID)
    window['eleImg'].update(image, visible=True)
    window['loco'].update("                    Location in the PT:   "+str(Gs[place][0]), visible=True)
    window['lo3Name'].update("Name:                     "+str(Gs[place][1]), visible=True)
    window['lo3abbr'].update("Abbreviation:            "+str(Gs[place][2]), visible=True)
    window['mm'].update     ("Molar mass:            "+str(Gs[place][3]), visible=True)
    


Gs = [[]]
GsN = []
for x in range(1,119):
    Gs = np.append(Gs, [x])
    Gs = np.append(Gs, [pt.elements[x].name])
    Gs = np.append(Gs, [pt.elements[x]])
    Gs = np.append(Gs, [pt.elements[x].mass])
    
    GsN = np.append(GsN, str(x)+"  "+str(pt.elements[x].name))
    
Gsname = []
for x in GsN:
    Gsname.append(str(x.replace(",","")))
Gs = Gs.reshape(118,4)

# find billede
layout1 = [ 
            #[sg.Image(defaultIMG, key="eleImg", visible=True, size=(900,600))]
            [sg.Text("", key="loco", visible = False)]
          ]

layout2 = [ 
            [sg.Image('',key="ENimg", visible=True, size=(900,600))],
          ]


layout3 = [
            [sg.Text("Choose element: "), sg.Combo(Gsname," ",key="combo"), sg.Button("Load",key="loadelement")],  
            [sg.Text("")],
            [sg.Text("")],
            [sg.Image("", key="eleImg", visible=True, size=(900,600))],
            [sg.Text("")],
            [sg.Text("", key="loco", visible = False)],
            [sg.Text("", key="lo3Name", visible = False)],
            [sg.Text("", key="lo3abbr", visible = False)],
            [sg.Text("", key="mm", visible = False)] 
          ]
# start
lout = [  
          [sg.Button("  Periodic Table  "), sg.Button("Electro Negativity"), sg.Button("     Elements     ")],
          [sg.Text("_________________________________________________________________________________________________________________________________________")],
          [sg.Column(layout1, key='layout1', visible = False), sg.Column(layout2, key='layout2', visible = False), sg.Column(layout3, key='layout3', visible = False)],
          [sg.Image("", key="eleImg", visible=True, size=(900,600))]
       ]

window = sg.Window('Window Title', lout,size=(950, 700), element_justification='c')
combo = ""
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    elif event == '  Periodic Table  ':
        window['layout1'].update(visible=True)
        window['layout2'].update(visible=False)
        window['layout3'].update(visible=False)
    
    elif event == 'Electro Negativity':
        window['layout1'].update(visible=False)
        window['layout2'].update(visible=True)
        window['layout3'].update(visible=False)
        
    elif event == '     Elements     ':
        window['layout1'].update(visible=False)
        window['layout2'].update(visible=False)
        window['layout3'].update(visible=True)
        
    elif event == 'loadelement':
        combo = values['combo']
        temp = combo[0:2]
        imgID = temp.strip() 
        layout3update(combo, Gs, imgID)
            
window.close()