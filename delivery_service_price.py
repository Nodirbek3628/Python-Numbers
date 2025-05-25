from num2words import num2words
a=float(input("boshlangish tulovni kiriting:($)"))
b=float(input("har bir (km) uchun tulovni kiriting:($)"))
c=float(input("yurgan masofani kiriting:(km) "))
yetkazib_berish=a+b*c
print(f"umumiy tulov:${yetkazib_berish:.2f}",num2words(yetkazib_berish,lang="en",to="currency"),num2words(yetkazib_berish,lang="ru",to="currency"))
