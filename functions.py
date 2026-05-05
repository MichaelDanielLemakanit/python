# creat the function that triangle the area of a triangle 

def triangle_area(base, height):
    area = 0.5* base * height
    print(area)
# area = 22/7 * 2 * radius
triangle_area(20, 40)

# creat the function that calculate the area of a cicle 

def cicle_area(radius):
    pie = 3.142
    area = pie * radius**2
    print(area)
# area = 22/7 * 2 * radius
cicle_area(20)

def hello(name):
    print(f"Hello {name}")

hello("mike")
hello("kevin")
hello("juma")

#creat a function that clculate the area of a triangle
def area_rectangle(l,w):
    area = l*w
    print(area)

area_rectangle(10,20)
area_rectangle(50,10)


def largest_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        large = num1
    if num2 > num1 and num2 > num3:
        large = num2
    else:
        large = num3
    return large


input1 = int(input("Enter first number: " ))
input2 = int(input("Enter second number: " ))
input3 = int(input("Enter third number: " ))


check1 = largest_number(input1, input2, input3)
print(check1)

#task