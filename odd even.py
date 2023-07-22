"""By Mayendra Dwika Prayudha"""
#the program for odd or even

x=eval(input(" Type your number:"))
if x > 0:
    if x % 2 == 0:
        print("{} is positive even number ".format(x))
    else :
        print("{} is positive odd number".format(x))
elif x < 0:
    if x % 2 == 0:
        print("angka{} is negative even number". format(x))
    else :
         print("angka{} is negative odd number". format (x))
else :
    print(" is a Zero")       
