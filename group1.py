# Q1
# A bank wants to improve its ATM service. Create a program that stores a customer’s name and account balance, then allows them to request a withdrawal. If the amount requested is greater than the available balance, the transaction should fail. If successful, deduct the amount together with a transaction fee of KES 30 and display the new balance.
# customers_name=input("Enter customer's name: ")
# account_balance=int(input("Account balance"))
# transaction_fee=30
# amount_requested=int(input("enter withrawal amount: "))

# if amount_requested >= account_balance:
#     print("failed transaction due to  insufient funds")
# else:
#     amount_requested <= account_balance
#     print("widrawa the amount")


# Q2
# A trainer entered marks for five subjects and needs help analyzing student performance. Create a program that stores the marks in a list, calculates the average, awards grade A for averages of 70 and above, grade B for averages of 50 to 69, and grade C for anything below 50. If any subject score is below 40, display a message showing the student must retake that subject.

subjects=["Maths, Eng, Kis, Geo, Physics"]
marks=[]

print("enter marks for 5 subjects: ")