kg = int(input("Lütfen kilonuzu kilogram olarak girin: "))
boy = int(input("Lütfen boyunuzu santimetre olarak girin: "))

boy = boy / 100
vki = kg / boy**2

if vki < 18.5:
    print("Zayıf", vki)
elif 18.5 <= vki <= 24.5:
    print("Normal", vki)
else:
    print("Kilolu", vki)
