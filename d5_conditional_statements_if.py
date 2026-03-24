age = int(input("Enter your age: "))
if(age>=18):
    print('eligible to vote')
print('every vote matters')



marks = int(input("Enter marks: "))
if(marks>=40):
    print('PASS')
else:
    print('FAIL')



salary = int(input("Enter your salary: "))
age = int(input("Enter your age: "))
if(age>=25 and salary>=80000):
    print('will meet you')
elif(age<25 and salary>=80000):
    print('will see')
elif(age>=25 and salary<80000):
    print('will try')
else:
    print('nope')



login = str(input("Are you user"))
if(login=="yes"):
 salary = int(input("Enter your salary: "))
 age = int(input("Enter your age: "))
 if(age>=25 and salary>=80000):
  print('WORKS GREAT')
 else:
  print('NEXT TIME')
else:
 print('Please create of credentials first')

