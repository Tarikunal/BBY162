#06.03.2018
_auther_='Tarık Ünal'
#Basit Sözlük Örneği

onemli_numaralar = {"Ambulans":112,"Polis":155,"İtfaiye":110,"Jandarma":156,"Bilinmeyen Numaralar":118,"TTNET":145,"Data Arıza":124,"Gaz Arıza":187,"Elektrik Arıza":186,"Su Arıza":185}
secenekler = """
[1] Önemli Numaraların İsimlerini Listele
[2] Önemli Numaraları Listele
[Q] Çıkış
"""

while True:
    print(secenekler)
    islem = input("İşlenminiz..:")

    if islem == "1" :
      print(onemli_numaralar.keys())

    elif islem == "2" :
        print(onemli_numaralar.values())

    elif islem == "Q" or islem == "q":
        break
    else:
        print("Hatalı Giriş Yapıldı...")