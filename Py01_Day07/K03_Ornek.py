#K03_Ornek.py

eDevlet = "https://www.turkiye.gov.tr"
text = "Turkiye'nin en guzel sehri Istanbul'dur"

#1- ´ Hello World ´ karakter dizisinin basinda ve sonunda bulunan bosluklari siliniz
cumle = " Hello World "
#print(cumle.strip())

#2- eDevlet icindeki turkiye yazisi haricindeki karakterleri siliniz
#print(eDevlet[12:19])
#print(eDevlet.split(".")[1])

#3- text icindeki tum karakterleri kucuk harf yapiniz
#print(text.lower())

#4- eDevlet icinde kac tane t karakteri vardir
#print(eDevlet.count("t"))

#5- eDevlet, www ile baslayip tr ile bitiyor mu
#print(eDevlet.startswith("www")) #False
#print(eDevlet.endswith("tr")) #True

#6 eDevlet icinde .com karakterleri var mi
#print(eDevlet.find(".com"))

#7- text icindeki karakterlerin hepsi alfabetik mi
#print(text.isalpha()) #False

#8- turkiye ifadesini satirda 50 karakter icine yerlestirip sagina ve soluna * ekleyin
print((eDevlet.split(".")[1]).center(50,"*"))
#print((eDevlet.split(".")[1]).rjust(50, "*"))
#print((eDevlet.split(".")[1]).ljust(50, "*"))
#
##9 text Stringinde bulunan bosluk karakterlerini - ile degistiriniz
#print(text.replace(" ", "-"))

#10- text icinde bulunan guzel kelimesini kalabalik olarak degistirin
print(text.replace("guzel", "kalabalik"))
