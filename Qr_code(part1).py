import qrcode 
name =input("Enter your name: ")
number = input("Enter your Number: ")
x = qrcode.make(name + " " + number)
x.save("my_Qrcode.png")