# Q1
# A school administration system is tracking unpaid fees. Build a program that checks student payment status and flags those with outstanding balances.
total_school_fees = int(input("Amount paid: "))
amount = 5000

if total_school_fees >= amount:
    status = "cleared"
else:
    status = "out standing balance"

print(status)

# Q2
# A traffic system is monitoring speeding vehicles. Create a program that evaluates speed readings and determines whether a driver should be fined.
# speed = distance/time
speed = int(input("Enter speed: "))
limit1 = 120
limit2 = 80

if speed > limit1:
    message = "Over speed"
elif speed >= limit2:
    message = "normal speed"
else:
    message = "low speeding"

print(message)


# Q3
# A website login system is being improved. Create a program that checks login credentials and determines whether a user should be granted full access, limited access, or denied entry.
user_email = input("Enter email: ")
user_password = input("Enter password: ")

correct_email = "admin@gmail.com"
correct_password = "admin@123"

# Determine access level
if user_email == correct_email:
    if user_password == correct_password:
        access_status = "granted full access"
    else:
        access_status = "limited access"
else:
    access_status = "denied entry."

# Single output at the end
print(access_status)