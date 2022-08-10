num = (12,43,23,67,45,24,90,67,78,67)
print(num[2:4])
for i in num:
    print(i)
num = num + (34,)
print(num)
print(min(num))
evenno = 0
oddno = 0
for i in range(len(num)):
    if (num[i] %2 == 0):
        evenno= evenno + num[i]
    else:
        oddno = oddno + num[i]
print(evenno)
print(oddno)
