days_of_the_week=('Sunday', 'Monday','Tuesday','Wenesday','Thursday','Friday','Sarturday')

print(type(days_of_the_week))
print(days_of_the_week[1])
print(days_of_the_week[2:4])
#way one
print(days_of_the_week[6])
#other way
print(days_of_the_week[-1])
#display thurday to sataday
print(days_of_the_week[4:7])

#convert tuple to list. list()
days_of_the_week=week.list(days_of_the_week)
print(type(days_of_the_week))
#modify
days_of_the_week[2]='Tuesday'

#convert back to a tuple()
days_of_the_week=tuple(days_of_the_week)
print(days_of_the_week)


# 1. Display "Sun" to "Sunday"
print(f"{days_of_the_week[0][:3]} to {days_of_the_week[0]}")

# 2. Correct way to convert to list (use list(), not weeklist)
temp_list = list(days_of_the_week)

# 3. Modify the typos while it's a list
temp_list[3] = 'Wednesday'
temp_list[6] = 'Saturday'

# 4. Convert back to tuple and ADD 'Jan'
days_of_the_week = tuple(temp_list) + ('Jan',)

print(days_of_the_week)