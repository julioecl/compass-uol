# Diferença entre cada valor e a média.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados

desvio_medio = dados.mad()

print(desvio_medio)