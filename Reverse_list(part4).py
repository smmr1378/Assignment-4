user_list = [] # ایجاد یک لیست خالی
for i in range(4): # حلقه 4 بار
    number = input("Enter a number: ") # گرفتن ورودی کاربر
    user_list.append(int(number)) # تبدیل ورودی به عدد و اضافه کردن به لیست
user_list.reverse()
print(user_list)