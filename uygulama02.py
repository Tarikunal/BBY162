_author_='Tarık Ünal'
#Saniye cinsinden verilen veriyi yıl, ay, gün, saat, dakika ve saniyeye dönüştüren formül..
#Uygulama02
girdi = int(input("Saniye cinsinden bir değer giriniz...:"))
yil = girdi / 31557600
ay = (girdi % 31557600) / 2629800
gun = ((girdi % 31557600) % 2629800) / 86400
saat = (((girdi% 31557600) % 2629800) % 86400) / 3600
dakika = ((((girdi % 31557600) % 2629800) % 86400)% 3600) / 60
saniye = (((((girdi % 31557600) % 2629800) % 86400) % 3600) % 60)

print(int(yil) , "Yıl" , " " , int(ay) ,"Ay" , " " , int(gun) ,"Gün" , " " , int(saat) , "Saat" , " " , int(dakika)  ,"Dakika", " " , int(saniye) , "Saniye")
