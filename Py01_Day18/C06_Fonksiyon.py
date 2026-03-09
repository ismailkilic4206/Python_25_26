#C06_Fonksiyon.py


def fnk(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
fnk(11, 13, 29, 13, 7, 47, key1 = "Value1", key2 = "Value2")