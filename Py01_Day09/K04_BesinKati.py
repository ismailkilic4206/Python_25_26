#K04_BesinKati.py

#Soru 1- Kullanicidan bir sayi isteyin, sayiyi kontrol edip 5 ile bolunebiliyorsa
#“Sayi 5’in tam kati” yazdirin.

sayi = int(input("Lutfen bir sayi giriniz.."))

if (sayi % 5 == 0) :
    print(f"{sayi}, 5'in katidir..")