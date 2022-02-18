#UserInputNumber = int(input("InputNumber"))
#print(str(UserInputNumber) + UserInputNumber * "*" )

#text = ""
#Number = int(input())
#for i in range(Number):
#    text = text + "*"

#    print(text)


Number = int(input())
for x in range (Number):
    text = ""
    for y in range(x+1):
        text += "*"
print(text)

#Number = int(input())
#for x in range (Number):
#    print("*" * (x + 1))
