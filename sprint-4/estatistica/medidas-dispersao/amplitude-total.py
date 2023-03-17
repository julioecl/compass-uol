# Diferença entre o maior e o menor valor observado

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados

maximo = dados.iloc[:, 0:4].max()
minimo = dados.iloc[:, 0:4].min()

print(dados.iloc[:, 0:4].max())