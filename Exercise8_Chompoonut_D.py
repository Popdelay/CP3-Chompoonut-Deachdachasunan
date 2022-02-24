userName = input("Username:")
passWord = int(input("Password:"))

if userName == "hello" and passWord == 1234:
    print("-----Sommai Shop Welcome-----")
    print("1. Banana  20 THB")
    print("2. Water   10 THB")
    print("3. Milk    15 THB")
    print("4. Apple   25 THB")
    print("-----------------------------")
    itemList = int(input("สินค้า:"))
    quantity = int(input("จำนวนสินค้า:"))
    if itemList == 1:
        print("Total:", 20*quantity, "THB")
    elif itemList == 2:
        print("Total:", 10*quantity, "THB")
    elif itemList == 3:
        print("Total:", 15*quantity, "THB")
    elif itemList == 4:
        print("Total:", 25*quantity, "THB")
    else:
        print("ไม่มีรายการสินค้าที่คุณเลือก")
else:
    print("คุณกรอก Username หรือ Password ไม่ถูกต้อง!!")



