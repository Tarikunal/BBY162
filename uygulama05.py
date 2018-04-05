__author__='Tarık Ünal'
#05.04.18
print("Adamasmaca Oyununa Hoşgeldiniz.\n")
import random
i = 0
Hak = 4
file = open('kelimelistesi.txt', "r")
sozluk = file.read().split()
file.close()
sozlukboyutu = len(sozluk)
gizliKelime = sozluk[random.randint(0, sozlukboyutu)]
#print(gizliKelime)
bosluk = []

for kelimeIslem in gizliKelime :
    bosluk.append("_")
print(bosluk)

while Hak > 0:
    i = 0
    tahmin= input("\nHarf giriniz: ").lower()
    if tahmin in gizliKelime:
        for bak in gizliKelime:
            if gizliKelime[i] == tahmin:
                bosluk[i] = tahmin
            i += 1
        print(bosluk)
    else:
        i = 0
        Hak -=1
        print("Kalan Can:" + str(Hak))
    if Hak == 0:
        print('Kaybettin. Doğru kelime "{}" idi.\n'.format(gizliKelime))
        break
