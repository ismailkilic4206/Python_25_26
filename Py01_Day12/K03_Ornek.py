#K03_Ornek.py

#Soru 2- Kullanicidan pozitif bir tamsayi alin, 1’den girilen sayiya kadar(girilen sayi
#dahil) 7 ila bolunebilen sayilari yazdirin.

sayi = int(input("Lutfen bir pozitif tamsayi giriniz: "))

for i in range(1, sayi + 1):
    #Sayiyi 7ye boldugumuzde kalan sonuc 0 ise sayi 7ye bolunebilir, farkli ise bolunemez
    if i % 7 == 0:
        print(i, end=" ")