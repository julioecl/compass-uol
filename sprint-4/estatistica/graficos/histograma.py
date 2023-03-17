import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
plt.hist(x)
plt.xlabel('Eixo X')
plt.ylabel('Frequência')

plt.show()