li = ["geeks", "for", "geeks"]
for x in li:
    print(x)
    
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)
    
s = "abc"
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
for x in set1:
    print(x),

#display even number btw 10 and 100
for i in range(10, 101, 2):
    print(i)
numbers = list(range(10, 101))
result = []
for i in numbers:
    if i%2==0:
        result.append(i)
print(result)

# #display number divisible by 3 and 7 from 1 to 100
numbers = list(range(1, 101))
result = []

for i in numbers:
    if i%3==0 and i%7 ==0:
        result.append(i)

print(result)

tries=3
attempts=list(range(1,4))

for i in attempts:
	pin=input('Enter pin:')
	correct_pin='1234'
	if pin==correct_pin:
		print("Welcome")
		break
	else:
		remaining_tries=tries-i
		if remaining_tries>0:
			print(f'incorrect pin try again {remaining_tries} tries remaining')
		else:
			print("account Blocked")