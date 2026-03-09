#K04_Ornek.py

#  Soru 8 (interview)- Kullanicidan pozitif bir sayi alin, 1’den baslayarak tum
#  tamsayilari yazdirin, sira
#  - 3 ile bolunebilen bir sayiya gelirse, sayi yerine Fizz
#  - 5 ile bolunebilen bir sayiya gelirse sayi yerine Buzz
#  - hem 3 hem 5 ile bolunebilen bir sayiya gelirse sayi yerine FizzBuzz
#  yazdirin

sayi = int(input("Lutfen pozitif bir tamsayi giriniz:"))

for i in range(1, sayi + 1):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)