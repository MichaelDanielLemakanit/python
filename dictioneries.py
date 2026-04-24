my_dict = {
    "name":"mike",
    "age":20,
    "gender":"male",
    "city":"Nairobi"
}
print(my_dict)
print(type(my_dict))

print(my_dict["age"])

#update and add properties
my_dict['age'] =40
print(my_dict)

#add
my_dict['occupation'] = 'sofware Developer'
print(my_dict)

#dictioneries methods
#pop(remove the specific key)
my_dict.pop('gender')
#popitem(removes the last added)
my_dict.popitem()
print(my_dict)