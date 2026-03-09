#K02_String.py

isim = "Nurullah"
soyisim = "Cingoz"
yas = "12"

tanitma = "Ben " + isim + ", Soyadim " + soyisim + ", Yasim " + yas
print(tanitma) #Ben Nurullah, Soyadim Cingoz, Yasim 12
print(len(tanitma)) #38   ilgili string ifadenin uzunlugunu (kac karakter oldugunu) hesaplar
print(isim[4]) #l

print(tanitma[4:12]) #Nurullah  (baslangic dahildir, bitis dahil degildir)
print(tanitma[6:20]) #rullah, Soyadi
print(tanitma[:12]) #Ben Nurullah  (: oncesinde bir deger yazilmazsa default deger olarak 0 atanir)
print(tanitma[14:]) #Soyadim Cingoz, Yasim 12 (: sonrasinda bir deger yazilmazsa default deger olarak en sona kadar gider)
print(tanitma[10::2]) #a,SydmCno,Ysm1        Default degerler: print(tanitma[0:len:1])
