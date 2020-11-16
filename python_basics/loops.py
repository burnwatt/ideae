# import mean to so we don't have to write our own average function
from statistics import mean

# basic statistics
data = [i for i in range(0,30,3)]
print(data)
print(f"List length: {len(data)}")
print(f"Min: {min(data)}")
print(f"Max: {max(data)}")
print(f"Sum: {sum(data)}")
print(f"Average: {mean(data)}")
