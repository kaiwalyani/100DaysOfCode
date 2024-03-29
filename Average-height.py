# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
tot_hei = 0
for height in student_heights:
  tot_hei += height 
print(f"total height = {tot_hei}")
no = len(student_heights)
print(f"number of students = {no}")
avg = round(tot_hei / no)
print(f"average height = {avg}")
