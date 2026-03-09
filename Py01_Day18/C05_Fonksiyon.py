#C05_Fonksiyon.py
def kullaniciBilgi(**args):
    print(type(args))
    for key, value in args.items():
        print("{} is {}".format(key, value))

kullaniciBilgi(name = "Adil", age = 11, city = "Ankara")
kullaniciBilgi(name = "Nurullah", age = 12, city = "Istanbul", phoneNo = "5445445454")
kullaniciBilgi(name = "Sami", age = 13, city = "Bursa", phoneNo = "5554443322")