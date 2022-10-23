
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Comportamiento Financiero                                                        -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: CuauhtemocCC                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/CuauhtemocCC/MyST_LAB_3_E3                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
#import warnings
#warnings.filterwarnings('ignore')

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from datetime import datetime
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf

def leer_archivo(archivo:str):
    datos = pd.read_excel(archivo,sheet_name="Posiciones")
    datos = datos.fillna(0)
    return datos

def columnas_tiempos(tabla):
    tabla["opentime"] = tabla["Fecha/Hora"]
    tabla["closetime"] = tabla["Fecha/Hora.1"]
    #formato = "%Y.%m.%d %H:%M:%S"
    tabla["opentime"] = pd.to_datetime(tabla["opentime"])
    tabla["closetime"] = pd.to_datetime(tabla["closetime"])
    tabla["time(seconds)"] = tabla["closetime"]-tabla["opentime"]
    for i in range(len(tabla["time(seconds)"])):
        tabla.iloc[i,16] = tabla.iloc[i,16].total_seconds()
    return tabla

def columnas_pips(tabla):
    tabla["pips"] = np.zeros(len(tabla["Tipo"]))
    for i in range(len(tabla["Tipo"])):
        if tabla["Tipo"][i]=="buy":
            tabla["pips"][i] = (tabla["Precio.1"][i]-tabla["Precio"][i])*tabla["Lote"][i]*tabla["Volumen"][i]
        else:
            tabla["pips"][i] = (tabla["Precio"][i]-tabla["Precio.1"][i])*tabla["Lote"][i]*tabla["Volumen"][i]

    tabla["pips_acum"] = tabla["pips"].cumsum()
    #tabla["Beneficio"] = tabla["Beneficio"].astype(int)
    tabla["profit_acum"] = tabla["Beneficio"].cumsum()
    tabla["Ops Totales"] = np.ones(len(tabla["Beneficio"]))
    return tabla

def estadisticas_ba1(tabla):
    medidas = ["Ops totales","Ganadoras","Ganadoras_c","Ganadoras_v","Perdedoras","Perdedoras_c","Perdedoras_v",
               "Mediana (Profit)","Mediana (Pips)","r_efectividad","r_proporcion","r_efectividad_c","r_efectividad_v"]
    
    descrip = ["Operaciones totales","Operaciones ganadoras","Operaciones ganadoras de compra",
               "Operaciones perdedoras de venta","Operaciones perdedoras","Operaciones perdedoras de compra",
               "Operaciones perdedoras de venta","Mediana de profit de operaciones",
               "Mediana de pips de operaciones","Ganadoras Totales/Operaciones Totales",
               "Ganadoras Totales/Perdedoras Totales","Ganadoras Compras/Operaciones Totales",
               "Ganadoras Ventas/ Operaciones Totales"]
    
    valor = np.zeros(13)
    
    datos_df1 = {"medidas":medidas,"valor":valor,"descripcion":descrip}
    df1 = pd.DataFrame(datos_df1)
    
    tabla["Ops Ganadoras"] = np.zeros(len(tabla["Tipo"]))
    tabla["Ops Perdedoras"] = np.zeros(len(tabla["Tipo"]))
    tabla["Ops Ganadoras_C"] = np.zeros(len(tabla["Tipo"]))
    tabla["Ops Perdedoras_C"] = np.zeros(len(tabla["Tipo"]))
    tabla["Ops Ganadoras_V"] = np.zeros(len(tabla["Tipo"]))
    tabla["Ops Perdedoras_V"] = np.zeros(len(tabla["Tipo"]))
    
    df1.valor[0] = len(tabla.Tipo)
    
    for i in range(len(tabla["Beneficio"])):
        if tabla["Beneficio"][i] > 0:
            tabla["Ops Ganadoras"][i] = 1
            tabla["Ops Perdedoras"][i] = 0
        else:
            tabla["Ops Ganadoras"][i] = 0
            tabla["Ops Perdedoras"][i] = 1
    
    df1.valor[1] = sum(tabla["Ops Ganadoras"])
    df1.valor[4] = sum(tabla["Ops Perdedoras"])
    
    for i in range(len(tabla["Beneficio"])):
        if tabla["Ops Ganadoras"][i] == 1 and tabla["Tipo"][i] == "buy" :
            tabla["Ops Ganadoras_C"][i] = 1
        elif tabla["Ops Ganadoras"][i] == 1 and tabla["Tipo"][i] == "sell" :
            tabla["Ops Ganadoras_V"][i] = 1
        elif tabla["Ops Perdedoras"][i] == 1 and tabla["Tipo"][i] == "buy" :
            tabla["Ops Perdedoras_C"][i] = 1
        elif tabla["Ops Perdedoras"][i] == 1 and tabla["Tipo"][i] == "sell" :
            tabla["Ops Perdedoras_V"][i] = 1
        else:
            tabla["Ops Ganadoras_C"][i] = 0
            tabla["Ops Ganadoras_V"][i] = 0
            tabla["Ops Perdedoras_C"][i] = 0
            tabla["Ops Perdedoras_V"][i] = 0
            
    df1.valor[2] = sum(tabla["Ops Ganadoras_C"])
    df1.valor[3] = sum(tabla["Ops Ganadoras_V"])
    df1.valor[5] = sum(tabla["Ops Perdedoras_C"])
    df1.valor[6] = sum(tabla["Ops Perdedoras_V"])
    
    df1.valor[7] = tabla["Beneficio"].median()
    df1.valor[8] = tabla["pips"].median()
    
    df1.valor[9] = round(sum(tabla["Ops Ganadoras"])/len(tabla["Ops Perdedoras"]),3)
    df1.valor[10] = round(sum(tabla["Ops Ganadoras"])/sum(tabla["Ops Ganadoras"]),3)
    df1.valor[11] = round(sum(tabla["Ops Ganadoras_C"])/len(tabla["Ops Ganadoras"]),3)
    df1.valor[12] = round(sum(tabla["Ops Ganadoras_V"])/len(tabla["Ops Ganadoras"]),3)
    
    return df1

def estadisticas_ba2(tabla):
    for i in range(len(tabla["Beneficio"])):
        if tabla["Beneficio"][i] > 0:
            tabla["Ops Ganadoras"][i] = 1
            tabla["Ops Perdedoras"][i] = 0
        else:
            tabla["Ops Ganadoras"][i] = 0
            tabla["Ops Perdedoras"][i] = 1

    for i in range(len(tabla["Beneficio"])):
        if tabla["Ops Ganadoras"][i] == 1 and tabla["Tipo"][i] == "buy" :
            tabla["Ops Ganadoras_C"][i] = 1
        elif tabla["Ops Ganadoras"][i] == 1 and tabla["Tipo"][i] == "sell" :
            tabla["Ops Ganadoras_V"][i] = 1
        elif tabla["Ops Perdedoras"][i] == 1 and tabla["Tipo"][i] == "buy" :
            tabla["Ops Perdedoras_C"][i] = 1
        elif tabla["Ops Perdedoras"][i] == 1 and tabla["Tipo"][i] == "sell" :
            tabla["Ops Perdedoras_V"][i] = 1
        else:
            tabla["Ops Ganadoras_C"][i] = 0
            tabla["Ops Ganadoras_V"][i] = 0
            tabla["Ops Perdedoras_C"][i] = 0
            tabla["Ops Perdedoras_V"][i] = 0
            
    pivot = pd.pivot_table(tabla,index=["Símbolo"],aggfunc={"Ops Ganadoras":np.sum,"Ops Totales":np.sum})
    pivot["rank"] = (pivot["Ops Ganadoras"]/pivot["Ops Totales"])
    pivot = pivot.drop(["Ops Ganadoras","Ops Totales"],axis=1)
    pivot = pivot.sort_values('rank',ascending=False)
    pivot["rank"] = round(pivot["rank"],2)
    pivot["rank %"] = pivot["rank"].map(lambda x:format(x,'.2%'))
    #pivot_ord["rank"] = pivot_ord["rank"].map(lambda x:format(x,'.2%'))
    return pivot

def evolucion_capital(tabla):
    tabla["day"] = tabla["closetime"].dt.strftime("%Y-%m-%d")

    pivot2 = pd.pivot_table(tabla,index=["day"],aggfunc={"Beneficio":np.sum})

    pivot2["timestamp"] = pivot2.index.get_level_values("day")
    pivot2 = pivot2.reindex(columns=['timestamp', 'Beneficio'])
    
    start = datetime.strptime(tabla["day"].min(), "%Y-%m-%d")
    end = datetime.strptime(tabla["day"].max(), "%Y-%m-%d")
    date_generated = pd.date_range(start, end)
    date_generated = date_generated.strftime("%Y-%m-%d")
    
    d3 = {"timestamp":date_generated,"profit_d": np.zeros(len(date_generated))}
    registros_d = pd.DataFrame(d3)
    
    for i in range(len(registros_d["timestamp"])):
        for j in range(len(pivot2["timestamp"])):
            if registros_d["timestamp"][i] == pivot2["timestamp"][j]:
                registros_d["profit_d"][i] = pivot2["Beneficio"][j]
                
    registros_d["profit_acum_d"] = np.zeros(len(registros_d["profit_d"]))
    registros_d["profit_acum_d"][0] = 100000+registros_d["profit_d"][0]

    for i in range(1,len(registros_d["profit_d"])):
        registros_d["profit_acum_d"][i] = registros_d["profit_acum_d"][i-1]+registros_d["profit_d"][i]
        
    return registros_d

def estadisticas_mad(tabla1,tabla2):
    
    # Sharpe Ratio Original
    tabla1["rends_log"] = np.log(tabla1["profit_acum_d"].shift(periods=1)/tabla1["profit_acum_d"])
    tabla1["rends_log"] = tabla1["rends_log"]*-1
    tabla1["rends_log"][0] = np.log(tabla1["profit_acum_d"][0]/100000)
    rp = tabla1["rends_log"].mean()
    std = tabla1["rends_log"].std()
    rf = 0.05
    SRO = (rp-rf)/std
    
    # Sharpe Ratio Benchmark
    data_sp500 = yf.download("^GSPC", start="2021-01-01", end="2022-10-14")
    data_sp500["Rends_log"] = np.log(data_sp500["Adj Close"].shift(periods=1)/data_sp500["Adj Close"])
    data_sp500["Rends_log"] = data_sp500["Rends_log"]*-1
    r_trader = rp
    r_benchmark = data_sp500["Rends_log"].mean()
    SRA = ((r_trader-r_benchmark)-rf)/std
    
    # Drawndown(Capital)
    tabla2["Capital"] = np.zeros(len(tabla2["profit_acum"]))
    tabla2["Capital"][0] = 100000+tabla2["profit_acum"][0]
    for i in range(1,len(tabla2["profit_acum"])):
        tabla2["Capital"][i] = tabla2["Capital"][i-1]+tabla2["Beneficio"][i]
    DDC_range = tabla2[tabla2['Capital'] == tabla2["Capital"].min()]
    DDC = DDC_range.iloc[0,28]
    DDC_ot = DDC_range.iloc[0,14]
    DDC_ct = DDC_range.iloc[0,15]
    
    # Drawnup(Capital)
    DUC_range = tabla2[tabla2['Capital'] == tabla2["Capital"].max()]
    DUC = DUC_range.iloc[0,28]
    DUC_ot = DUC_range.iloc[0,14]
    DUC_ct = DUC_range.iloc[0,15]
    
    datos_desempeño = {"Metrica":["sharpe_original","sharpe_actualizado","drawdown_capi","drawdown_capi","drawdown_capi",
                                  "drawup_capi","drawup_capi","drawup_capi"],
                       "Tipo de Dato":["Cantidad","Cantidad","Fecha Inicial","Fecha Final","DrawDown $ (capital)","Fecha Inicial",
                                      "Fecha Final","DrawUp $ (capital)"],
                      "Valor":np.zeros(8),
                      "Descripcion":["Sharpe Ratio Fórmula Original","Sharpe Ratio Fórmula Ajustada","Fecha inicial del DrawDown de Capital",
                                    "Fecha final del DrawDown de Capital","Máxima pérdida flotante registrada",
                                    "Fecha inicial del DrawUp de Capital","Fecha final del DrawUp de Capital",
                                    "Máxima ganancia flotante registrada"]}
    
    tabla_desempeño = pd.DataFrame(datos_desempeño)
    
    tabla_desempeño["Valor"][0] = SRO
    tabla_desempeño["Valor"][1] = SRA
    tabla_desempeño["Valor"][4] = DDC
    tabla_desempeño["Valor"][2] = DDC_ot
    tabla_desempeño["Valor"][3] = DDC_ct
    tabla_desempeño["Valor"][7] = DUC
    tabla_desempeño["Valor"][5] = DUC_ot
    tabla_desempeño["Valor"][6] = DUC_ct

    return tabla_desempeño






