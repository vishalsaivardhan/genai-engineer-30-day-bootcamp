# Task-05 : Salary Calculator

#input
Baisc_Salary = float(input("Enter basic salary : "))
HRA_percentage = float(input("Enter HRA percentage : "))
DA_percentage = float(input("Enter DA percentage : "))

#process
HRA = Baisc_Salary * HRA_percentage / 100
DA = Baisc_Salary * DA_percentage / 100
Gross_salary = Baisc_Salary + HRA + DA

#output
print("Your gross salary is : ",Gross_salary)