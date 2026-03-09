#C01_Fonksiyon.py

def marketAlisverisi(urun1, urun1Sayi, urun2, urun2Sayi, urun3, urun3Sayi):
    print(f"Alinan 3 cikolata, 2'ser ekmek ve tereyaginin maliyeti {(urun1 * urun1Sayi) + (urun2 * urun2Sayi) + (urun3 * urun3Sayi)}TL'dir")

cikolata = 10
ekmek = 15
tereyagi = 250

marketAlisverisi(cikolata, 3, ekmek, 2, tereyagi, 2)