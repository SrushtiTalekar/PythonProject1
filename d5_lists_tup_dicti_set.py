list1 = [1,2,'why',4,5,'howw']
print(list1)
print(type(list1))
print(list1[2])
list1 = [1,2,'3',4,5,'6']
print(list1)

tuple1 = (1,2,3,4,5,6)
print(tuple1)
print(type(tuple1))

set1 ={1,2,3,4,5,6}
print(set1)
print(type(set1))

set2 = {1,2,3,4,5,6,6} ## duplicates will be removed
print(set2)
print(type(set2))

## list to set bcz we want to remove duplicates from list interview que, how to remove duplicates from list given
list3 = [1, 1, 2, 2, 3, 3]
print(set(list3))

dict3 = {} ## if empty flower bracket it will consider as dict and not set
print(type(dict3))

details = {"name":"srushti", "age":20, "city":"New York"}
print(details)
print(type(details))
print(details["name"])
details["address"] = "church road"
print(details)