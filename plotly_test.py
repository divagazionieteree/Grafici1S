from tkinter import *
import chart_studio.plotly as py
import plotly.graph_objs as go 

from datetime import datetime
from pandas_datareader import data
#import pandas.io.data as web


mGui = Tk()

mGui.geometry('651x700+51+51')
mGui.title('Plotly at Tkinter')

df = data.DataReader("AAPL", 'yahoo',
                    datetime(2007, 10, 1),
                    datetime(2016, 7, 11))

trace = go.Scatter(x=df.index,
                   y=df.High)


data1 = [trace]
layout = dict(
    title='Time series with range slider and selectors',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        type='date'
    )
)

fig = dict(data=data1, layout=layout)
py.iplot(fig)

mGui.mainloop()