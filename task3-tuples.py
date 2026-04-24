# # create a new file tuples_task.py
# 1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
numbers=(10, 20, 30, 40, 50)
number_list= list(numbers)

#adding 60 to the end using append
number_list.append(60)

#replacing 30 with 35
number_list[2]=35

#convering back to tuple
numbers=tuple(number_list)

print(numbers)
# 2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
Values = (15, 5, 30, 25, 10)

sorted_values = sorted(Values)
print(sorted_values)

# 3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
fruit=fruits.count("banana")

print(fruit)
# remove Count occurrences of "banana",Remove all occurrences of "banana".
fruits_new_list= list(fruits)
del fruits_new_list [5], fruits_new_list [3], fruits_new_list [1]

print(fruits_new_list)

# 4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort method.
names = ("Alice", "Bob", "Charlie", "David")

# 1. Convert the tuple to a list (a must for .sort())
names_list = list(names)

# 2. Use the sort method with reverse=True
# This sorts alphabetically Z -> A
names_list.sort(reverse=True)

# 3. Convert back to a tuple
names = tuple(names_list)

print(names)
# Output: ('David', 'Charlie', 'Bob', 'Alice')

# 5. colors = ("red", "blue", "green")add "yellow" at index 1,Extend with ["purple", "orange"]
colors = ("red", "blue", "green")

# Step 1: Convert to a list
colors_list = list(colors)

# Step 2: Add "yellow" at index 1
# .insert(index, value) puts the item exactly where you want it
colors_list.insert(1, "yellow")

# Step 3: Extend with ["purple", "orange"]
# .extend() adds multiple items from another list to the end
colors_list.extend(["purple", "orange"])

# Step 4: Convert back to tuple
colors = tuple(colors_list)

print(colors)
# Output: ('red', 'yellow', 'blue', 'green', 'purple', 'orange')
# Output: ('red', 'yellow', 'blue', 'green', 'purple', 'orange')
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
