"""Tarık Ünal"""
print("Adamasmaca Oyununa Hoşgeldiniz..")
import random
AdamAsmaca = ("""=====""","""====""","""===""","""==""","""=""")
maxCan = len(AdamAsmaca) - 1
#file = open('kelimelistesi.txt', "r")
#sozluk = file.read().split()
#file.close()
#sozlukboyutu = len(sozluk)
#gizliKelime = sozluk[random.randint(0, sozlukboyutu)]
kelimeler = ("hacettepe","telefon","manda","televizyon","mavi","porsuk","yarasa","balina","kobra","puma","karga","tavuk","tesla")
gizliKelime = random.choice(kelimeler)
#print(gizliKelime)
pano = "-" * len(gizliKelime)
hak = 0
havuz = []
while hak <= maxCan and pano !=gizliKelime:
    print(AdamAsmaca[hak])
    print("\nBu harfleri kullandın: ", havuz )
    print("Kelime: ", pano)
    print("Kalan can: ", 4-hak)
    tahmin = input("\nHarf giriniz: ").lower()
    while tahmin in havuz:
        print("\nBu harf zaten kullanıldı.")
        tahmin = input("Harf giriniz: ").lower()
    havuz.append(tahmin)
    if tahmin in gizliKelime:
        print("Güzel !!", tahmin, "harfi kelimede mevcut :)")
        yeni = ""
        for i in range(len(gizliKelime)):
            if tahmin == gizliKelime[i]:
                yeni += tahmin
            else:
                yeni += pano[i]
        pano = yeni
    else:
        print("Bulunamadın !!!")
        hak += 1
if hak > maxCan:
    print("\nKaybettin :(")
else:
    print("\nTebrikler!! Kazandın :)  :)")
print("Cevap: ", gizliKelime)
