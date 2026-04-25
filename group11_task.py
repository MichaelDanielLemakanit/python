# Q1
# A school administration system is tracking unpaid fees. Build a program that checks student payment status and flags those with outstanding balances.
total_school_fees = int(input("amount paid: "))
amount = 5000

if total_school_fees >= amount:
    print("cleared")
elif total_school_fees <= amount:
    print("out standing balance")

# Q2
# A traffic system is monitoring speeding vehicles. Create a program that evaluates speed readings and determines whether a driver should be fined.
# speed = distance/time
speed = int(input("Enter speed: "))
limit1 = 120
limit2 = 80
if speed <= limit1 and speed >= limit2:
    print("normal speed")
elif speed >= limit1 and speed >= limit2:
    print("Over speed")
else:
    print("low speeding")


# Q3
# A website login system is being improved. Create a program that checks login credentials and determines whether a user should be granted full access, limited access, or denied entry.
user_email= input("Enter email: ")
user_password = input("enter password: ")

correct_email = "admin@gmail.com"
correct_password = "admin@123"

if user_email == correct_email and user_password == correct_password:
    print("granted full access")
elif user_email == correct_email and user_password != correct_password:
    print("limited access")
else:
    print("denied entry.")