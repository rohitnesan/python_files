my_set = {12,15,29,48,39,57,12}
print(my_set)
my_set.add(45)
print(my_set)
# for i in my_set:
#     print(i)
my_set.remove(15)
print(my_set)
my_set.update({67,89},"hello")
print(my_set)
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b)) #|
print(a.intersection(b)) #&
print(a.difference(b)) #-
print(a.symmetric_difference(b)) #^
# my_set.clear()
print(my_set)

