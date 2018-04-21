from tkinter import *
from PIL import Image, ImageTk

class uygulamaPencerem:
    def __init__(self, anaSayfa):
        self.anaSayfa = anaSayfa
        anaSayfa.title("test")

        self.etiket = Label(anaSayfa, text="Test")
        self.etiket.pack()

        self.sol=Button(anaSayfa, text="<<<")
        self.sol.pack(side=LEFT)

        self.sağ=Button(anaSayfa, text=">>>")
        self.sağ.pack(side=RIGHT)

        self.foto = Image.open("smile.jpg")
        self.tkimage = ImageTk.PhotoImage(self.foto)
        self.resim = Label(root, image=self.tkimage)
        self.resim.pack()

        self.kapatButonu = Button(anaSayfa, text="Kapat", command=anaSayfa.quit)
        self.kapatButonu.pack()

root = Tk()
yeniPencere = uygulamaPencerem(root)
root.mainloop()
