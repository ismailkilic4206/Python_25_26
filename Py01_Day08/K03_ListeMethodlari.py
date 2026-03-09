#K03_ListeMethodlari.py

harf = ['a', 'h', 't', 'p', 'm', 'v', 'e', 'z', 'A']
sayi00 = ['7', '0', '93', '29', '37', '17', '1', '53', '105']
sayi01 = [7, 0, 93, 29, 37, 17, 1, 53, 105, 1]

sonVersiyon = max(harf)
sonVersiyon = min(harf)
sonVersiyon = max(sayi00)
sonVersiyon = max(sayi01)

sayi01.append(8) #liste sonuna ekleme yapar
sayi01.remove(1) #soldan saga dogru giderken karsilastigi ilk degeri siler
sayi01.pop(1) #ilgili indexi siler
sayi00.sort() #ASCII'ye gore siralama yapar
sayi01.reverse() #tersten siralama yapar
sayi01.clear() #tamamini siler


print(sayi01)
#print(sayi00)
#print(sonVersiyon)
