_author_ = 'Tarık Ünal'
# 27.03.18

import random

file = open('kelimelistesi.txt', "r")  # Dışardan kelime aldırmak için..
sozluk = file.read().split()
file.close()

sozlukboyutu = len(sozluk)
kelimeSec = sozluk[random.randint(0, sozlukboyutu)]  # Kelimenin seçimi için..

harfler = []
kalanhak = 7
altcizgi = "_"

gosterilecek = list(altcizgi * len(kelimeSec))

dongu = 1

while dongu:

    print(" ".join(gosterilecek), "\n")

    girilenHarf = input("Bir harf giriniz..:").lower()

    try:
        int(girilenHarf)
        print("Tek bir harf giriniz...\n")
    except:

        if len(girilenHarf) > 1:
            print("Harf giriniz!\n")
        else:

            if girilenHarf in harfler:
                print("Bu harfi zaten girdiniz...\n")
            else:

                KelDo = None

                for i in range(len(kelimeSec)):

                    if girilenHarf == kelimeSec[i]:

                        KelDo = True

                        gosterilecek[i] = girilenHarf

                        harfler.append(girilenHarf)

                        if altcizgi not in gosterilecek:
                            print(" ".join(gosterilecek))
                            print("\nTebrikler kelimeyi buldunuz...")

                            dongu = 0

                else:

                    if KelDo != True:
                        kalanhak -= 1

                        print("Yanlış harf. Kalan hakkınız: %s\n" % kalanhak)

                        harfler.append(girilenHarf)

                if kalanhak == 0:
                    print("Kaybettin! Doğru kelime =  %s  \n" % kelimeSec)
                    break
