#K02_DegiskenTanimlamaOrnek.py

# Verilen 3 siparisin toplamini degiskenler olusturarak
# hesaplayip yazdiriniz

#   Siparis 1 = 510tl + Vergi
#   Siparis 2 = 2070.82tl + Vergi
#   Siparis 3 = 730tl + Vergi

#   Vergi oranlari %8 hesaplanacaktir

siparis01 = 510
siparis02 = 2070.82
siparis03 = 730

vergi = 0.08

#vergiDahilSiparis01 = 510 * 0.08 + 510
#vergiDahilSiparis02 = 2070.82 * 0.08 + 2070.82
#vergiDahilSiparis03 = 730 * 0.08 + 730

vergiDahilSiparis01 = siparis01 * vergi + siparis01
vergiDahilSiparis02 = siparis02 * vergi + siparis02
vergiDahilSiparis03 = siparis03 * vergi + siparis03

toplam = vergiDahilSiparis03 + vergiDahilSiparis02 + vergiDahilSiparis01

print("Fiyatlari verilen 3 siparisin vergi dahil toplam fiyati:" , toplam)