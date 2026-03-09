#K03_StringFormatlama.py

isim = "Sami"
soyad = "Basar"
yas = 13

tanitma = "Adim: " + isim + " Soyadim: " + soyad
print(tanitma) #Adim: Sami Soyadim: Basar

print("Adim: {}".format(isim)) #Adim: Sami
print("Adim Soyadim: {i} {s}".format(s = soyad, i = isim)) #Adim Soyadim: Sami Basar

print(f"Adim Soyadim: {isim} {soyad}.. Yasim {yas}") #Adim Soyadim: Sami Basar.. Yasim 13
