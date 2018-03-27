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

    print(" ".join(gosterilecek),"\n") # Aralarında boşluk olacak şekilde kelimenin karakterlerini birleştiriyor.

    alinanharf = input("Bir harf giriniz..:").lower() # Büyük-küçük harf uyumluluğu için küçük harfe çevirdim.

    try: # try, input ile alınan verinin sayı olup olmadığını kontrol eder.
        int(alinanharf)
        print("Tek bir harf giriniz...\n")
    except: # Except alınan harf 1 den uzun olduğunda hata mesajı verir.

        if len(alinanharf) > 1:
            print("Harf giriniz!\n")
        else:

            if alinanharf in harfler:
                print("Bu harfi zaten girdiniz...\n")
            else:

                bulduk = None

                for i in range(len(kelimeSec)):
                    # kullanıcının girdiği harf, bulunucak kelimenin "i" nin taşıdığı sayı değerindeki indeksteki harfe eşit ise,
                    if alinanharf == kelimeSec[i]:

                        bulduk = True

                        gosterilecek[i] = alinanharf

                        harfler.append(alinanharf) # Alınan harf, harf havuzuna eklendi.

                        if altcizgi not in gosterilecek:

                            print(" ".join(gosterilecek)) # Aralarında boşluk olacak şekilde kelimenin karakterlerini birleştiriyor.
                            print("\nTebrikler kelimeyi buldunuz...")

                            dongu = 0
                            # Girilen harf aranan kelime içinde yoksa alttaki kodlar çalıştırılacak.
                else:

                    if bulduk != True:
                        kalanhak -= 1

                        print("Yanlış harf. Kalan hakkınız: %s\n" %kalanhak)

                        harfler.append(alinanharf) # Alınan harf, harf havuzuna eklendi

                if kalanhak == 0:
                    print("Kaybettin! Doğru kelime =  %s  \n" %kelimeSec)

                    break
