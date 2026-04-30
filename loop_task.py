# Write a program that displays a numbers 1 to 50 inside a list.
number = list(range(1, 50))
result = []

for i in number:
    result.append(i)


print(result)

# From 1 above display the ones divisible by 7 or 5 inside a list.
number = list(range(1, 50))
result = []

for i in number:
    if i % 7 == 0 and i % 5 == 0: 
       result.append(i)

print(result)

# Find sum and average of values in the range between 10 to 40.
number = list(range(10, 40))
total_sum = 0

for i in number:
    total_sum = total_sum +i

number_len =len(number)
avarage = total_sum / number_len

print("sum:", total_sum)
print("avarage:", avarage)


# Put in a list the first 10 odd numbers between 10 to 50. 

number = list(range(10, 50,))
result = []

for i in number:
    if i % 2 !=0:
        result.__len__(i)
print(result)




# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# Display the total quantity of the 3 above.

