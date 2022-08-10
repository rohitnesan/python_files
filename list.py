# datetime_program
import datetime
current_time = datetime.datetime.now()
print(current_time)

#square_root_program
number = float(input("Enter the Number: "))
Square_root = number ** 0.5
print("The square root of %0.2f is %0.2f" % (number, Square_root))

#Area_of_triangle_program
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of triangle is %0.3f" %area)

#swap_two_variables_program
x = 10
y = 5
temp = x
x = y
y = temp
print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))

#Generate_random_number_program
import random
print(random.randint(0,5))

# celsius = 41.23
# fahrenheit = (celsius * 1.8) + 32
# print("%0.3f celsius is equal to the %0.3f fahrenheit" % (celsius, fahrenheit))

# numbers = [23, 45, 18, 51, 39, 10]
# print("before sorting: ", numbers)
# numbers.sort()
# print("after sorting: ", numbers)
# numbers.sort(reverse=True)
# print(numbers)
# print(numbers[3])
# print(len(numbers))
# a = ["mullai", 35, "nesan", 51, True]
#
# for i in a:
#     print(i)
#
# users = { "name" : "mullai", "age":24,"dep":"mech"}
# print(users["name"])

# import calendar
# year = int(input("Enter the year:"))
# month = int(input("Enter the Month:"))
# print(calendar.month(year, month))

# def cub(num):
#     return num ** 3
#
# number = int(input("Enter the number: "))
# cube = cub(number)
# print("The cube of the number {} is {}".format(number, cube))

# a = float(input("Enter the number: "))
# b = float(input("Enter the number: "))
# if a > b:
#     print("{} is greater than {}".format(a,b))
# elif b > a:
#     print("{} is greater than {}".format(b,a))
# else:
#     print("{} is equal to {}".format(a,b))

# number = int(input("Enter the number: "))
# for i in range(1, number+1, 2):
#     print(i, end=",")
#
# for i in range(1, 100):
#     if(i%2 != 0):
#         print(i, end=",")

# for i in range(2):
#     for j in range(1,16):
#         print("{} * {} = {}".format(j,i,i*j))

# for i in range(1,11):
#     num = int(input("number %d = " %i))
# sum = sum + num
# avg = sum / 10
# print(avg)

# for i in range(10,0,-1):
#     print(i, end = ',')

# for i in range(1, 21):
#     if i %2 != 0:
#         print(i)

# list1 = []
# for i in range(1, 6):
#     element = int(input("Enter a number %d: " %i))
#     list1.append(element)
# print("sum of the given numbers is {}".format(sum(list1)))
# print("Average of numbers is {}".format(sum(list1)/len(list1)))

# a = float(input("Enter the number: "))
# b = float(input("Enter the number: "))
# c = float(input("Enter the number: "))
# sum = a+b+c
# average = sum/3
# print("the sum of {},{},{} are {}".format(a,b,c,sum))
# print("the average of {},{},{} are {}".format(a,b,c,average))

# sum = 0
# for i in range(1, 11):
#     num = int(input("Number %d = " %i))
#
#     if num < 0:
#         continue
#     sum = sum + num
#
# print("The sum of the positive numbers are {}".format(sum))

# from datetime import datetime
# print("current date & time: ", datetime.today())

# character = input("Enter the Character: ")
# if(character.islower()):
#     print("The given character {} is lowercase".format(character))
# else:
#     print("The given character {} is not lowercase".format(character))

# ch = 'mullai'
# print(ch.upper())

# numbers = [1, 45, 28, 10, 39, 51]
# numbers.reverse()
# print(numbers[::-1])
# print(numbers)
# for i in range(len(numbers)):
#     # print("the value of list %d = %d" %(i,numbers[i]))
#     print(numbers[i])
# print(numbers)


# for i in range(len(numbers)):
#     print("the index no ", i, "of the list is ", numbers[i])

# numbers.append(18)
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# names = ['mullai', 'vidhya', 'rithvik']
# numbers.append(names)
# print(numbers)
# print(numbers[0])

# numbers = []
# pos_no = 0
# neg_no = 0
#
# num = int(input("Enter the numbers: "))
# for i in range(1, num+1):
#     value = int(input("the numbers are %d: " %i))
#     numbers.append(value)
# for j in range(num):
#     if(numbers[j] > 0):
#         pos_no = pos_no + 1
#     else:
#         neg_no = neg_no + 1
# print(numbers)
# print("the positive numbers are {}".format(pos_no))
# print("the negative numbers are {}".format(neg_no))

# numbers = [1,3,5,23,5,34,23,56,34,45,87]
# for i in numbers:
#     if (i %2 == 0):
#         numbers.remove(i)
# print(numbers)
# num = set(numbers)
# print(num)

values = [12,34,54,78,51,98,20]
print(values[3:-1])
# values.sort()
# print(values)
# values.sort(reverse=True)
# print(values)
# values.reverse()
# print(values)
# print(max(values))
# print(min(values))
# values.append(39)
# print(values)
# values.insert(1,89)
# print(values)
# values.pop(2)
# print(values)
# values.clear()
# print(values)




















