import matplotlib.pyplot as plt

inputs = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# initialize our chart
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(inputs, squares, linewidth=3)

# Set title and axis labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=13)
ax.set_ylabel("Square of Value", fontsize=13)

# Set tick labels
ax.tick_params(axis='both', labelsize=13)

plt.show()
