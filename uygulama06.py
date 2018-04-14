_author_="Tarık Ünal"
import random
from tkinter import *
class Uygulama06:
    def __init__(self,master):
        self.master = master
        master.title("Uygulama06")
        master.configure(background="black")

        self.label= Label(master,text="BBY162 Programlama ve Algoritmalar",font=("Helvetica", 15),fg="yellow",bg="blue")
        self.label.pack()

        self.günün_siiri = Button(master, text="Günün Şiiri",font=("Helvetica", 12),fg="yellow", command=self.siir, bg = "blue",cursor="star")
        self.günün_siiri.pack(side=LEFT)

        self.günün_filmi = Button(master, text="Günün Filmi",font=("Helvetica", 12),fg="yellow", command=self.film, bg = "blue",cursor="mouse")
        self.günün_filmi.pack(side=RIGHT)

        self.çıkış = Button(master, text="ÇIKIŞ",font=("Helvetica", 6),command=master.quit, bg = "red",cursor="man")
        self.çıkış.pack(side="bottom")
    def siir(self):
        siirler = ("\n\nGeleceğim bekle dedi gitti\nBen beklemedim,\nO da gelmedi.\nÖlüm gibi bir şey oldu\nAma kimse ölmedi..","\n\nBir martı göğü ikiye bölüyor\nYakınlarda deniz olmalı\nDiyorum\nSonra\nGözlerin aklıma geliyor.","\n\nNe atom bombası\nNe londra konferansı\nBir elinde cımbız\nBir elinde ayna\nUmurunda mı dünya","\n\nSu başında durmuşuz,\nSu serin\nÇınar ulu...\nBen şiir yazıyorum\nKedi uyukluyor\nGüneş sıcak\nÇok şükür yaşıyoruz\nSuyun şavkı vuruyor bize\nÇınara, bana, kediye, güneşe\nBir de ömrümüze..","\n\n...iki kar tanesi gibi\nDüşerken gökten birbirini kovalayarak,\nNe güzel seninle aynı dünyayı paylaşmak\nVe uyumak aynı gök altında\nÖlü ya da diri olarak...","\n\nBeni bu güzel havalar mahvetti,\nBöyle havada istifa ettim\nEvkaftaki memuriyetimden.\nTütüne böyle havada alıştım,\nBöyle havada âşık oldum;\nEve ekmekle tuz götürmeyi\nBöyle havalarda unuttum;\nŞiir yazma hastalığım\nHep böyle havalarda nüksetti;\nBeni bu güzel havalar mahvetti.","\n\nSon karesi gibi Red Kit'in\nBatan güneşe doğru\nSürerken atımı\nGitme kal demeni bekliyordum\nAma yalnızca\nRüzgar çekiştiriyordu atkımı")
        secilen_siir = random.choice(siirler)
        self.siirim = Label(self.master, text=secilen_siir)
        self.siirim.pack()
    def film(self):
        fimler = ("\nYaşam Şifresi / Source Code (2011)","\nBen Efsaneyim / I Am Legend (2007)","\nOndan Uzakta / Away from Her (2006)","\nDünya Savaşı Z / World War Z (2013)","\nTruman Şov / The Truman Show (1998)","\nBaşlangıç / Inception (2010)"," \nSiyah Giyen Adamlar 3 (2012)","\nX-Men: Geçmiş Günler Gelecek (2014)","\nMakinist / The Machinist (2004)","\nFelekten bir Gece / The Hangover (2009)","\nDeadpool (2016)","\nBlack Panther (2018)","\nIşığın Bittiği Yer / The Abyss (1989)","\nYarının Sınırında / Edge of Tomorrow (2014)","\nUzay Yolu / Star Trek (2009)","\nDeja Vu (2006)","\nPrometheus (2012)","\nYapay Zeka / Artificial Intelligence: AI (2001)","\nYaşam Şifresi / Source Code (2011)","\nNot Defteri / The Notebook (2004)","\nHiroşima Sevgilim / Hiroshima mon amour (1959)","\nPiyanist / The Pianist (2002)","\nYerdeki Yıldızlar / Taare Zameen Par (2007)","\nYenilmezler: Ultron Çağı / Avengers: Age of Ultron (2015)","\nPK (2014)","\nEjderha Dövmeli Kız / Män Som Hatar Kvinnor (2009)","\nIron Man 3 (2013)","\nGalaksinin Koruyucuları (2014) ","\nOtomatik Portakal / A Clockwork Orange (1971)")
        secilen_film = random.choice(fimler)
        self.filmim = Label(self.master, text=secilen_film)
        self.filmim.pack()
root = Tk()
my_gui = Uygulama06(root)
root.mainloop()
