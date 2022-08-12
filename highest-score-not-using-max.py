student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max_val = 0

for x in student_scores:
    if x > max_val:
        max_val = x
print("The highest score in the class is:", max_val)
