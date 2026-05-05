# 2, 4, 7, 10, 12....use function

# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.
# Once you learn functions,revisit this and write this code inside a function.

def check_number(number):

    if number % 4 == 0:
        text = "divisible by 4"
    elif number % 2 == 0:
        text = "even" 
    else:
        text = "odd"
    return text
user_number = int(input("Enter number: "))

check = check_number(user_number)

print(check)


# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
# Once you learn functions,revisit this and write this code inside a function.

def check_email(email):
    if "@" in email and "."in  email:
        text = "valid email"
    else:
        text = "invalid email"
    return text

user = input("Enter email address: ")

#calling the function
result = check_email(user)

print(result)


# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# Once you learn functions,revisit this and write this code inside a function.

def student_marks(marks):
    if marks < 0 or marks > 100:
        return "invalid marks."
    
    if marks >= 79:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "E"
    
    return grade

marks = int(input("Enter student marks (0-100): "))

result = student_marks(marks)
print("Grade:", result)




# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
# Once you learn functions,revisit this and write this code inside a function.


# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken as input from a user.
# Once you learn functions,revisit this and write this code inside a function.

def largest_number(num1, num2, num3, num4):
    if num1 > num2 and num1 > num3 and num1 > num4:
        large = num1
    if num2 > num1 and num2 > num3 and num2 > num4:
        large = num2
    if num3 > num1 and num3 > num2 and num3 > num4:
        large = num3
    else:
        large = num4
    return large


input1 = int(input("Enter first number: " ))
input2 = int(input("Enter second number: " ))
input3 = int(input("Enter third number: " ))
input4 = int(input("Enter fourth number: " ))


check1 = largest_number(input1, input2, input3, input4)
print(check1)