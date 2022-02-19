#userInput = int(input("pyramid H : "))
#for x in range(userInput):
#    text = ""
#    for y in range(x + 1):
#        text = "*" + text * 2
#    print(text)


#userInput = int(input("pyramid H : "))
#for x in range(userInput):
#    text = ""
#    for y in range(x + 1):
#        text = "*" + text * 2
#        print(" " * (userInput - x), "*" * ((x * 2) + 1))


userInput = int(input("pyramid H : "))
for x in range(userInput):
    print((userInput - x) * " " + ((2*x)-1)*"*")



for i in range(5):
    print(i,end=":)")
