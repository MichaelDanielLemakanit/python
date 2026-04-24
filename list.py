fruit=['orange','banana', 'mango', 'lemon']
print(type(fruit))
print(fruit)
print(fruit[1])
#update
fruit[1]='apple'
print(fruit)
#slice
print(fruit[2:])

my_list=["mike", "jane", "alex", 1000, 200, 2000, True, False]

my_list.append('donkey')
print(my_list)

#insert add an item at a specific index
my_list.pop(3)
print(my_list)

#task
lst = [10, 20, 30, ['jane', 'Mary', [1000, 2000, 3000]], 40, 50, 60]
lst.append(70)

print(lst)

lst[3][2].insert(1, 1500)

print(lst)

lst[3][2].remove(2000)

print(lst)

#sort
lst1=[1, 50, 10, 20, 5, 2]
lst1.sort(reverse=True)
print(lst1)

lst2 = ['mike', 'jane', 'alex']
lst2.sort()
print(lst2)

#remove
lst2.remove('alex')
print(lst2)

#extend
lst2 = ['mike', 'jane', 'alex']
lst1 = [1,50,10,20,5,2]
lst3=lst2+lst1
lst2.extend(lst1)
print(lst3)

#count
print(lst2.count('Mike'))
#copy
lst4=lst1.copy()
print(lst4)

traninees = ['john', [2, ['james','mary']]]
print(traninees[1][0])

print(traninees[1][1][0])

traninees.append(56)
print(traninees)

traninees[1][1].insert(1, 'mike')
print(traninees)


traninees[1][0]=8
print(traninees)

traninees.pop(0)
print(traninees)

traninees[0][1].pop()
print(traninees)

print(len(traninees))