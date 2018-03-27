_author_='Tarık Ünal'
#27.03.18

import random

file = open('kelimelistesi.txt', "r") #Dışardan kelime aldırmak için..
sozluk = file.read().split()
file.close()

sozlukboyutu = len(sozluk)
kelimeSec = sozluk[random.randint(0, sozlukboyutu)] #Kelimenin seçimi için..

harfler = []
kalanhak = 7
altcizgi = "_"

gosterilecek = list(altcizgi * len(kelimeSec))

dongu = 1


while dongu:

    print(" ".join(gosterilecek),"\n").

    alinanharf = input("Bir harf giriniz..:").lower() 

    try:
        int(alinanharf)
        print("Tek bir harf giriniz...\n")
    except:

        if len(alinanharf) > 1:
            print("Harf giriniz!\n")
        else:

            if alinanharf in harfler:
                print("Bu harfi zaten girdiniz...\n")
            else:

                bulduk = None

                for i in range(len(kelimeSec)):
                 
                    if alinanharf == kelimeSec[i]:

                        bulduk = True

                        gosterilecek[i] = alinanharf

                        harfler.append(alinanharf) 

                        if altcizgi not in gosterilecek:

                            print(" ".join(gosterilecek)) 
                            print("\nTebrikler kelimeyi buldunuz...")

                            dongu = 0
                            
                else:

                    if bulduk != True:
                        kalanhak -= 1

                        print("Yanlış harf. Kalan hakkınız: %s\n" %kalanhak)

                        harfler.append(alinanharf)

                if kalanhak == 0:
                    print("Kaybettin! Doğru kelime =  %s  \n" %kelimeSec)
                    break
