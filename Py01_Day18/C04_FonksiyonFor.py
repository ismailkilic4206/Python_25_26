#C04_FonksiyonFor.py

def toplama(*params):
    print(type(params))
    toplam = 0

    for i in params:
        toplam = toplam + i

    return toplam
print(toplama(5, 8, 10, 4))