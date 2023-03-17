import numpy as np
from bokeh.sampledata.iris import flowers as dados

media = round(np.mean(dados['sepal_length']), 2)
print(media)
media2 = round(np.mean(dados['sepal_width']), 2)
print(media2)

media_geral = np.mean(dados)
print(media_geral)