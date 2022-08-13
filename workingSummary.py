print("____________________Let's Generate Today's Working Summary____________________")

employe_working_hours = input("Enter the list of working hours: ").split()

for n in range (0, len(employe_working_hours)):
    employe_working_hours[n] = int(employe_working_hours[n])

number_of_employees = 0
for employees in employe_working_hours:
    number_of_employees += 1
print(f"There are {number_of_employees} employees currently working.")

maximum_time = 0
for time in employe_working_hours:
    if time > maximum_time:
        maximum_time = time
print(f"Maximum time of working is {maximum_time} hours.")

position = (employe_working_hours.index(maximum_time)) 
which_employee = position + 1
print(f"Most hard working employee at the moment is placed as {which_employee} in the list.")

minimum_time = 1
for m_time in employe_working_hours:
    if m_time <= minimum_time:
        minimum_time = m_time
print(f"Minimum time of working is {minimum_time} hours.")

position_1 = (employe_working_hours.index(minimum_time)) 
which_employee_1 = position_1 + 1
print(f"Least hard working employee at the moment is placed as {which_employee_1} in the list.")

total_hours = 0
for that_hour in employe_working_hours:
    total_hours += that_hour
print(f"Total working hours of employees for today is {total_hours}.")

average_hours = round(total_hours/number_of_employees)
print(f"So for today....Average working hour is {average_hours}.")

if average_hours >= 6:
    print("WELDONE!!! Today is a productive Day!!!")
else:
    print("OOPS!!! You have to be more productive!!!")