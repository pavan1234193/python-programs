m=int(input("Marks in math:"))
s=int(input("Marks in Science:"))
e=int(input("Marks in English:"))
total_marks = m+s+e
average=total_marks/3
percentage=(total_marks/300)*100
grade=""
if percentage>90:
    grade="A+"
elif percentage>80 and percentage<=90:
    grade="A"
elif percentage>70 and percentage<=80:
    grade="B"
else:
    grade="pass"
print(f"Total Marks: {total_marks}\n Average Marks: {average}\n Grade: {grade}")