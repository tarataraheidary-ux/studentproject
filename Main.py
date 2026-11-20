from Student import average, maximum, get_status

name = input("Enter student name: ")
grades = [20, 15, 17, 18]

avg = average(grades)

print("student:", name)
print("Avg =", avg)
print("max =", maximum(grades))
print("status =", get_status(avg))
