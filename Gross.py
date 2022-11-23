# d_A , t_A , h_R_A

basic_Salary =  int(input("Enter the Salary of an employee :"))
d_A = int(basic_Salary*80)/100
t_A = int(basic_Salary*10)/100
h_R_A = 6050
gross_salary = basic_Salary + d_A + h_R_A + t_A
print("gross_salary = ",gross_salary)