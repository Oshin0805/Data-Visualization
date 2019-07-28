import matplotlib.pyplot as plot

plot.scatter(2, 4, s=200)

plot.title("Sq. numb." ,fontsize = 20)
plot.xlabel("Sq num",fontsize=15)
plot.ylabel("value" , fontsize = 15)

plot.tick_params(axis = 'both' , which = 'major' , labelsize=14)

plot.show()
