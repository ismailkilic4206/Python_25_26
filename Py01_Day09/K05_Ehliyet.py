#K05_Ehliyet.py

#Soru 3- Kullanicidan yasini isteyin, 18 yas ve uzeri ise ”Ehliyet alabilirsin”
#yazdirin, yoksa Ehliyet almasi icin gecmesi gereken yil sayisini yazdirin.

yas = int(input("Lutfen Yasinizi Giriniz: "))

if (yas >= 18) :
    print("Ehliyet alabilirsin")
else:
    print(f"Ehliyet almaniz icin {18 - yas} yil vardir..")