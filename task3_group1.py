# A trainer entered marks for five subjects and needs help analyzing student performance. Create a program that stores the marks in a list, calculates the average, awards grade A for averages of 70 and above, grade B for averages of 50 to 69, and grade C for anything below 50. If any subject score is below 40, display a message showing the student must retake that subject.


# subjects=["Maths, Eng, Kis, Geo, Physics"]
# marks=(50, 40, 100, 80, 70)
# avarage= sum(marks) / len(marks)

# if avarage >= 70:
#     message= "grade: A"
# elif avarage >=50 and avarage <= 69:
#     message= "grade: B"
# elif avarage <= 50 and avarage >=40:
#     message= "grade: C"
# else:
#    avarage <40
#    message="student must retake that subject."


# print(message)

# A supermarket manager needs help checking stock levels. Create a program that stores product names and quantities in a dictionary, identifies items that are completely out of stock, and also shows products with quantities below five units that need urgent restocking.

# dict={
#     'Milk':200,
#     'Bread':300,
#     'Meat':800,
#     'Flour':400,
#     'Soap':750,
# }
# if (dict['Milk'])<400:
#     print('Out of stock:Milk')
# else:
#     print('Valid stock')
# if (dict['Bread'])<400:
#     print('Out of stock:Bread')
# else:
#     print('Valid stock')
# if (dict['Meat'])<400:
#     print('Out of stock')
# else:
#     print('Valid stock:')
# if (dict['Flour'])<400:
#     print('Out of stock')
# else:
#     print('Valid stock')
# if (dict['Soap'])<400:
#     print('Out of stock')
# else:
#     print('Valid stock')

# Q4
# A company wants to secure employee accounts. Create a login system that stores a username and password, allows only three attempts, locks the account after three failed attempts, and welcomes the user when the correct credentials are entered.

# username = input("enter username: ")
# password = input("enter password: ")

# correct_username="mike"
# correct_password="1234"

# attempt = 0
# max_attempt = 3

# if password == correct_password and username == correct_username and attempt < 3:
#       print("welcome")

# # elif password != correct_password and username == correct_username and attempt >0 and max_attempt <3:
# #      print("Try again")

# else:
#     print("account locked")
    



# Q1
# An electricity company charges customers based on usage. Create a billing system where the first 100 units are charged at KES 15 each, while any additional units are charged at KES 20 each. If the final bill exceeds KES 5000, add 5% tax before displaying the total.

unit= int(input("enter user unit "))
bill= 100
# unit <= 100 == charged 15 per unit each
if unit < 100:
    bill = unit*15
    message=f"you have been charged {unit*15}ksh "
elif unit > 100:
    rem= (unit - 100)*20
    message=f"you have been charged {rem}ksh "
else:
    bill = 5000 
    message=f"you have been charged {5000*0.5 + bill}ksh"


print(message)

# unit > 100 == charged 20 per unit
# bill >5000 + 5% before displaying the total




# A retail shop wants to identify wholesale customers. Create a system that checks how many items a customer has bought. If items are more than five, reward points should be given.

# items=int(input("Enter number of items purchased: "))
# wholesale_tresh=5

# if items >5:
#     reward_point= items/ wholesale_tresh
#     res=f"you have bought {items} items you have earned {reward_point} reward points"
# else:
#     rem= wholesale_tresh - items
#     res= f"you have bought {items} items add {rem} more to earn points"

# print(res)















# user_name=input("enter the username:")
# password=input("enter password:")
# company_name=input("enter comapny name:")
# correct_password="Secret@123"
# correct_user_name="Danish"
# min_attempts=0
# max_attempts=3


# if max_attempts>3 and user_name!=correct_user_name and password!=correct_password:
#  message=f"Hello {user_name} your account{password} has been locked the account ,because{max_attempts} is more than required"
# elif min_attempts>0 and max_attempts<=3:
#  message=f" Hello{user_name} you have one remaining attempts,enter the correct{password}"
# else:
#  message=f"Hello{user_name}welcomes to {company_name},we offer diverse services"

#  print(message)