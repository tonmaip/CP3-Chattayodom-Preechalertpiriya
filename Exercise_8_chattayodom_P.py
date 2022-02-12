print("Wecome To Tonmai Shop :")
print("------------------------------------")
Username = input("Username : ")
Password = input("Password : ")

if Username == "tm" and Password == "12345":
    print("What Do you want to Eat")
    print("No.1","  ข้าวหมูทอด          " ,"50" ,"THB")
    print("No.2", " ข้าวหมูทอด + ไข่ดาว  ", "65", "THB")
    print("No.3", " ข้าวมันไก่           ", "50", "THB")
    print("No.4", " ข้าวขาหมู           ", "50", "THB")
    print("No.5", " น้ำดื้ม ตราสิงโตร้องไห้ ", "10", "THB")

    print("เลขเมนูที่ต้องการ 1,2,3,4,5")
    Food = input("ใส่เลขเมนูอาหาร :")
    if Food == "1":
        print("No.1","  ข้าวหมูทอด          " ,"50" ,"THB")
        manu1 = int(input("ใส่จำนวนที่ตองการ"))
        print("No.1","  ข้าวหมูทอด          " ,manu1 ,manu1*50,"THB")

    elif Food == "2":
        print("No.2", " ข้าวหมูทอด + ไข่ดาว  ", "65", "THB")
        manu2 = int(input("ใส่จำนวนที่ตองการ"))
        print("No.2", " ข้าวหมูทอด + ไข่ดาว  ", manu2, manu2 * 65, "THB")

    elif Food == "3":
        print("No.3", "ข้าวมันไก่            ", "50", "THB")
        manu3 = int(input("ใส่จำนวนที่ตองการ"))
        print("No.3", " ข้าวหมูทอด + ไข่ดาว  ", manu3, manu3 * 50, "THB")

    elif Food == "4":
        print("No.4", " ข้าวขาหมู           ", "50", "THB")
        manu4 = int(input("ใส่จำนวนที่ตองการ"))
        print("No.4", " ข้าวขาหมู           ", manu4, manu4 * 50, "THB")

    elif Food == "5":
        print("No.5", " น้ำดื้ม ตราสิงโตร้องไห้ ", "10", "THB")
        manu4 = int(input("ใส่จำนวนที่ตองการ"))
        print("No.5", " น้ำดื้ม ตราสิงโตร้องไห้ ", manu5, manu5 * 10, "THB")

    else:"Thank You"

