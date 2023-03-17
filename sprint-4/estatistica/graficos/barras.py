import matplotlib.pyplot as plt
# import seaborn as sns

y = [ 2, 5, 2, 7, 5, 1]
x = [ 'n1', 'n2', 'n3', 'n4', 'n5', 'n6']

# Seaborn

# sns.barplot(x, y)

# Barras horizontais

plt.barh(x,y)
plt.xlabel('Variável eixo X', size=24)
plt.ylabel('Categoria', size=24)
plt.title('Título')

# Barras verticais

plt.bar(x,y)
plt.xlabel('Variável eixo X', size=24)
plt.ylabel('Categoria', size=24)
plt.title('Título')

plt.show()

