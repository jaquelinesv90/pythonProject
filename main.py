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
