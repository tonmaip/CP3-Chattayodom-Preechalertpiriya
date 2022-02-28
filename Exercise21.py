from tkinter import *
import math

def leftClickButton(event):
    theresult = float(textBoxweight.get()) / math.pow(float(textBoxhight.get()) / 100, 2)
    if theresult > 30 :
        lablelResult.configure(text= "อ้วนมากๆ")

    elif theresult > 25 and theresult < 29.9:
        lablelResult.configure(text="อ้วน")

    elif theresult > 23 and theresult < 25.9:
        lablelResult.configure(text="น้ำหนักเกิน")

    elif  theresult > 18.6 and theresult < 22.9:
        lablelResult.configure(text="น้ำหนักปกติ เหมาะสม")

    elif theresult < 18:
        lablelResult.configure(text="ผอมเกินไป")

    else:
        print("กดใหม่")




MainWindow = Tk()
lablelHight = Label(MainWindow, text="ส่วนสูง (cm.)")
lablelHight.grid(row=0,column=0)
textBoxhight = Entry(MainWindow)
textBoxhight.grid(row=0, column=1)
lablelweight = Label(MainWindow, text="น้ำหนัก (Kg.)")
lablelweight.grid(row=1, column=0)
textBoxweight = Entry(MainWindow)
textBoxweight.grid(row=1,column = 1)

calculateButton = Button(MainWindow, text= "คำนวณ")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
lablelResult = Label(MainWindow, text="ผลลัพธ์ BMI ")
lablelResult.grid(row=2,column=1)
MainWindow.mainloop()
