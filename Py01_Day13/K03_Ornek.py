#K03_Ornek.py

#Soru 7- Kullanicidan pozitif bir tamsayi alip, rakamlar toplamini yazdirin.

sayi = int(input("Lutfen pozitif bir tamsayi giriniz"))

toplam = 0
while sayi > 0:
   toplam = toplam + (sayi % 10)
   sayi = sayi // 10
print(f"Kullanicidan alinan sayinin rakamlar toplami: {toplam}")