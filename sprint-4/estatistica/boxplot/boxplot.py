"""
Boxplot é um gráfico que utiliza cinco medidas estatísticas:
- Valor mínimo;
- Valor máximo;
- Mediana (Q2); -> posição central
- Primeiro quartil (Q1);
- Terceiro quartil (Q3).
Oferece a ideia:
- Posição;
- Dispersão;
- Assimetria;
- Caudas;
- Dados discrepantes.
"""

import seaborn as sns
import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados

sns.set(style='whitegrid', color_codes=True)
boxplot = sns.boxplot(data = dados)

plt.show()
