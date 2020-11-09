import tkinter as tk; import tkinter.font as font
root = tk.Tk()
root.geometry("800x700+300+60")
root.title("Tic-Tac-Toe")
player = 'O'
def game():
    delete_screen()
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, wlabel, pbutton
    ttframe = tk.Frame(root)
    tframe = tk.Frame(root)
    cframe = tk.Frame(root)
    bframe = tk.Frame(root)
    ttframe.pack(anchor="n")
    tframe.pack(anchor="n")
    cframe.pack(anchor="center")
    bframe.pack(anchor="s")

    wlabel = tk.Label(ttframe, text="Tic-Tac-Toe", fg="black", font=10)
    wlabel.grid(row=0, column=0, pady=(50, 0))
    pbutton = HoverButton(ttframe, activebackground='red', text="Play again!", fg="black", font=('Helvetica', '10'), bg="#c7c7c7", width=0, height=0, command=lambda: game())
    
    b1 = HoverButton(tframe, activebackground='green', text=" ", fg="black", bg="#c7c7c7", font=('Helvetica', '20'), width=12, height=4, command=lambda: tl(b1))
    b1.grid(row=0, column=0, pady=(70, 1), padx=(0, 1))
    b2 = HoverButton(tframe, activebackground='green', text=" ", fg="black", bg="#c7c7c7", font=('Helvetica', '20'), width=12, height=4, command=lambda: tl(b2))
    b2.grid(row=0, column=1, pady=(70, 1), padx=(0, 1))
    b3 = HoverButton(tframe, activebackground='green', text=" ", fg="black", bg="#c7c7c7", font=('Helvetica', '20'), width=12, height=4, command=lambda: tl(b3))
    b3.grid(row=0, column=2, pady=(70, 1), padx=(0, 1))

    b4 = HoverButton(cframe, activebackground='green', text=" ", fg="black", bg="#c7c7c7", font=('Helvetica', '20'), width=12, height=4, command=lambda: tl(b4))
    b4.grid(row=1, column=0, pady=(0, 1), padx=(0, 1))
    b5 = HoverButton(cframe, activebackground='green', text=" ", fg="black", bg="#c7c7c7", font=('Helvetica', '20'), width=12, height=4, command=lambda: tl(b5))
    b5.grid(row=1, column=1, pady=(0, 1), padx=(0, 1))
    b6 = HoverButton(cframe, activebackground='green', text=" ", fg="black", bg="#c7c7c7", font=('Helvetica', '20'), width=12, height=4, command=lambda: tl(b6))
    b6.grid(row=1, column=2, pady=(0, 1), padx=(0, 1))

    b7 = HoverButton(bframe, activebackground='green', text=" ", fg="black", bg="#c7c7c7", font=('Helvetica', '20'), width=12, height=4, command=lambda: tl(b7))
    b7.grid(row=2, column=0, pady=(0, 1), padx=(0, 1))
    b8 = HoverButton(bframe, activebackground='green', text=" ", fg="black", bg="#c7c7c7", font=('Helvetica', '20'), width=12, height=4, command=lambda: tl(b8))
    b8.grid(row=2, column=1, pady=(0, 1), padx=(0, 1))
    b9 = HoverButton(bframe, activebackground='green', text=" ", fg="black", bg="#c7c7c7", font=('Helvetica', '20'), width=12, height=4, command=lambda: tl(b9))
    b9.grid(row=2, column=2, pady=(0, 1), padx=(0, 1))

    
class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        if self['state'] == 'disabled':
            pass
        else:
            self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        
def change_player():
    global player

    if player == 'O':
        player = 'X'
    else:
        player = 'O'


def check_winner():
    global wlabel, pbutton
    if b1['text']  == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or\
    b4['text']  == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or\
    b7['text']  == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or\
    b1['text']  == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or\
    b2['text']  == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or\
    b3['text']  == 'O' and b6['text'] == 'O' and b9['text'] == 'O' or\
    b1['text']  == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or\
    b3['text']  == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        for x in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
            x.config(state = 'disabled')
        wlabel.config(text = "O is the winner")
        pbutton.grid(row=0, column=3, sticky="s", padx=(10, 0))

    elif b1['text']  == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or\
    b4['text']  == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or\
    b7['text']  == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or\
    b1['text']  == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or\
    b2['text']  == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or\
    b3['text']  == 'X' and b6['text'] == 'X' and b9['text'] == 'X' or\
    b1['text']  == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or\
    b3['text']  == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        for x in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
            x.config(state = 'disabled')
        wlabel.config(text = "X is the winner")
        pbutton.grid(row=1, column=0, sticky="s", padx=(10, 0))

def tl(b):
    global player
    b.configure(text = player, state=tk.DISABLED, fg='black')
    change_player()
    check_winner()

def delete_screen() :
    s = root.winfo_children()

    for i in s :
        try:
            i.destroy()
        except:
            i.delete()
    root.config(bg = "SystemButtonFace")
game()
root.mainloop()
