students = {'name': 'mullai nesan', 'age': 23, 'sex': 'male', 'dep': 'mech'}
students.update({'year': 3})
print(students)
for i in students.keys():
    print(i)

key = input("please enter the key you want to search for: ")
if key in students.keys():
    print("\n the key was present")
    print("key:", key, "and value:", students[key])
else:
    print("the key was not present")