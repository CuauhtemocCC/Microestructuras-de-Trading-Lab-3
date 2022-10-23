
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Comportamiento Financiero                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: CuauhtemocCC                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/CuauhtemocCC/MyST_LAB_3_E3                                                                      -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import functions as fn 

def plot_pie_graph(tabla):
    tabla = tabla[tabla["rank"] > 0]
    tabla["Symbol"] = tabla.index.get_level_values("Símbolo")
    
    labels = tabla.iloc[:,2].tolist()
    values = tabla.iloc[:,0].tolist()

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0.15, 0, 0, 0])])
    fig.update_layout(legend_title="Symbols", title="Rank Sucessful Ops",
        font=dict(
        size=15,
        color="black"
    )
    )
    return fig.show()

def id_DU_DD(tabla):
    tabla["DU"] = [tabla["profit_acum_d"].max() if tabla["profit_acum_d"][i]==tabla["profit_acum_d"].max() else None for i in range(len(tabla["profit_acum_d"]))]
    tabla["DD"] = [tabla["profit_acum_d"].min() if tabla["profit_acum_d"][i]==tabla["profit_acum_d"].min() else None for i in range(len(tabla["profit_acum_d"]))]
    
    return tabla

def plot_DDC_DUC(tabla):
    df_DUDD = id_DU_DD(tabla)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tabla.iloc[:,0], y=tabla.iloc[:,2], name='Capital', line=dict(color='black', width=4)))
    fig.add_trace(go.Scatter(x=df_DUDD.iloc[:,0], y=df_DUDD.iloc[:,4], name='Drawn Up',
                             marker = dict(color='chartreuse', size=15)))
    fig.add_trace(go.Scatter(x=df_DUDD.iloc[:,0], y=df_DUDD.iloc[:,5], name='Drawn Down',
                             marker = dict(color='red', size=15)))
    fig.update_layout(title='Capital Evolution',
                       xaxis_title='Date',
                       yaxis_title='Capital',
                     font=dict(size=15,color="black"))
    
    return fig.show()