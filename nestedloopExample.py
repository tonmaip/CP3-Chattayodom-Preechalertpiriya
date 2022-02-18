for x in range(12):
    x = x + 1
    for y in range(12):
        print(x ," x ", y + 1 ,"=", x * (y + 1))

# หรือแบบนี้ก็ได้
for x in range(12):
    for y in range(12):
        print(x+1 ," x ", y + 1 ,"=", (x+1) * (y + 1))


