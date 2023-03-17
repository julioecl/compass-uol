import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados


variancia = np.var(dados.iloc[:, 0:4]) # dados.iloc[:, 0:4].std()

print(variancia)

desvio_padrao = dados.iloc[:, 0:4].std() # np.std(dados.iloc[:, 0:4])

print(desvio_padrao)