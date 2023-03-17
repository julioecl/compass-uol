import matplotlib.pyplot as plt

y = [ 2, 5, 2, 7, 5, 1]
x = [ 'n1', 'n2', 'n3', 'n4', 'n5', 'n6']

plt.pie(y, labels=x, radius=1)
plt.show()