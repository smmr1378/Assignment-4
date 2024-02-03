user_list = [] # ایجاد یک لیست خالی
new_list = []
for i in range(7): # حلقه 7 بار
    number = input("Enter a number: ") # گرفتن ورودی کاربر
    user_list.append(int(number)) # تبدیل ورودی به عدد و اضافه کردن به لیست
for item in user_list:
    if item not in new_list:
        new_list.append(item)
        print(new_list)