import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Generate random walks
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Plot walks
    plt.style.use('seaborn-dark-palette')
    fig, ax = plt.subplots(figsize=(12,6), dpi=128)
    point_nums = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    # emphasis on the starting and ending points
    ax.scatter(0,0,c='green', edgecolors='none', s=42)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=42)

    # Remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_walking = input("Take another walk? (y/n): ")
    if keep_walking == 'n':
        break
