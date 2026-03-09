#K01_Donguler.py

marka = ["Nike", "Adidas", "Puma", "Skechers"]

#print(marka[0])
#print(marka[1])
#print(marka[2])
#print(marka[3])

for i in marka:
    print("merhaba")

isim = ['Nurullah', 'Adil Furkan', 'Selim', 'Sami']

for ism in isim:
    print(f"Benim adim: {ism}")

isim = "Adim Furkan"
for sm in isim:
    print(sm)

tuple01 = ("Futbol", "Basketbol", "Golf")
for t in tuple01:
    print(t)

liste03 = [(1,2), (2,3), (3,4), (4,5), (5,6)]

for a, b in liste03:
    print(a, b)

baskentler = {'Turkiye' : 'Ankara',
              'Danimarka' : 'Kopenhag',
              'Almanya' : 'Berlin',
              'Fransa' : 'Paris',
              'Senegal' : 'Dakar'}

for key, value in baskentler.items():
    print(f"{key}'nin baskenti {value}'dir")