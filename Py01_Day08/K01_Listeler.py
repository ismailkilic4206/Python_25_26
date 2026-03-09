#K01_Listeler.py

text = "Turkiye'nin en guzel sehri Istanbul'dur"
textList = text.split()
print(textList) #["Turkiye'nin", 'en', 'guzel', 'sehri', "Istanbul'dur"]

liste01 = [1, 3, 5, 7, 9]
print(liste01) #[1, 3, 5, 7, 9]

liste02 = [2, 0.5, "Elma", True]
print(liste02) #[2, 0.5, 'Elma', True]

meyveListesi01 = ["Elma", "Armut", "Kivi"]
meyveListesi02 = ["Seftali", "Nektarin", "Erik"]

print(meyveListesi01, meyveListesi02) #['Elma', 'Armut', 'Kivi'] ['Seftali', 'Nektarin', 'Erik']
print(meyveListesi01 + meyveListesi02)  #['Elma', 'Armut', 'Kivi', 'Seftali', 'Nektarin', 'Erik']

print(len(meyveListesi01))
print(len(meyveListesi01 + meyveListesi02))
print(   len(    (meyveListesi01 + meyveListesi02)[3]     )    )