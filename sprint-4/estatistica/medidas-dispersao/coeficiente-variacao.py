# Variabilidade da medida em relação a média.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados

desvio_padrao = dados.iloc[:, 0:4].std()
media = dados.iloc[:, 0:4].mean()

cv = (desvio_padrao/media)*100

print(cv)