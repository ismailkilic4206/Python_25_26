#K02_Ornek.py

#1- 4 tane markanin elemanlarina sahip bir liste olusturunuz
marka = ["Nike", "Adidas", "Puma", "Skechers"]

#2- listenin eleman sayisini bulunuz
sonHali = len(marka) #4

#3- listenin ilk ve son elemanini bulunuz
sonHali = marka[0] #Nike
sonHali = marka[-1] #Skechers
sonHali = marka[len(marka) - 1] #Skechers

#4- Nike degerini Puma degeri ile degistirin
marka[marka.index('Nike')] = "Puma"
sonHali = marka

#5- Adidas listenin kacinci elemanidir
sonHali = marka.index("Adidas") + 1

#6- listenin -2 indexindeki degeri
sonHali = marka[-2]

#7- listenin ilk uc elemani nedir
sonHali = marka[:3]

#8- listedeki son iki eleman yerine Kinetix ve NewBalance ekleyin
marka[-2:] = ["Kinetix", "NewBalance"]
sonHali = marka

#9- listeye 'Dockers' ve 'Kemal Tanca' ekleyiniz
marka = marka + ["Dockers" , "Kemal Tanca"]
sonHali = marka

#10- listenin sondan ikinci elemanini silin
del marka[-2]


print(sonHali)