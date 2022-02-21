tupleExample = ('GeGee' ,'Kaijeaw' , 'ChokDee')
print(tupleExample)
tupleExample2 = ('bank', 'Kai')
tupleExample3 = tupleExample + tupleExample2
print(tupleExample3)
print(tupleExample3[:2])
print('bank' in tupleExample3) # ดูว่า 'bank' อยู่ใน tuple นั้นมั้ยถ้าใช่จะprint ออกมาเป็น True
for i in tupleExample3:
    print("Hello",i)



#tuple แก้ไม่ได้ ใช้ () ต่างจาก list แก้ได้ใช้ []
