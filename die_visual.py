from die import Die
import pygal

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)

freqs = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result +1):
    freq = results.count(value)
    freqs.append(freq)

#print(freqs)

hist = pygal.Bar()

hist.title = "Results of rolling two D6 100 times."
hist.x_label = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', freqs)
hist.render_to_file('die_visual.svg')
