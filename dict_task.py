
my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76, "John")]

# 1. Print KES
# Accessing index 3 (the list), then index 2 (the dictionary), then the value for key "currency"
print(type(my_ds),(560))
print(my_ds[3][2]["currency"])

# 2. Print 560
# Accessing index 2. Note: (560) in Python without a comma is treated as an integer, not a tuple.
print(my_ds[2])

# 3. Print Maths
# Accessing index 3 (the list), then index 1 within that list
print(my_ds[3][1])

# 4. In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]["amount"] = 90
print(my_ds)

# 5. Reverse 987 to 789 without using an inbuilt method or Assigning 789 manually.
# Convert to string, use slicing to reverse, and convert back to integer
my_ds[4]=str(my_ds[4])
print(type(my_ds[4]))

my_ds[4] = my_ds[4][::-1]

my_ds[4] =int(my_ds[4])
print(my_ds)
# 6. Change the name “John” to “Jane”.
# Since the last element is a tuple (76, "John"), and tuples are immutable, 
# we must replace the tuple with a new one.
temp_list = list(my_ds[5])  # Convert tuple to list
temp_list[1] = "Jane"       # Change name
my_ds[5] = tuple(temp_list) # Convert back to tuple and assign
print(my_ds[5])

# Final check of the data structure
print("\nFinal my_ds state:")
print(my_ds)