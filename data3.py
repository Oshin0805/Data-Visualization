import matplotlib.pyplot as plt

x_val = list(range(1, 1001))
y_val = [x**2 for x in x_val]

plt.scatter(x_val, y_val, c =y_val, cmap=plt.cm.Blues, edgecolor='none', s = 40)
plt.axis([0, 1100, 0, 1100000])

plt.show()
