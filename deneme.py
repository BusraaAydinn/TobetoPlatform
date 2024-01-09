import random
import string

def rastgele_isim_uret(uzunluk):
    harfler = string.ascii_letters  # İsimleri oluşturmak için kullanılacak harfler
    return ''.join(random.choice(harfler) for i in range(uzunluk))

# Fonksiyonu kullanarak rastgele isim üretme (örneğin, 8 karakter uzunluğunda)
rastgele_isim = rastgele_isim_uret(8)
print("Üretilen rastgele isim:", rastgele_isim+"@gmail.com")




import random
import string

def rastgele_isim_uret(uzunluk):
    harfler = string.ascii_letters
    return ''.join(random.choice(harfler) for i in range(uzunluk))

def diger_fonksiyon():
    yeni_isim = rastgele_isim_uret(10)  # rastgele_isim_uret fonksiyonunu başka bir fonksiyon içinde çağırıyoruz
    print("Üretilen rastgele isim:", yeni_isim)

# Başka bir fonksiyonu çağırma
diger_fonksiyon()
