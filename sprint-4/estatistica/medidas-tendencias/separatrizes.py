import numpy as np
from bokeh.sampledata.iris import flowers as dados
import matplotlib.pyplot as plt

P10 = np.quantile(dados['sepal_length'], 0.10)

print(P10)