import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Generate random walks
rw = RandomWalk()
rw.fill_walk()

# Plot walks
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=13)
plt.show()
