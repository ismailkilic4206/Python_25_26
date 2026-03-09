#K04_StringOrnek.py

eDevlet = "https://www.turkiye.gov.tr"
text = "Turkiye'nin en guzel sehri Istanbul'dur"

#eDevlet icinden www karakterlerini yazdirin
print(eDevlet[8:11])

#eDevlet icinden turkiye karakterlerini yazdirin
print(eDevlet[12:19])

#text karakter dizisinde kac tane karaketer bulunur
print(len(text)) #39

#text icinde ilk 7 ve son 12 karakteri yazdirin      Turkiye-------Istanbul'dur
print(text[:7] , text[-12:])
print(text[:7] , text[len(text) - 12:])

#text degiskenindeki karakterleri tersten yazdirin
print(text[::-1]) #rud'lubnatsI irhes lezug ne nin'eyikruT