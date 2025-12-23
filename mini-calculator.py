#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

print("✨ Gelişmiş Mini Hesap Makinesi ✨")
print("""
Yapabileceğin işlemler:
1) Toplama (+)
2) Çıkarma (-)
3) Çarpma (*)
4) Bölme (/)
5) Üs alma (**)
6) Mod alma (%)
7) Karekök (sqrt)
8) Mutlak değer (abs)
9) Sayıyı kare yapma (square)
10) Sayıyı küp yapma (cube)
""")

while True:
    op = input("İşlem seç ( + , - , * , / , ** , % , sqrt , abs , square , cube ): ")

    if op in ["sqrt", "abs", "square", "cube"]:
        x = float(input("Sayıyı gir: "))
        
        if op == "sqrt":
            print("Sonuç:", math.sqrt(x))
        elif op == "abs":
            print("Sonuç:", abs(x))
        elif op == "square":
            print("Sonuç:", x ** 2)
        elif op == "cube":
            print("Sonuç:", x ** 3)
    else:
        x = float(input("Birinci sayıyı gir: "))
        y = float(input("İkinci sayıyı gir: "))

        if op == "+":
            print("Sonuç:", x + y)
        elif op == "-":
            print("Sonuç:", x - y)
        elif op == "*":
            print("Sonuç:", x * y)
        elif op == "/":
            if y == 0:
                print("0'a bölüm olmaz!")
            else:
                print("Sonuç:", x / y)
        elif op == "**":
            print("Sonuç:", x ** y)
        elif op == "%":
            print("Sonuç:", x % y)
        else:
            print("Geçerli bir işlem değil!")
    
    again = input("Devam etmek ister misin? (e/h): ")
    if again.lower() != "e":
        print("Program sonlandırıldı.")
        break

