'''1.Write a Python program to find the Area of Triangle.
semi-perimeter : s=(a+b+c)/2
(formula to find area of traingle  is area = (s*(s-a)*(s-b)*(s-c))**0.5)'''


a=2
b=3
c=4
s=(a+b+c)/2
area=((s*(s-a)*(s-b)*(s-c))**0.5)
print(area)
'''2.Write a Pyhton program to capture employee details like emp_id,emp_name and emp_salary'''
my_dict={
    'emp_id':'1',
    'emp_name':'Akhil',
    'emp_salary':'20000000'

}
print(my_dict)