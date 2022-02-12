price = input("Price THB :")
vat = 7
result = float(price) + (float(price) * vat / 100)
print(result)
# หรือแบบนี้แทน
price = float(input("Price THB :"))
vat = 7
result = (price) + (price * vat / 100)
print(result)
