import numpy as np
from bokeh.sampledata.iris import flowers as dados

mediana = np.median(dados['petal_length'])

print(mediana)