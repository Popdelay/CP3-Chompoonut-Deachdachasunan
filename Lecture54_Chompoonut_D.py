def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Username หรือ Password ไม่ถูกต้อง !!!")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculator()
    elif userSelected == 2:
        return priceCalculator()

def vatCalculator():
    totalPrice = int(input("Enter price: "))
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    print(result, "THB")


def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print(price1 + price2, "THB")

login()
