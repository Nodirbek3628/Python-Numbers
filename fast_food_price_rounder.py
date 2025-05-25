from num2words import num2words

a=float(input("birinchi maxsulot narxini  kiriting>>($)"))
b=float(input("ikkinch maxsulot narxini  kiriting>>($)"))
c=float(input("uchunchi maxsulot narxini  kiriting>>($)"))

umumiy_narxi=(a+b+c)
a=f"${umumiy_narxi:.2f}"
round=( umumiy_narxi,0.1)


print(umumiy_narxi,(num2words(umumiy_narxi,lang="en",to="currency"),num2words(umumiy_narxi,lang="ru",to="currency")))