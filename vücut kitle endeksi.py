kg=int(input("lütfen kilonuzu girin:"))
boy=int(input("lütfen boyunuzu girin:"))
boy=boy/100
vki=kg/boy**2
if vki<18.5:
    print("zayıf",vki)
elif vki >=18.5 and vki<=24.5:
    print("normal",vki)
else :
    print("kilolusunuz",vki)