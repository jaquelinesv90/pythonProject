name = input("type a name: ")
age = int(input("type an age: "))
salary = int(input("type a salary: "))
gender = int(input("type an age: "))
maritalStatus = input("type a marital status: ")

if len(name) < 3:
    print("minimum is 3 letters")

if age < 0 or age > 150:
    print("error at age")
