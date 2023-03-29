from tkinter import *
win = Tk()

frame_bottom = Frame(win)
frame_bottom = LabelFrame(win, text='word 2000')
frame_bottom.pack(padx = 10, pady = 7, ipadx = 5)

text = Text(frame_bottom, wrap=WORD, width=25, height=5,bg = 'red', fg = 'white' )
scrooll = Scrollbar(frame_bottom ,command=text.yview)
scrooll.pack(side = RIGHT ,fill=Y)
text.config(yscrollcommand=scrooll.set)
text.pack(side=LEFT)

frame_down = Frame(win)
frame_down = LabelFrame(win, text='вещи для word')
frame_down.pack(side = LEFT, padx = 10, pady = 7, ipadx = 5)

def get_text():
    s = text.get(1.0, END)
    lab1['text'] = s

lab1 = Label(frame_down, font = 'Arleal 12')
lab1.pack()

Button(frame_down, text="ctl+c",
       command=get_text, bg = 'yellow').pack(side=LEFT)

def delete_text():
    text.delete(1.0, END)

but2 = Button(frame_down, text = 'backSpaiy',
              command=delete_text, bg = 'yellow')
but2.pack(side=LEFT)

def insert_text():
    s = text.get(1.0, END)

    text.insert(1.0, s)

but3 = Button(frame_down, text = 'ctl+v',
              command=insert_text, bg = 'yellow')
but3.pack(side=LEFT)


win.mainloop()