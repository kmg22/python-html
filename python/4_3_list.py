# 리스트 데이터 타입
# -> 직관적인 작업 가능

# 문자열 리스트
students = ["egoing", "sori", "maru"]

# 숫자 리스트
grades = [2, 1, 4]

# index는 0부터 시작
print(students[1]) # sori

print("len(students)=", len(students)) # len(students)= 3
print("min(grades)=", min(grades)) # min(grades)= 1
print("max(grades)=", max(grades)) # max(grades)= 4
print("sum(grades)=", sum(grades)) # sum(grades)= 7

import statistics
print("statistics.mean(grades)=", statistics.mean(grades)) # statistics.mean(grades)= 2.3333333333333335

import random
print("random.choice(students)=", random.choice(students)) # random.choice(students)= sori