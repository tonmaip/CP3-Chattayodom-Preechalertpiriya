point = int(input("ใส่คะแนน : "))
if point > 80:
    print("Grade A")
elif point >= 75:
    print("Grade B+")
elif point >= 70:
    print("Grade B")
elif point >= 65:
    print("Grade C+")
elif point >= 60:
    print("Grade C")
elif point >= 55:
    print("Grade D+")
elif point >= 50:
    print("Grade D")
else:
    print("Grade F")
