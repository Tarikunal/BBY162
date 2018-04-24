                #######################################################
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                #              Programlama ve Algoritmalar            #
                #                     Uygulama07                      #
                #                     Tarık Ünal                      #
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                #######################################################
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from PIL import ImageTk

# ---------------------------------------------------------------------------------------------------------------------------------------#
root = tk.Tk() 
t = tk.Label(root, text="PhotoViewer", background="yellow", font="DejaVuSans 11 underline")
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
t.pack(ipadx=200)
root.configure(background="black")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------#
fotograflar = "1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg", "11.jpg", "12.jpg", "13.jpg", "14.jpg", "15.jpg", "16.jpg", "17.jpg"
# ------------------------------------------------------------------------------------------------------------------------------------------------------------#
fotograf_listesi = []
for i in fotograflar:
    fotograf_listesi.append(ImageTk.PhotoImage(file=i))
label = None
say = 0
# ---------------------------------------------------------------------------------------------------------------------------------------#
def resimleri_goster():
    global label, say
    if label is not None:
        label.destroy()
    try:
        label = tk.Label(master=root, image=fotograf_listesi[say])
        label.pack()
        say -= 1
    except IndexError:
        say = 0
geriButon = tk.Button(master=root, text="<<<", background="yellow", cursor="star")
geriButon.pack(side="left")
geriButon.configure(command=resimleri_goster)
# ---------------------------------------------------------------------------------------------------------------------------------------#
def resimleri_goster():
    global label, say
    if label is not None:
        label.destroy()
    try:
        label = tk.Label(master=root, image=fotograf_listesi[say])
        label.pack()
        say += 1
    except IndexError:
        say = 0
ileriButon = tk.Button(master=root, text=">>>", background="yellow", cursor="mouse")
ileriButon.pack(side="right")
ileriButon.configure(command=resimleri_goster)
# ---------------------------------------------------------------------------------------------------------------------------------------#
# cıkıs = tk.Button(text = "Kapat", command=exit, fg="black", bg="yellow",cursor="man")
# cıkıs.pack(side="bottom",ipadx=1000)
cıkıs = tk.PhotoImage(file='exit.png')
tk.Button(image=cıkıs, bg="yellow", command=exit).pack(side="bottom", ipadx=100)
# ---------------------------------------------------------------------------------------------------------------------------------------#
root.mainloop()
