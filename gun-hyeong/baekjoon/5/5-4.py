exam = []
for i in range(10):
    n = int(input())
    exam.append(n%42)
print(len(set(exam)))