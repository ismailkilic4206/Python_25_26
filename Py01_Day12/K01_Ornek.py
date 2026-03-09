#K01_Ornek.py
from Py01_Day05.K02_DegiskenTanimlamaOrnek import toplam

sayilar = [1, 5, 7, 14, 21, 76, 81, 56, 102, 103]

#  sayilar listesindeki 3'un kati olanlari yazdirin..
#for i in sayilar:
#    if i % 3 == 0:
#        print(i)

#  sayilar listesindeki sayilarin toplamini yazdirin..
#toplam = 0
#for i in sayilar:
#    toplam = toplam + i
#print(toplam)

#  sayilar listesindeki tek sayilari toplayin..
#toplam = 0
#for i in sayilar:
#    if i % 2 == 1:
#        toplam = toplam + i
#print(toplam)

#  sayilar listesindeki cift sayilarin karelerini aliniz..
#for i in sayilar:
#    if i % 2 == 0:
#        print(i ** 2)

nufus = [{'ulke':'Turkiye', 'nfs':  '85.664.000'},
{'ulke':'Danimarka', 'nfs': '6.002.000'},
 {'ulke':'Almanya', 'nfs': '84.075.000'},
  {'ulke': 'Fransa', 'nfs': '66.650.000'},
   {'ulke':'Senegal', 'nfs': '18.931.000'}]
#  ulkelerin nufuslarinin toplami nedir
toplam = 0
for i in nufus:
    kisi = int(i['nfs'].replace('.', ''))
    toplam = toplam + kisi
print(toplam)





#  20.000.000 uzerinde nufusu olan ulkeleri yazdiriniz