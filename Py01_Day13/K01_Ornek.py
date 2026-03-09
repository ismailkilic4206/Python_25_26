#K01_Ornek.py

#Soru 3- Kullanicidan baslangic ve bitis degeri olarak pozitif sayilar alin, sinirlar
#dahil olarak aralarindaki tum sayilarin toplamini yazdirin. Bitis degeri
#baslangic degerinden kucukse, uyari yazdirip islemi sonlandirin

baslangic = int(input("Lutfen baslangic degerini giriniz.. "))
bitis = int(input("Lutfen bitis degerini giriniz.. "))

if bitis < baslangic:
    print("Bitis degeri baslangic degerinden kucuk olamaz.. ")

else:
    toplam = 0
    for i in range(baslangic, bitis + 1):
        toplam = toplam + i
    print(f"Baslancigi {baslangic}, bitisi {bitis} olan sayilar arasindaki sayilarin toplami: {toplam}")

#Bitis degeri baslangic degerinden kucuk ise, uyari yazdirip islemi sonlandirin