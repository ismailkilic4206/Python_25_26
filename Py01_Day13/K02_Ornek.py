#K02_Ornek.py

#Soru 4- Kullanicidan baslangic ve bitis degeri olarak pozitif sayilar alin, sinirlar
#dahil olarak aralarindaki tum sayilarin toplamini yazdirin. Bitis degeri
#baslangic degerinden kucuk olsa da program calissin

# No Pain No Gain

baslangic = int(input("Lutfen baslangic degerini giriniz.. "))
bitis = int(input("Lutfen bitis degerini giriniz.. "))

if bitis < baslangic:
    baslangic, bitis = bitis, baslangic


toplam = 0
for i in range(baslangic, bitis + 1):
    toplam = toplam + i
print(f"Baslancigi {baslangic}, bitisi {bitis} olan sayilar arasindaki sayilarin toplami: {toplam}")