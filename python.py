a =17
b = 5
print("Addition:", a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Floor Division:",a//b)
print("Remainder:",a%b)
print("Power:",a**b)

#simple calcuater
a =int(input("enter first number"))
b =int(input("enter second number"))

print("Addition:", a + b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)

#student marks calculator
name = input("enter student name:")

a = int(input("enter python marks:"))
b = int(input("enter java marks:"))
c = int(input("enter SQL marks:"))
total = a+b+c
average = total/3
print("total = ", total)
print("average = ", average)

#shopping bill calculater
price1 =float(input("enter product 1 price:"))
price2 = float(input("enter product 2 price:"))
price3 =float(input("enter product 3 price:"))

totol = price1 + price2 + price3 

discount = total * 0.50
final_amount = total - discount
print("total:",total)
print("discount:",discount)
print("final amount:",final_amount)

#salary calculator
basic = float(input("enter basic salary:"))
hra = basic * 0.30
da = basic * 0.20
gross_salary = basic + hra + da
print("basic salary:",basic)
print("HRA:",hra)
print("DA:",da)
print("gross salary:",gross_salary)

 #assignment operators
x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

x //= 2
print(x)
