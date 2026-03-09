#K01_String.py

isim, soyad, yas, memleket = "Sami", "Basar", 13, "Istanbul"

#Yukaridaki verilen degiskenlerle asagidaki ifadeyi yazdiriniz..
# Benim adim Sami Basar 13 yasindayim ve Istanbulluyum..

print("Benim adim " + isim, soyad , str(yas) , "yasindayim ve " + memleket + "luyum..")
print(f"Benim adim {isim} {soyad} {yas} yasindayim ve {memleket}luyum..")



# sami basar yazisindaki s ve b harflerini buyuk harf ile degistiriniz..
adSoyad = "sami basar"
adSoyad = "S" + adSoyad[1:5] + "B" + adSoyad[6:]
print(adSoyad)