# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

message = "WHADDUP!?"
print(message)

# simple string methods
message = 'testing string methods in python'
print(message.title())
print(message.upper())
print(message.lower())

# f-string for concatenation
first_name = 'josh'
last_name = 'burnwatt'
print(f"My name is {first_name.title()} {last_name.title()}")

# old formatting method
old_method = "This is the old way to say my name is {} {}".format(first_name.title(), last_name.title())
print(old_method)

# adding whitespace
print('No tabs')
print("\tWith tabs")

# new lines 
print('Things I like: \n\tCoding \n\tData viz \n\tSpongebob')

person = 'Turd Ferguson'
print(f"Greetings, {person}!")
print(f'{person} once said, "Look at my hat. It is funny!"')

# number methods
print(1 + 7)
print(17 - 9)
print(2 * 4)
print(16 / 2)

answer = 42
print(f"The secret to life, the universe, and everything is {answer}")
