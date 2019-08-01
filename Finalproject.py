# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:39:10 2019

@author: STEM
"""

import pandas as pd
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

ccdf = pd.read_excel("GISdata.xlsx", sheet_name = "cancercases")
cancerCases = go.Bar(x = ccdf['CancerType'], y = ccdf['Number'], marker = {"color": ccdf["Number"], 'colorscale':"Jet"})
#plot([womenoccupation])


cancerc = go.Bar(x=ccdf["CancerType"], y=ccdf["Number"], marker = {"color": ccdf["Number"], 'colorscale':"Jet"})

titles = go.Layout(title = "Number of Different Cancer Types",
    xaxis = go.layout.XAxis(title=go.layout.xaxis.Title(text="CancerType",)),
    yaxis = go.layout.YAxis(title=go.layout.yaxis.Title(text="Number",)))
    
fig = go.Figure(data=[cancerCases], layout=titles)
plot(fig)