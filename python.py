


#comparision operators
a = 10
b = 20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#age eligibility check
age = int(input("enter you age"))

print("eligibile:",age >= 18)

#pass or fail checker
marks = int (input("enter marks"))
print("passed:", marks >=40)

#login validation
correct_username = "admin"
correct_password = "1234"
username = input("enter usename:")
password = input ("enter password:")
print(username==correct_username)
print(password==correct_password)

#logical operators
age = 25
citizen = True
print(age>=18 and citizen== True )

has_card=False
has_card=True
print(has_card or has_card)

is_logged_in = True
print(not is_logged_in)

#atm eligibility checker
balance = 10000
withdraw = 5000
print(withdraw > 0 and withdraw <= balance)

#studends scholorship eligibility checker
marks = float(input("enter marks:"))
attendence = float(input("enter attendence:"))
eligible = marks>=85 and attendence>=75
print("scholoship eligible:",eligible)

#identity operator
a=None
print(a is None)
print(a is not None)

#bitwise operators
a = 8
b = 6
print(a&b)
print(a|b)
print(a^b)
print(a<<b)
print(a>>b)