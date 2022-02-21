name = "Tonmai"
weigth = "65"
print("Hello " + name + "And weigth is " + weigth + "KG")
print("Hello %s And weigth is  %d KG" % (name, 65))

# %s ใช้กับพวก str %d ใช้กับint %f จะเป็นพวกทสนิยม

nameS= input("Input Name : ").capitalize()
LName = input("InPut last Name : ").capitalize()
print("Hello %s %s Wecome to The Web :)" % (nameS , LName))

text = "Tonmai"
textformat = "Wecome %s" % (nameS)
print(textformat.center(20 , "-"))
print(len(text))