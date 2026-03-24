num1 = 5
print(num1)
print(type(num1))
print(float(num1))

num2 = 5.8
print(num2)
print(type(num2))
print(int(num2))

num3 = 6 + 5j
print(num3)
print(type(num3))
print(int(num3.real))
print(float(num3.imag))

num = str(input("Enter an integer: "))
print('Number is ' + num )
num1 = int(num) + 11    ## whatever be the input but always input from user is treated as str so need typecast
print(num1)
