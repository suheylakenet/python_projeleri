import random
import string

rakamlar = string.digits #rakamları verir
semboller= string.punctuation #rastgele sembol verir
kücük_harfler=string.ascii_lowercase #küçük harfleri verir
büyük_harfler= string.ascii_uppercase #büyük harfleri verir
tüm_karakterler= [rakamlar , semboller, kücük_harfler , büyük_harfler]

sifre =""

for j in range(4):
    for i in range(2):
        sifre += tüm_karakterler[j][random.randint(0, 9)]


print(sifre)
sifre = list(sifre)
random.shuffle(sifre)
print(sifre)

yeni_sifre= ""
yeni_sifre= yeni_sifre.join(sifre)

print(yeni_sifre)

