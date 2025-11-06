# Week 1 - Variables and Data Types
name = "William"
age = 23
weight = 235.0

print(f"My name is {name}, I'm {age} years old, and weigh {weight} lbs.")

is_tired = False # type: ignore

if is_tired: # type: ignore
    print("Go take a break.")
else:
    print("Keep going!")

# Variables
    # "String or str = text - anything inside quotes"
    # "Integer or int = Whole numbers - no decimals"
    # "Float or float = Numbers with decimals"
    # "Boolean or bool = True or False - for logic or decisions"
    # "List or list = An ordered collection - like a box that can hold multiple values"
    # "Dictionary or dict = key-value pairs - like a mini database"
    # "Tuple or tuple = like a list, but unchangeable (immutable)"
    # "Set or set = Unordered, unique collection - automatically removes duplicates"
    # "NoneType = represents 'nothing' or 'no value'"

qoute = "Knowledge is power."

print(qoute.upper()) # Makes it ALL CAPS
print(qoute.lower()) # all lowercase
print(qoute.title()) # Capitalizes Each Word
print(qoute.replace("power", "freedom")) # swaps words
print(len(qoute)) # counts characters

# Condtionals
    # if condition:
        # do this if condition is True
    # elif another_condition:
        # do this instead
    # else:
        # do this if everything above is False

if age >= 21:
    print("You can drink legally")
elif age >= 18:
    print("You can vote, but no beer yet.")
else:
    print("You're still underage.")

# Logic Operators
    # And - both must be true
    # Or - at least one must be true
    # not - reverses True/False

# Loops
    #Loops - repeat a block of code multiple times; either
        # a fixed number of times, or
        # until a condtiion changes.
    
    # for loops - repeat for every item in a list, range, or sequence
    # while loops - repeat as long as a condition is true.

for i in range(5):
    print("Hello, world!")

tools = ["Python", "Git", "VS Code"]

for tool in tools:
    print(f"I'm using {tool}.")

energy = 3
cycles = 0
WorkDone = False

while not WorkDone and energy > 0:
    print("Still coding...")
    energy -= 1 # subtract 1 each loop
    cycles += 1 # add 1 cycle each loop
    if energy <= 0:
        print("taking a break")
        energy += 1 # add 1 each loop
    if cycles == 5:
        WorkDone = True
        
print(f"Work completed after {cycles} cycles.")
