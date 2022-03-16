from tkinter import *
import math

def leftClick(event):
    CalHight = float(textBoxHight.get())
    CalWeight = float(textBoxWeight.get())
    result= CalWeight/math.pow(CalHight/100,2)
    print(result)
    if result > 30.0:
        lebelResult.configure(text="ผลลัพธ์: อ้วนมาก!")
    elif result > 25.0:
        lebelResult.configure(text="ผลลัพธ์: อ้วน!")
    elif result > 23:
        lebelResult.configure(text="ผลลัพธ์: น้ำหนักเกิน!")
    elif result > 18.6:
        lebelResult.configure(text="ผลลัพธ์: น้ำหนักปกติ เหมาะสม")
    else:
        lebelResult.configure(text="ผลลัพธ์: ผอมเกินไป!")






MainWindow = Tk()
lebelHight = Label(MainWindow, text="ส่วนสูง(cm.)")
lebelHight.grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
lebelWeight = Label(MainWindow, text="น้ำหนัก(kg.)")
lebelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow, text="คำนวณ")
calculateButton.bind('<Button-1>',leftClick)
calculateButton.grid(row=2,column=0)
lebelResult = Label(MainWindow, text="ผลลัพธ์",fg="blue")
lebelResult.grid(row=2,column=1)

MainWindow.mainloop()