#     *****     import     *****
from tabnanny import check
#from typing_extensions import IntVar
import pandas as pd
import tkinter as tkr
import matplotlib.pyplot as plt
import numpy as np
from tkinter import IntVar, filedialog
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

#     *****     Finestra     *****
app = tkr.Tk()
app.geometry('800x600')
app.title('Gestire Grafici 1S')
app.iconbitmap('omron.ico')

#plt.use('TkAgg')

CheckB = IntVar() 
CheckC = IntVar() 
CheckD = IntVar() 
CheckE = IntVar() 

#     *****      Funzione Bottone      *****
def btnCaricaFile():
    files = filedialog.askopenfilenames()
    str = ''.join(files)
    df = pd.read_csv(str, sep=';')
    indexNames = df[df['A'] == 0].index
    df.drop(indexNames, inplace=True)
    plt.title('titolo')
    #plt.plot(df["index"], df["B"])
    if CheckB.get() == 1 : 
        plt.scatter(df["index"], df["B"])
    if CheckC.get() == 1 : 
        plt.scatter(df["index"], df["C"])
    if CheckD.get() == 1 : 
        plt.scatter(df["index"], df["D"])
    if CheckE.get() == 1 : 
        plt.scatter(df["index"], df["E"])
    plt.show()


#     *****     Grafica Tkinter     *****
BottoneCaricaFile = tkr.Button(app, text ="Carica File", command = btnCaricaFile)
BottoneCaricaFile.grid(column=0, row=0, padx=10, pady=10)
FlagB = tkr.Checkbutton(app,text= "Velocità", variable = CheckB, onvalue = 1, offvalue = 0)
FlagB.grid(column=0, row=1, padx=10, pady=10)
FlagC = tkr.Checkbutton(app,text= "Coppia", variable = CheckC, onvalue = 1, offvalue = 0)
FlagC.grid(column=0, row=2, padx=10, pady=10)
FlagD = tkr.Checkbutton(app,text= "Par D", variable = CheckD, onvalue = 1, offvalue = 0)
FlagD.grid(column=0, row=3, padx=10, pady=10)
FlagE = tkr.Checkbutton(app,text= "Par E", variable = CheckE, onvalue = 1, offvalue = 0)
FlagE.grid(column=0, row=4, padx=10, pady=10)

#     ****** Visualizzazione App     ***** develop
app.mainloop()