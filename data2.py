import matplotlib.pyplot as plt

x_val = [1, 2, 3, 4, 5]
y = [x**2 for x in x_val]

plt.scatter(x_val , y , edgecolor='none', s =40)
plt.axis([0, 6, 0, 36])
plt.show()
