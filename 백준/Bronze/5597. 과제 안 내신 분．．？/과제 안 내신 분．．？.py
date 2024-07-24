student=[]
n_student=[]
for i in range(28):
    s=int(input())
    student.append(s)
for i in range(1,31):
    if i not in student:
        n_student.append(i)
print(min(n_student))
print(max(n_student))