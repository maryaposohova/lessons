#Практическая работа по уроку "Динамическая типизация"

name = 'Marya'
print('Name: ' + name)
age = 44
print('Age:', age)
age = age+1
print('New age:', age)
# is_student= age<age+1
is_student = age == age
print('Is_student:', is_student)


name = 'Marya'
print('Name: ' + name)
age = 44
print('Age:', age)
age = age+1
new_age = 45
print('New age:', age)
# is_student= age<age+1
is_student = new_age == age
print('Is_student:', is_student)

