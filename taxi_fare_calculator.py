from num2words import num2words

boshlangich_tulov=float (input("boshlangich tulovni kiriting: ($)"))
km_uchun=float(input("Har bir km uchun tulovni kiriting:($)"))
masofani_km=float(input("Yurgan masofani kiriting:(km)"))

umumiy_tulov=boshlangich_tulov+km_uchun*masofani_km

print(umumiy_tulov,num2words(umumiy_tulov,lang="en"),",",num2words(umumiy_tulov,lang="ru"))


