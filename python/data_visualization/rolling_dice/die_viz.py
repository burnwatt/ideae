from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die 

# create die
die = Die()

# ROLL DEM BONES!!!!
rolls = []
for roll in range(1000):
    result = die.roll()
    rolls.append(result)

# Analyze rolls
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = rolls.count(value)
    frequencies.append(frequency)

# Visualize results
x_values = list(range(1,die.num_sides+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
layout_config = Layout(title='Results of rolling one D6 die 1000 times',
                        xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout':layout_config},filename='d6.html')