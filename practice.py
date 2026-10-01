print('salary breakup')
name = input("enter name:")
age = int(input("enter age:"))
course = input("enter course:")
designation = input("enter designation:")
salary = float(input("enter salary"))
basic = float(input("enter basic:"))
hra = float(input("enter hra:"))
allowance = float(input("enter allowance:"))
is_deployed = input("deployed?:")
pf = float(input("enter pf:"))

total_salary = basic+hra+allowance-pf

print(name)
print(course)
print(total_salary)