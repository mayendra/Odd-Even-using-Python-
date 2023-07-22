#program menentukan apakah suatu bilangan tersebut bernilai ganjil atau genap

x=eval(input(" masukan angka :"))
if x > 0:
    if x % 2 == 0:
        print("angka {} adalah bilangan genap".format(x))
    else :
        print("angka{} adalah bilangan ganjil".format(x))
elif x < 0:
    if x % 2 == 0:
        print("angka{} adalah bilangan negatif genap". format(x))
    else :
         print("angka{} adalah bilangan negatif ganjil". format (x))
else :
    print(" angka nol")       