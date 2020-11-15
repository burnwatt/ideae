# lists/arrays
colors = ['red', 'green', 'blue', 'black', 'yellow']
print(colors)

# accessing item in list
print(f"My favorite color is {colors[2]}")

# adding to lists
colors.append('purple')
print(colors)
colors.insert(3,'pink')
print(colors)

# removing from lists
removed_color = colors.pop()
print(f"Removing {removed_color} from list...")
print(colors)

green = colors.pop(1)
print(f"{green.title()} has been removed as well...")
print(colors)

print("Let's remove pink as well...")
colors.remove('pink')
print(colors)

# list organization

## permanent sorting
colors.sort()
print(colors)

## temporary sorting
recruits = ['Elliott', 'Angela', 'Darlene', 'Tyrell', 'Whiterose', 'Leon']
print("Original list order:")
print(recruits)
print("Sorted recruits:")
print(sorted(recruits))
print("Original order again:")
print(recruits)

## list reversal
recruits.reverse()
print("Reverse!")
print(recruits)

## list length
print(f"There are {len(recruits)} recruits in the list.")

# basic for loop for the list to name each individual recruit
print("Recruits:")
for recruit in recruits:
    print(f"\t{recruit}")
print(f"Total recruits: {len(recruits)}")

# Looping through a range of items in the list
print('First 3 recruits:')
for i in range(0,3):
    print(f'\t {recruits[i]}')