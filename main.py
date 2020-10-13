import sys
import datetime

print("Python version")
print(sys.version)

now = datetime.datetime.now()
print("current date and time : ")
print(now.strftime("%Y -%m -%d %H:%M:%S"))


for item in['Mosh','John','Sarah']:
    print(item)

#imprime cada letra em uma linha
for item in 'Python':
    print(item)

for item in [1,2,3,4]:
    print(item)

prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")


name = input("type a name: ")

if len(name) < 3:
    print("name:minimum is 3 letters")

age = int(input("type an age: "))
if age < 0 or age > 150:
    print("error at age")

salary = int(input("type a salary: "))
if salary == 0:
    print("salary should be more than 0")

gender = input("type an gender: ")
if gender != 'f' and gender != 'm':
    print("error gender")

maritalStatus = input("type a marital status: ")
if maritalStatus != 's' or maritalStatus != 'c' or\
        maritalStatus != 'v' or maritalStatus != 'd':
    print("marital status invalid")
