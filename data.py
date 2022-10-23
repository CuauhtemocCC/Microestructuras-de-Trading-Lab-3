
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Comportamiento Financiero                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: CuauhtemocCC                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/CuauhtemocCC/MyST_LAB_3_E3                                                                       -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import functions as fn 
import numpy as np

datos_c = fn.leer_archivo("files/MyST_LAB2_CuauhtemocCorralesC.xlsx")
datos_m = fn.leer_archivo("files/MyST_LAB2_MarcoOchoac.xlsx")
datos_e = fn.leer_archivo("files/Historicos_Esteban.xlsx")

datos2_c = fn.columnas_tiempos(datos_c)
datos2_m = fn.columnas_tiempos(datos_m)
datos2_e = fn.columnas_tiempos(datos_e)

datos3_c = fn.columnas_pips(datos2_c)
datos3_m = fn.columnas_pips(datos2_m)
datos3_e = fn.columnas_pips(datos2_e)

df_1_tabla_c = fn.estadisticas_ba1(datos3_c)
df_1_tabla_m = fn.estadisticas_ba1(datos3_m)
df_1_tabla_e = fn.estadisticas_ba1(datos3_e)

df_2_tabla_c = fn.estadisticas_ba2(datos3_c)
df_2_tabla_m = fn.estadisticas_ba2(datos3_m)
df_2_tabla_e = fn.estadisticas_ba2(datos3_e)

evo_c_c = fn.evolucion_capital(datos3_c)
evo_c_m = fn.evolucion_capital(datos3_m)
evo_c_e = fn.evolucion_capital(datos3_e)

metricas_c = fn.estadisticas_mad(evo_c_c,datos3_c)
metricas_m = fn.estadisticas_mad(evo_c_m,datos3_m)
metricas_e = fn.estadisticas_mad(evo_c_e,datos3_e)

dict_datos4 = {"order":datos3_c["Posición"],
              "opentime":datos3_c["opentime"],
              "type":datos3_c["Tipo"],
               "size":datos3_c["Volumen"],
               "symbol":datos3_c["Símbolo"],
               "openprice":datos3_c["Precio"],
               "s/l":datos3_c["S / L"],
               "t/p":datos3_c["T / P"],
               "closetime":datos3_c["closetime"],
               "closeprice":datos3_c["Precio.1"],
               "comission":datos3_c["Comisión"],
               "taxes":np.zeros(len(datos3_c["Posición"])),
               "swap":datos3_c["Swap"],
               "profit":datos3_c["Beneficio"],
                "time":datos3_c["time(seconds)"],
              "pips":datos3_c["pips"],
              "pips_acum":datos3_c["pips_acum"],
              "profit_acum":datos3_c["profit_acum"],
              "capital_acm":datos3_c["Capital"]}
 
datos4 = pd.DataFrame(dict_datos4)