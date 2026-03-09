#K01_Tuple.py

sayi = [7, 0, 93, 29, 37, 17, 1, 53, 105, 1]

tuple = (1, 2, 'uc', 4)

#print(type(sayi)) #<class 'list'>
#print(type(tuple)) #<class 'tuple'>

liste = ["Armut", "Seftali", "Kiraz"]
tuple01 = ("Futbol", "Basketbol", "Golf")
tuple02 = ("BMW", "Mercedes0", "Ferrari")

liste[0] = "Muz"
#tuple02[0] = "Porche" #TypeError: 'tuple' object does not support item assignment

del  liste[0]
#del  tuple02[0] #TypeError: 'tuple' object doesn't support item deletion

tuple03 = tuple01 + tuple02
print(tuple03) #('Futbol', 'Basketbol', 'Golf', 'BMW', 'Mercedes0', 'Ferrari')