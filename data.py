import matplotlib.pyplot as plt 

input_val = [1, 2, 3, 4, 5]
sq = [1,4, 9, 16, 25] 

plt.plot(input_val , sq,linewidth = 5)
plt.title("Sqare Numbers" , fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Sq. of Values", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()
