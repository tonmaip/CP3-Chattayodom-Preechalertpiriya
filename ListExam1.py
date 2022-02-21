menuList = []
priceList = []


def showBill():
    print("------My FooD------")
    totalPriceList = 0
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        totalPriceList += int(priceList[number])
    print("Total :" , totalPriceList)
while True:
    menuName = input("Pls Enter Menu : ")
    if(menuName .lower() == 'exit'):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

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




