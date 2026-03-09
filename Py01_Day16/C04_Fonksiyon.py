#C04_Fonksiyon.py
isim = "Atakan"
yeniIsim = input("Lutfen isim giriniz..")

def isimDegistirme (isim):
    print(isim)

isimDegistirme(isim)
isimDegistirme(f"Eski ismim {isim} olmasina ragmen yeni ismim {yeniIsim}")