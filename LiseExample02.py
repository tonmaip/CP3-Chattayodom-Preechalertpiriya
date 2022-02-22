menuList = []
systemPriceList = {"หมูทอด":100 , "ไก่ทอด" : 200}

def showBill():
    allPrice = 0
    print("------My FooD------")
    for number in range(len(menuList)):
        print(menuList[number] [0], menuList[number][1])
        allPrice += int(menuList[number][1])
    print("_________________"
    print("Total Price : ",allPrice ,"THB")

while True:
    menuName = input("Pls Enter Menu : ")
    if(menuName .lower() == 'exit'):
        break
    else:
        menuList.append([menuName,systemPriceList[menuName]])

print(menuList)
showBill()


# อีกแบบ
#menuList = []
#priceList = []

#while True:
#    menuName = input("Pls Enter Menu : ")
#    if(menuName .lower() == 'exit'):
#        break
#    else:
#        menuPrice = input("Price : ")
#        menuList.append(menuName)
#        priceList.append(menuPrice)

#def showBill():
#    print("------My FooD------")
#    for food in menuList:
#        print(food, calulatePrice())




