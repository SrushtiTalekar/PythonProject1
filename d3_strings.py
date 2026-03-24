## initialization
from os.path import split

computer_choice = "paper"

## indexing
print(computer_choice[3])
print(computer_choice[-1])

## length
print(len(computer_choice))
print(len(computer_choice))
print(computer_choice.find('z'))

## find function
str1 =  computer_choice.find('a')
print(str1)
str2 =  computer_choice.find('z')
print(str2)

## split function
text = "Srushti Talekar"
str3 = text.split()
print(str3)

## replace and reassigning or functions
text = text.replace('Srushti', 'Soumya')
print(text)

## count
str4 = text.count('a')
print (str4)
str5 = text.count('z')
print (str5)

## upper and lower cases
print(text.lower())
print(text.upper())

## swap
print(text.swapcase())

## capatilize and title
line = 'My name is Srushti Talekar'
print(line)
print(line.capitalize()) ## only 1st chr of line capital
print(line.title()) ## all 1st letters capital

## slicing
print(line[6])
print(line[0:7:2]) ## by default if not mentioned it will take start as zero and end as last index and step as one
print(line[7:0:-2])
print(line[::-1]) ## here if we put zero  in between then M was lost
print(line[-8:-15:2]) ## this doesnt work as building function works in forward direction




