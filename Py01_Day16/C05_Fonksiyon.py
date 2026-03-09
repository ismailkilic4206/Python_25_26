#C05_Fonksiyon.py

# Belirtilen bir ismi belirtilen sayi kadar yazdiran bir fonksiyon yaziniz...
def yazdirma(isim, sayi):
    print(isim * sayi)

yazdirma("Adil\n", 3)

# Verilen iki sayi arasindaki asal sayilari bulan bir fonksiyon yaziniz...

def asalSayilariBulma(sayi1, sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

sayi1 = int(input("1. Sayiyi giriniz:"))
sayi2 = int(input("2. Sayiyi giriniz:"))


asalSayilariBulma(sayi1, sayi2)