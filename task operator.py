# Take three inputs from a user, separately. Print the largest of the numbers.
user1 =int(input('enter user1:'))
user2 =int(input('enter user2:'))
user3 =int(input('enter user3:'))
if user1 >= user2 and user1 >= user3:
    largest = user1
elif user2 >=user1 and user2 >= user3:
    largest = user2
else:
    largest = user3
print('The largest number is:', largest)


user1 =int(input('enter user1:'))
user2 =int(input('enter user2:'))
user3 =int(input('enter user3:'))
user4 =int(input('enter user4:'))
if user1 >= user2 and user1 >= user3 and user1 >= user4:
    largest = user1
elif user2 >= user1 and user2 >= user3 and user2 >= user4:
    largest = user2
elif user3 >= user1 and user3 >= user2 and user3 >= user4:
    largest = user3
else:
    largest = user4

print('The largest number is:', largest)



#     Hint: Determine what type of data is taken in as input.
# 2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”

temp=float(input("enter temperature: "))
if temp>30:
    print("The temperature is too high")
elif temp>15 and temp<=39:
    print("Normal temperature")
else:
    print("coold temperature")


user= int(input("user balancee: "))
if user<100 :
    print("insufficient fund")
elif 100 <= user <= 1000:
    print("Moderate balance")
else:
    print("high balamce")


# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x = 10 and 20
y = 100
if 10>=x <=20 and y>100:
    print("Condition are met")
else:
    print("conditions not met")


x = 10 and 20
y = 100
if 10>=x <=20 and y>100:
    print("Condition are met")
elif 
else:
    print("conditions not met")


# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password = "my_password"  
if password == "secret123":
    print("Access granted")
else:
    print("Access denied")

# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"

# 1. Ask the user for email and password
email = input("Enter your email: ")
password = input("Enter the password: ")

# 2. Check if both conditions are met
if email == "admin@gmail.com" and password == "admin123":
    print("Access granted")
else:
    print("Access Denied")