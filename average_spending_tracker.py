from num2words import num2words


a=float(input("birinchi qiymatni kiriting>>($),"))
b=float(input("ikkinchi qiymatni kiriting>>($),"))
c=float(input("uchunchi qiymatni kiriting>>($),"))
d=float(input("turtinchi  qiymatni kiriting>>($),"))
e=float(input("beshinchi qiymatni kiriting>>($),"))
j=float(input("oltinchi qiymatni kiriting>>($),"))
k=float(input("yettinchi qiymatni kiriting>>($),"))
ortachasi=(a+b+c+d+e+j+k)/7

print(ortachasi,num2words(ortachasi,lang="en",to="currency"),num2words(ortachasi,lang="ru",to="currency"))