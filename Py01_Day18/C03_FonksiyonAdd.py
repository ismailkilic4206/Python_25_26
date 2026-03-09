#C03_FonksiyonAdd.py
#list = ["Adil", "Sami", "Nurullah", "Selim"]
#
#def ekleme(a, b, c = 0):
#    return sum((a, b, c))
#print(ekleme(9, 17, 8))


def toplama(*params):
    print(params)
    print(params[2])
    return sum((params))
print(toplama(5, 8, 10, 4))