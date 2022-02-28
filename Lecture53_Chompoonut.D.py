def vatCalculate(totalprice):
    result = totalprice + (totalprice*7/100)
    return result
numBer = int(input("กรอกราคา:"))
print(vatCalculate(numBer))

