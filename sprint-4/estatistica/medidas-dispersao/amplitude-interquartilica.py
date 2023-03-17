# Diferença entre o primeiro e o terceiro quartil.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados

q3 = dados['sepal_length'].quantile(0.75)
q1 = dados['sepal_length'].quantile(0.25)

amplitude = q3 - q1

print(amplitude)

# Total

dqt = dados.quantile(0.75) - dados.quantile(0.25)

print(dqt)