def Calulate(totalprice):
    result  = totalprice + (totalprice * 7 / 100)
    return result

print(Calulate(int(input("In Put Number : "))))