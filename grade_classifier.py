# A report card

full_name = input("Enter your fullname: ")

#Grade for 3 subject
maths = float(input("Enter your Math marks: "))
programming = float(input("Enter your Programming marks: "))
database = float(input("Enter your database marks: "))

avg_mark = (maths + programming + database) / 3
print(float(round(avg_mark,2)))

if avg_mark >= 80:
    grade = 'A'
elif avg_mark >= 70 and avg_mark < 80:
    grade = 'B'
elif avg_mark >= 60 and avg_mark < 70:
    grade = 'C'
elif avg_mark >= 50 and avg_mark < 60:
    grade = 'D'
else:
    grade = 'F'

# Assign status Fail/Pass
if avg_mark >= 50:
    status = "Pass"
else:
    status = "Fail"


# Individual marks falg
flag1 = "Needs Intervention" if maths < 40 else " "
flag2 = "Needs Intervention" if programming < 40 else " "
flag3 = "Needs Intervention" if database < 40 else " "



#Report Card
print("\nReport card: ")
print("\n*****************************************")
print(f"Student Name: {full_name.title()}")
print("="*30)
print("Subject Marks: ")
print(f"Maths: {maths:.2f}% {flag1}")
print(f"Programming: {programming:.2f}% {flag2}")
print(f"Database: {database:.2f}% {flag3}")
print("="*30)
print("Performance Summary: ")
print(f"- Average Mark: {round(avg_mark, 2)}")
print(f"- Grade Letter: {grade}")
print(f"- Status: {status}")
print("="*40)