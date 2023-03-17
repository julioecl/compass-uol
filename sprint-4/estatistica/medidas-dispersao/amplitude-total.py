# Diferença entre o maior e o menor valor observado

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados

maximo = dados.iloc[:, 0:4].max() # np.max(dados.iloc[:, 0:4])
minimo = dados.iloc[:, 0:4].min() # np.min(dados.iloc[:, 0:4])
amplitude = maximo - minimo

print(amplitude)