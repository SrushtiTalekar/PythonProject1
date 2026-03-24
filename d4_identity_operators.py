x = 20
y = 20
z = x + y
print(x is y)
print(x is z)
print(id(z))
print(id(x))
print(id(y))

str1 = 'hii'
str2 = 'hie'
str3 = 'hie'
print(str1 is str2)
print(str2 is str3)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2)  ## in collection this doesnt work