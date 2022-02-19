def LogIN():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "tonmai" and passwordInput == "12345":
        return True
    else:
        return  False

def ShowMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def MenuSelect():
    userSelected = int(input(">>"))
    return userSelected
def VatCalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result
def PriceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return VatCalculate(price1 + price2)

print("Wecome to Shop Please LogIN")
while LogIN() != True:
    LogIN()
ShowMenu()

OpenMenu = MenuSelect()
if OpenMenu == 1:
    print(VatCalculate(int(input("Input Price : "))))

elif OpenMenu == 2:
    print(PriceCalculate())