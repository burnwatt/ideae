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
