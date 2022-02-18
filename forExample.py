
#inputRound = int(input("Pls enter Number : "))
#sum = 0
#for x in range(inputRound):
#    inputNumber = int(input("x" + str(x+1) + ":"))
#    sum = sum + inputNumber # 10
#    print("sum = " , sum)

#inputRound = int(input("Pls enter Number : "))
#sum = 1
#for x in range(inputRound):
#    inputNumber = int(input())
#    sum = sum + inputNumber # 10
#    print("sum = " , sum)
result = ""
star = int(input("1"))
step = int(input("2"))
for i in range(5):
    result += str(star + step * i + 1 )
    print(result)