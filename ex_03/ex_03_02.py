score = input("Enter Score: ")
s = float(score)
if s > 1.0:
    grade = "Error"
elif s < 0:
    grade = "Error"
elif s >= 0.9:
    grade = "A"
elif s >= 0.8:
    grade = "B"
elif s >= 0.7:
    grade = "C"
elif s >= 0.6:
    grade = "D"
elif s < 0.6:
    grade = "F"

print(grade)