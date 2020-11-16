import matplotlib.pyplot as plt

inputs = range(1,5001)
cubes = [i**3 for i in inputs]

plt.style.use('fivethirtyeight')

fig,ax = plt.subplots()
ax.scatter(inputs,cubes,c=cubes,cmap=plt.cm.Blues, s=10)

# Set title and axis labels
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=13)
ax.set_ylabel("Cubed Value", fontsize=13)

# Set tick labels
ax.tick_params(axis='both', which='major', labelsize=13)

ax.axis([0,5000,0,5000**3])

# plt.show()
plt.savefig('cubes_figure.png')
