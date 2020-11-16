import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Generate random walks
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Plot walks
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=13)
    plt.show()

    keep_walking = input("Take another walk? (y/n): ")
    if keep_walking == 'n':
        break
