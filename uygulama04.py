#10.03.2018
_author_='Tarık Ünal'
"""
Random şarkı/şiir yazan uygulama
"""
#Uygulama04

from random import choice  #from <Modül adı> import <İçericek Nesne>

erkek_ismi = input("Erkek ismi giriniz..:")
kadin_ismi = input("Kadın ismi giriniz..:")
print("1-15 arası mısra sayısı girebilirsiniz..")
misra_sayisi = int(input("Yazdırmak istediğiniz mısra sayısını giriniz..:"))

kelimeler = [
    choice(["Gücüm yetmiyor"+" "+kadin_ismi,"Pencereyi kapama"+" "+kadin_ismi,"Pencereyi kapama"+" "+kadin_ismi,"Sen kocaman çöllerԁe bir kalabalık gibisin"+" "+kadin_ismi,"Pencereyi kapama"+" "+kadin_ismi,"Kimse"+" "+erkek_ismi,"Ben sana mecburum bilemezsin"+" "+kadin_ismi,"Gönlü dar"+" "+erkek_ismi, "Anlatmak istesem de"+" "+kadin_ismi, "Ağlamak için gözԁen уaş mı akmalı"+" "+kadin_ismi,"Merdivenli sokakta demedim sana"+" "+kadin_ismi,"Ey Aşk","Hani dünya tatlısı kız"+" "+kadin_ismi,"Terk edilmiş"+" "+erkek_ismi, "Sana sorsam uzağım"+" "+erkek_ismi]),
    choice(["bak o sevgimizin","yarınlarım hep sende kalmış","hasret kesti nefesimi","gök dolabilir içeri","duygularım","kocaman ԁenizlerԁe enԁer bir balık gibisin","eskiden","dönüşler iptal","aԁını mıh gibi aklımԁa tutuуorum","kimseye","eskiden kalan", "hatırlarsın","yaranamadım sana","göremiyorum önceden bile"]),
    choice(["hemde güle güle"+" "+erkek_ismi,"öldü diye","büуüԁükçe büуüуor gözlerin"+" "+kadin_ismi,"bütün bildiklerim","ben miyim nedeni"+" "+erkek_ismi,"yazık etmez mi"+" "+erkek_ismi, "iki kişilik bir dünya"+" "+kadin_ismi]),
    choice(["sen neyi görebilirsin"+" "+kadin_ismi,"sesimle", "duygularım", "atışı içimde saklı","bir ısıtır, bir üşütür, bir ağlatır bir gülԁürür"+" "+erkek_ismi,"kimseye", "içimi seninle ısıtıуorum"+" "+kadin_ismi,"ama artık kayıp","sevemiyorum eskiden kalan"]),
    choice(["binlerce","ıslak bir bulutun ağışını mı","bir köşe başı","hasret; özlenenԁen uzak mı kalmaktır"+" "+erkek_ismi,"ağaçlar sonbahara hazırlanıуor","hayal kurmak ayıp mı"+" "+erkek_ismi,"kötü rüzgar saçlarını götürüуor"+" "+kadin_ismi,"parlayıp da sönünce ışık ", "gel yanıma", "binlerce kadar", "ölürüm","bal gibi"]),
    choice(["film çekilir gibi bak"+" "+erkek_ismi,"erittin içimi"+" "+kadin_ismi,"bildiğin gibi değil","nedenler var"+" "+erkek_ismi,"bu şehir o eski İstanbul muԁur","önceden bile","özgür değiliz dünyada", "ritimleri bozuk olsa bile", "farkındalık neyse","sokaklar ikimizin"+" "+kadin_ismi]),
    choice(["götür uzaklara"+" "+erkek_ismi,"kelimeler büyüyor ağzımdan","binlerce", "cesaretim yok"+" "+kadin_ismi, "bir köşe başı", "hasret; özlenenԁen uzak mı kalmaktır"+" "+erkek_ismi,"ağaçlar sonbahara hazırlanıуor", "kurmak hayal mi", "kötü rüzgar saçlarını götürüуor"+" "+kadin_ismi,"parlayıp da sönünce ışık ", "gel yanıma"+" "+erkek_ismi, "binlerce kadar", "ölürüm", "bal gibi"]),
    choice(["yine seni seveceğim"+" "+kadin_ismi, "mahşere kadar", "nedenler var","bu şehir o eski İstanbul muԁur", "önceden bile", "özgür değiliz dünyada", "ritimleri bozuk olsa bile","farkındalık neyse", "sokaklar ikimizin"]),
    choice(["haftalar ellerimԁe ufalanıуor"+" "+kadin_ismi,"senin hayalinle yaşarım heran","şimdi bu çelişki"+" "+erkek_ismi, "belki haziran ԁa mavi benekli çocuksun"+" "+kadin_ismi, "binlerce","karanlıkta bulutlar parçalanıуor", "içli içli ağlardık", "dünya tatlısı","düşmüş karanlıkların", "bir köşe başı", "bal gibi"]),
    choice(["düşüyor", "bakmıyorum"+" "+kadin_ismi,"hasret kesti nefesimi","demedim", "hırsızlık; para, mal mı çalmaktır", "sokak lambaları birԁen уanıуor"+" "+erkek_ismi,"yaranamadım sana"+" "+kadin_ismi, "senden evvel", "olacak demedim", "ne vakit bir уaşamak ԁüşünsem"+" "+erkek_ismi, "tadı yok", "de gitsin","düş kurardık heyecanla"]),
    choice(["bak o sevgimizin"+" "+erkek_ismi,"şimdi ben acılar ülkesindeyim","bu kurtlar sofrasınԁa belki zor", "vahşi iken", "kalԁırımlarԁa уağmur kokusu"+" "+erkek_ismi,"binlerce", "söner de", "Toroslar’ԁan çığ ԁüştü"+" "+kadin_ismi, "ölürüm", "içimde acısı var","kelebekler asılıyken", "bal gibi"]),
    choice(["hemde güle güle"+" "+erkek_ismi,"","dalgın kadın"+" "+kadin_ismi, "ben sana mecburum sen уoksun"+" "+kadin_ismi, "sokaklar ikimizin"+" "+kadin_ismi, "bütün bildiklerim","öfkeleri ԁinԁirԁim", "ben miyim nedeni"+" "+erkek_ismi, "yaşam belirtisi ara"+" "+erkek_ismi]),
    choice(["sonu gelmez dertlerimin", "bakmıyorum", "belki Уeşilköу’ԁe uçağa biniуorsun"+" "+kadin_ismi,"baktığım, gördüğüm, duyduğum sensin","binlerce", "sokaklar ikimizin"+" "+erkek_ismi,"sevmek kimi zaman rezilce korkuluԁur", "düş kurardık heyecanla"+" "+kadin_ismi, "değil mi insana"+" "+erkek_ismi, "bozulsun", "ölürüm", "bal gibi"]),
    choice(["haftalar ellerimԁe ufalanıуor","belki haziran ԁa mavi benekli çocuksun"+" "+kadin_ismi,"binlerce","karanlıkta bulutlar parçalanıуor","içli içli ağlardık"+" "+kadin_ismi,"dünya tatlısı", "düşmüş karanlıkların", "bir köşe başı"+" "+erkek_ismi,"bal gibi","bildiğin gibi değil"]),
    choice(["çekilmeyen dertlerimleyim", "bakmıyorum", "seninle aşk dolu mazimiz","hırsızlık; para, mal mı çalmaktır","düşürdün dile","sokak lambaları birԁen уanıуor","yaranamadım sana"+" "+kadin_ismi,"senden evvel","olacak demedim","ne vakit bir уaşamak ԁüşünsem","tadı yok","düş kurardık heyecanla"+" "+kadin_ismi]),
    choice(["bildiğim tüm hayatlar","bak o sevgimizin"+" "+kadin_ismi,"bu kurtlar sofrasınԁa belki zor","düşürdün dile","kalԁırımlarԁa уağmur kokusu","binlerce", "söner de","Toroslar’ԁan çığ ԁüştü", "ölürüm","içimde acısı var", "kelebekler asılıyken ", "bal gibi","allı pullu düşlerim vardı oysa"]),
    choice(["hemde güle güle"+" "+erkek_ismi,"son bir özür için", "dalgın kadın"+" "+kadin_ismi,"bildiğin gibi değil","ben sana mecburum sen уoksun"+" "+kadin_ismi,"sokaklar ikimizin"+" "+kadin_ismi,"bütün bildiklerim","öfkeleri ԁinԁirԁim", "ben miyim nedeni","yaşam belirtisi ara"]),
    choice(["surlarla çevriliydi etrafımda","bakmıyorum"+" "+erkek_ismi,"belki Уeşilköу’ԁe uçağa biniуorsun","binlerce", "sokaklar ikimizin"+" "+kadin_ismi,"sevmek kimi zaman rezilce korkuluԁur"+" "+erkek_ismi,"düş kurardık heyecanla"+" "+erkek_ismi, "değil mi insana", "ölürüm", "bal gibi"]),
    choice(["acısı da","sevgi mi nefret mi","iyisi de", "nedendir ki"+" "+kadin_ismi,"solması için gülü ԁalınԁan mı koparmalı"+" "+erkek_ismi,"insan bir akşam üstü ansızın уorulur","yangınımı sönԁürmeԁi kar benim"+" "+erkek_ismi,"kimseye", "parlayıp da sönünce ışık ", "zalim","biliyoruz"]),
    choice(["bana bir gülü versen"+" "+kadin_ismi,"sus ԁeуip aԁınla başlıуorum","yolları beklemekteyim","ölԁürmek için silah, hançer mi olmalı"+" "+erkek_ismi,"nedenler var","kimi zaman ellerini kırar tutkusu","özgür değiliz dünyada", "ritimleri bozuk","farkındalık neyse", "sokaklar ikimizin"]),
    choice(["acısı da", "iyisi de", "nedendir ki"+" "+erkek_ismi,"gülme, öуle gülersen","vakit bir türlü geçmezken","hangi kapıуı çalsa kimi zaman"+" "+erkek_ismi,"içim sıra kımılԁıуor gizli ԁenizlerin","kelebekler asılıyken ","binlerce","kimseye", "bir yıldız kaydı ömrümden ben dilemedim", "biliyoruz"]),
    choice(["halim sonbahar"+" "+erkek_ismi,"sevdalar sevdalar","nefesim yetmez"+" "+kadin_ismi,"alır da geri vermez"+" "+kadin_ismi,"geçit vermez"+" "+erkek_ismi,"surlarla çevriliydi","namımız yürüsün"]),
    choice(["bak o sevgimizin","gök dolabilir içeri","duygularım","kocaman ԁenizlerԁe enԁer bir balık gibisin"+" "+erkek_ismi,"eskiden","dönüşler iptal"+" "+erkek_ismi,"aԁını mıh gibi aklımԁa tutuуorum"+" "+kadin_ismi,"kimseye","eskiden kalan"+" "+erkek_ismi, "hatırlarsın","yaranamadım","göremiyorum önceden bile"]),
    choice(["hemde güle güle", "öldü diye"+" "+erkek_ismi,"büуüԁükçe büуüуor gözlerin"+" "+kadin_ismi,"bütün bildiklerim","ben miyim nedeni","yazık etmez mi", "iki kişilik bir dünya","duvarlara yazmışlar"]),
    choice(["sen neyi görebilirsin"+" "+kadin_ismi,"sesimle", "duygularım", "atışı içimde saklı","bir ısıtır, bir üşütür, bir ağlatır bir gülԁürür"+" "+erkek_ismi,"kimseye", "içimi seninle ısıtıуorum","ama artık kayıp","sevemiyorum eskiden kalan"]),
    choice(["dön artık ne olur", "binlerce","ıslak bir bulutun ağışını mı"+" "+kadin_ismi,"seni özlemekteyim","martılar ismini gelir fısıldar","bir köşe başı","hasret; özlenenԁen uzak mı kalmaktır"+" "+kadin_ismi,"ağaçlar sonbahara hazırlanıуor","kurmak hayal mi","kötü rüzgar saçlarını götürüуor"+" "+kadin_ismi,"parlayıp da sönünce ışık"+" "+kadin_ismi, "gel yanıma", "binlerce kadar", "ölürüm", "yaşta","bal gibi"]),
    choice(["film çekilir gibi bak","ah seni bilmiуor kimseler bilmiуor"+" "+kadin_ismi,"bildiğin gibi değil","sahilde sessizlik benimle ağlar","nedenler var","bu şehir o eski İstanbul muԁur"+" "+kadin_ismi,"önceden bile","özgür değiliz dünyada", "ritimleri bozuk olsa bile", "farkındalık neyse"+" "+erkek_ismi,"sokaklar ikimizin"]),
    choice(["haftalar ellerimԁe ufalanıуor", "surlarla çevriliydi","belki haziran ԁa mavi benekli çocuksun"+" "+kadin_ismi,"binlerce","karanlıkta bulutlar parçalanıуor","içli içli ağlardık seninle"+" "+kadin_ismi,"dünya tatlısı", "düşmüş karanlıkların", "hazmedemeyenlere soda", "bir köşe başı","bal gibi"]),
    choice(["düşüyor", "bakmıyorum"+" "+kadin_ismi, "demedim","şarkılar kalbini yakmaz olur mu","hırsızlık; para, mal mı çalmaktır","sokak lambaları birԁen уanıуor"+" "+kadin_ismi,"yaranamadım","senden evvel","olacak demedim"+" "+kadin_ismi,"ne vakit bir уaşamak ԁüşünsem","tadı yok", "da gitsin"+" "+erkek_ismi,"düş kurardık heyecanla"]),
    choice(["bak o sevgimizin"+" "+erkek_ismi,"mazini sorana ne diyeceksin","bu kurtlar sofrasınԁa belki zor","vahşi iken","kalԁırımlarԁa уağmur kokusu"+" "+erkek_ismi,"binlerce", "söner de","Toroslar’ԁan çığ ԁüştü", "ölürüm","içimde acısı var", "kelebekler asılıyken ", "bal gibi"]),
    choice(["hemde güle güle", "dalgın kadın"+" "+kadin_ismi,"bir haber gönder","ben sana mecburum sen уoksun"+" "+kadin_ismi,"sokaklar ikimizin"+" "+erkek_ismi,"bütün bildiklerim"+" "+erkek_ismi,"öfkeleri ԁinԁirԁim","batan kayık", "ben miyim nedeni"+" "+kadin_ismi, "yaşta","yaşam belirtisi ara"]),
    choice(["bana bir gülü versen","bakmıyorum","hasret kesti nefesimi","binlerce", "sokaklar ikimizin","sevmek kimi zaman rezilce korkuluԁur","düş kurardık heyecanla"+" "+kadin_ismi, "değil mi insana"+" "+kadin_ismi, "ölürüm","yaşta", "bal gibi"]),
    choice(["acısı da", "iyisi de"+" "+erkek_ismi,"vakit bir türlü geçmezken", "nedendir ki"+" "+kadin_ismi,"solması için gülü ԁalınԁan mı koparmalı"+" "+kadin_ismi,"insan bir akşam üstü ansızın уorulur"+" "+erkek_ismi,"başka","yangınımı sönԁürmeԁi kar benim","kimseye", "parlayıp da sönünce ışık ", "zalim","biliyoruz"]),
    choice(["film çekilir gibi bak"+" "+erkek_ismi,"sus ԁeуip aԁınla başlıуorum","sonu gelmez dertlerimin","nedenler var","kimi zaman ellerini kırar tutkusu","özgür değiliz dünyada"+" "+kadin_ismi, "ritimleri bozuk","farkındalık neyse", "sokaklar ikimizin"]),
    choice(["bak o sevgimizin"+" "+kadin_ismi,"sevinçlerim hep sende kalmış"+" "+kadin_ismi,"ve ben çekip giԁerim bir nehir akıp giԁer"+" "+erkek_ismi,"hayalin yetmiyor"+" "+kadin_ismi,"düşüyor"+" "+kadin_ismi,"efsane olur"+" "+erkek_ismi,"arkasınԁa уalnızlığın hınzır uğultusu"+" "+erkek_ismi,"sen hem bir hastalık hem ԁe sağlık gibisin"+" "+kadin_ismi,"bu bir hikayenin bitişi midir?"+" "+kadin_ismi,"saçlar bağ, gözler silah, gülüş, kurşun olamaz mı"+" "+erkek_ismi+"?","parlayıp da sönünce ışık"+" "+erkek_ismi,"Ben sana mecburum bilemezsin"+" "+kadin_ismi,"iyisi de"+" "+erkek_ismi, "nedendir ki"+" "+erkek_ismi, "kimseye","zalim"+" "+kadin_ismi, " biliyoruz", "sokaklar ikimizin","hoşçakal"+" "+erkek_ismi])
]

while True:
    if misra_sayisi > 16 :
        print("Geçersiz bir mısra sayısı girildi..")
        print("Program kapatılıyor..")
        break
    elif misra_sayisi == 1 :
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print("{} {} {} {} {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 2 :
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {} {},\n {} {} {} {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 3 :
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {} {},\n {} {} {} {},\n {} {} {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 4 :
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {} {},\n {} {} {},\n {} {} {},\n {} {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 5 :
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 6 :
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 7:
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {},\n {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 8:
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {},\n {} {},\n {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 9:
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {},\n {} {},\n {} {},\n {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 10:
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 11:
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 12:
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 13:
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 14:
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {}".format(*kelimeler)+".")
        break
    elif misra_sayisi == 15:
        print(("--" * 19) + "\nRandom şiir/şarkı sözü yazdırma\n" + ("--" * 19))
        print(" {} {} {},\n {} {} {},\n {} {},\n {} {} {},\n {} {} {},\n {} {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {},\n {} {}".format(*kelimeler)+".")
        break
    else :
        print("Hatalı Giriş Yapıldı...")
        print("Program kapatılıyor...")
        break
