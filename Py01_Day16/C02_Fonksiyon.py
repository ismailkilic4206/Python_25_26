#C02_Fonksiyon.py


k1 = int(input("Ucgenin 1. kenar uzunlugunu giriniz: "))
k2 = int(input("Ucgenin 2. kenar uzunlugunu giriniz: "))
k3 = int(input("Ucgenin 3. kenar uzunlugunu giriniz: "))

def ucgeninCevresi(kenar1, kenar2, kenar3):

    print(f"Kenar olculeri alinan ucgenin cevre uzunlugu: {kenar1 + kenar2 + kenar3} birimdir..")

ucgeninCevresi(k1, k2, k3)