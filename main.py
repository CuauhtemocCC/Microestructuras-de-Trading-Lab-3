
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Comportamiento Financiero                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: CuauhtemocCC                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/CuauhtemocCC/MyST_LAB_3_E3                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import data as dt
import functions as fn
import visualizations as vs

dt.df_1_tabla_c
dt.df_1_tabla_m
dt.df_1_tabla_e

dt.df_2_tabla_c
dt.df_2_tabla_m
dt.df_2_tabla_e

dt.evo_c_c
dt.evo_c_m
dt.evo_c_e

dt.metricas_c
dt.metricas_m
dt.metricas_e

pie_chart_c = vs.plot_pie_graph(dt.df_2_tabla_c)
pie_chart_m = vs.plot_pie_graph(dt.df_2_tabla_m)
pie_chart_e = vs.plot_pie_graph(dt.df_2_tabla_e)

DrawUpDown_c = vs.plot_DDC_DUC(dt.evo_c_c)
DrawUpDown_m = vs.plot_DDC_DUC(dt.evo_c_m)
DrawUpDown_e = vs.plot_DDC_DUC(dt.evo_c_e)
