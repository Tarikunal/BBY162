__author__ = "Tarık Ünal"
#Uygulama09-Final
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter
from tkinter import messagebox
import time
from random import randint
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
oyunRenkleri = []
kulRenkleri = []
count = 1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
renkler = {
    1: 'red',
    2: 'blue',
    3: 'yellow',
    4: 'green',
    'red': 'red',
    'blue': 'blue',
    'yellow': 'yellow',
    'green': 'green'}
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
temrenks = {
    'red': 'darkred',
    'blue': 'darkblue',
    'yellow': 'goldenrod',
    'green': 'darkgreen'}
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def RandomRenk():
    renk = randint(1, 4)
    oyunRenkleri.append(renkler[renk])
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def aydinlat(renk):
    buttons[renk].config(bg=renkler[renk])
    pencere.update()
    time.sleep(0.4)
    buttons[renk].config(bg=temrenks[renk])
    pencere.update()
    time.sleep(0.4)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Renklerigös():
    for renk in oyunRenkleri:
        aydinlat(renk)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def erişBut():
    red.config(state='normal')
    blue.config(state='normal')
    green.config(state='normal')
    yellow.config(state='normal')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def RenkEkl(renk):
    kulRenkleri.append(renk)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def RenkleriKontrolEt():
    global oyunRenkleri, kulRenkleri, count
    if oyunRenkleri == kulRenkleri:
        count += 1
        messagebox.showinfo("Tebrikler :)", "Doğru seçim :)\nGelecek seviye %d\nSonraki seviye için 'Oyna' butonuna bas!" % (count))
        kulRenkleri = []
        return True
    else:
        messagebox.showwarning("Kaybettin :(", "Yanlış seçim :(\nUlaştığın seviye %d" % (count))
        messagebox.showinfo("Tekrar Oyna :))","Yeniden Oynamak İçin 'Oyna' Butonuna Tıklaman Yeterli :))")
        kulRenkleri = []
        oyunRenkleri = []
        return False
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def mesaj():
    messagebox.showinfo("Sıra Sende", "Simon'ın seçtiği renkleri seç ve 'Kontrol Et' butonuna bas :)")
    erişBut()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def oyun():
    RandomRenk()
    Renklerigös()
    mesaj()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pencere= tkinter.Tk()
pencere.wm_iconbitmap("final_resim.ico")
baslik = pencere.title("Simon&Simon")
pencere.configure(background="black")
messagebox.showinfo("Simon&Simon'a Hoşgeldin","Simon Renkli Lambalar Hafıza Oyunu\n\nAmaç : Karmaşık sıra ile yanıp sönen renkli lambaların sırasını tekrar etmek.\n\nOyun Hakkında Bilgi : 'Oyna' butonuna basıp oyunu başlatın. Renkli lambalar birbiri ardına yanıp sönerler. Sizin göreviniz bu lambaların yanıp sönme sırasını hafızanızda tutmak ve gelen bildirimden sonra aynısını tekrarlayıp 'Kontrol Et' butonuna basmaktır.\nEğer şaşırırsanız oyun biter. Bu oyun başta kolay başlayıp ilerledikçe zorlaşan bir oyundur. Hafızanızı kuvvetlendirmek için çok faydalıdır.")
messagebox.showinfo("Oynamak için :)","'Oyna' butonuna basarak oyunu başlat :)")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
red = tkinter.Button(pencere, state='disabled', bg="darkred", activebackground="red", height="10", width="20",command=lambda: RenkEkl('red'))
blue = tkinter.Button(pencere, state='disabled', bg="darkblue", activebackground="blue", height="10", width="20",command=lambda: RenkEkl('blue'))
green = tkinter.Button(pencere, state='disabled', bg="darkgreen", activebackground="green", height="10", width="20",command=lambda: RenkEkl('green'))
yellow = tkinter.Button(pencere, state='disabled', bg="goldenrod", activebackground="yellow", height="10", width="20",command=lambda: RenkEkl('yellow'))
basla = tkinter.Button(pencere, text="Oyna", bg="white", command=oyun)
check = tkinter.Button(pencere, text="Kontrol Et", bg="white", command=RenkleriKontrolEt)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
buttons = {
    'red': red,
    'blue': blue,
    'yellow': yellow,
    'green': green}
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
red.grid(row=1, column=0)
blue.grid(row=1, column=1)
green.grid(row=2, column=0)
yellow.grid(row=2, column=1)
basla.grid(row=3, column=0)
check.grid(row=3, column=1)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pencere.mainloop()
