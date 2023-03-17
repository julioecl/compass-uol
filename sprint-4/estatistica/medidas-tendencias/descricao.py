import numpy as np
from bokeh.sampledata.iris import flowers as dados
import matplotlib.pyplot as plt

# Descrição detalhada de todas as informações relativas aos dados da tabela.
print(dados.describe())

# x = dados['sepal_length']
# y = dados['sepal_width']
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')

# plt.plot(np.mean(x), np.mean(y), 'or')
# plt.plot(np.median(x), np.median(y), 'oy')
# plt.plot(x.mode(), y.mode(), 'og')

# plt.scatter(x, y)
# plt.show()

x = dados['petal_length']
y = dados['petal_width']
plt.xlabel('petal length')
plt.ylabel('petal width')

plt.plot(np.mean(x), np.mean(y), 'or')
plt.plot(np.median(x), np.median(y), 'oy')
# plt.plot(x.mode(), y.mode(), 'og')

plt.scatter(x,y)
plt.show()


