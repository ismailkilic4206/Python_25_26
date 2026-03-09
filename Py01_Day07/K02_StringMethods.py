#K02_StringMethods.py

info = "Benim adim Sami Basar 13 yasindayim ve Istanbulluyum.."

#1-) tamamini buyuk harfle yaziniz..
print(info.upper()) #BENIM ADIM SAMI BASAR 13 YASINDAYIM VE ISTANBULLUYUM..
print(info.isupper()) #False

#2-) tamamini kucuk harfle yapiniz..
print(info.lower()) #benim adim sami basar 13 yasindayim ve istanbulluyum..

#3-) her kelimenin ilk harfini buyuk yapiniz
print(info.title()) #Benim Adim Sami Basar 13 Yasindayim Ve Istanbulluyum..

#4-) Sadece ilk kelimenin ilk harfini buyuk yapar
print(info.capitalize()) #Benim adim sami basar 13 yasindayim ve istanbulluyum..

#5-) cumleyi bizim istedigimiz yerden ayirarak yeni bir liste dondurur
print(info.split()) #['Benim', 'adim', 'Sami', 'Basar', '13', 'yasindayim', 've', 'Istanbulluyum..']
#nereden ayirmak istedigimizi () icine tirnak isaretleri arasina belirtmek gereklidir.. tirnak isaretleri yoksa bosluklardan ayirir