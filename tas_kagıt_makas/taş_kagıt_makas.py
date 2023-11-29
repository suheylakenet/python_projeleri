import random
def pc_secimi_uret():
    n= random.randint(1,3)
    if n == 1:
        return "tas"
    elif n == 2:
        return "kagit"
    else :
        return "makas"
    
skor_kullanici = 0
skor_pc=0


while True :
    kullanici_secimi = input("Taş? Kagit? Makas? ")
    pc_secimi = pc_secimi_uret()
    print ("bilgisayar:", pc_secimi )

    if pc_secimi == kullanici_secimi:
        print("berabere")
    elif pc_secimi == "tas" and  kullanici_secimi =="kagit":
            skor_kullanici+=1

    elif pc_secimi == "kagit" and  kullanici_secimi =="makas":
            skor_kullanici+=1
    elif pc_secimi == "makas" and  kullanici_secimi =="tas":
            skor_kullanici+=1
    else:
        skor_pc += 1
    print("SİZ:",skor_kullanici,"VS PC:",skor_pc)

    if skor_kullanici ==3 or skor_pc== 3 :
         break
if skor_pc > skor_kullanici :
     print("MAALESEF KAYBETTİNİZ :(")
else:
     print("KAZANDINIZ :)")