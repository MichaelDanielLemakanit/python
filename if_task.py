# Write a program that:
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."
# Otherwise “Wrong account type”

amount = float(input("Enter transaction amount: "))
account_type = input("Enter account type (Standard or Premium): ").lower()

if account_type == "standard":
    if amount > 500:
        res="Transaction exceeds the limit for Standard accounts"
    else:
        res="Transaction approved."
else:
    if account_type == "premium":
        if amount > 1000:
            res="Transaction exceeds the limit for Premium accounts."
        else:
            res="Transaction approved"
    else:
        res="wrong account type"

print(res)



# 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
# If start_date comes before end_date, print "Valid period",
# If start_date is after end_date, print "Invalid period".
# If both dates are the same, print "One-day period".

start_date = '2024-01-02' 
end_date = '2024-12-31'
day= int(input("enter day to start the project: "))
month= int(input("enter month to start the project: "))

if day < 31 and month < 12:
    print("valid period")
elif day > 31 and month > 12:
    print("invalid period")
else:
    day == 31 and month == 12
    print("one-day period")


# 2.Given two strings str1 and str2, write a conditional statement that checks:
# If str1 is longer than str2, print "str1 is longer".
# If str2 is longer than str1, print "str2 is longer".
# If both have equal length, print "Both are of equal length".

str1= str(input("enter your first name: "))
str2= str(input("enter your second name: "))

if len(str1) > len(str2):
    print("first name is longer")

elif len(str2) > len(str1):
    print("second name is longer")

else:
    len(str2) == len(str1)
    print("Both names size are equal")


# 3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# Prints "Access Granted" if user_id is in valid_ids.
# Prints "Access Denied" if user_id is not in valid_ids.

valid_ids = [101, 102, 103] 
user_id = int(input("enter user id: "))

if user_id in valid_ids:
    print("access granted")

else:
    print("access dinied")

# 4.Given a variable value that could be of any type, write a conditional statement that:
# Prints "String Detected" if value is a string.
# Prints "Integer Detected" if value is an integer.
# Prints "Unknown Type" for any other type.

data_input = eval(input("Enter something: "))

print(type(data_input))

# 5.Given x = 7 and y = 14, write nested conditional statements that print:
# "x and y are both even" if both x and y are even numbers.
# "Only y is even" if only y is even.
# "Neither x nor y are even" if both are odd.

x = 7
y = 14

if x % 2 == 0:
    if y % 2 == 0:
        print("x and y are both even")
    else:
        print("Only x is even")
else:
    if y % 2 == 0:
        print("Only y is even")
    else:
        print("Neither x nor y are even")
