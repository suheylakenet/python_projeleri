def faktoriyel_hesapla(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel_hesapla(n - 1)

# Kullanıcıdan bir sayı al
girilen_sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))

# Faktöriyel hesapla
faktoriyel_sonuc = faktoriyel_hesapla(girilen_sayi)

# Sonucu ekrana yazdır
print(f"{girilen_sayi}! = {faktoriyel_sonuc}")
