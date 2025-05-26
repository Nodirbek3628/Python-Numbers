from num2words import num2words

oy_boshi=float(input("Oy boshidagi istimolni kiriting:(kwt)"))
oy_oxiri=float(input("Oy oxiridgi istimolni kiriting:(kwt)"))
kwt=0.45 #1kwt narxi
istimol=oy_oxiri-oy_boshi
umumiy_tulov=kwt*istimol


print(f'umumiy tulov:${umumiy_tulov:.2f}',num2words(umumiy_tulov,lang="en",to="currency"),num2words(umumiy_tulov,lang="ru",to="currency"))