from tkinter import *
from tkinter import ttk

halfBlack = "#292929"
white = "#feffff"
azul = "#38576b"
cinza = "#eceff1"
laranga = "#f57e1d"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x314")
janela.config(bg=halfBlack)

frame_tela = Frame(janela, width=235, height=50, bg=azul)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=264)
frame_corpo.grid(row=1, column=0)

todosValores = ""

def entrada(event):
    global todosValores
    todosValores = todosValores + str(event)
    valorText.set(todosValores)

def calcular():
    global todosValores
    a = eval(todosValores)
    valorText.set(a) 
    todosValores = ""

def clear():
    global todosValores
    todosValores = ""
    valorText.set("")

valorText = StringVar()

app_label = Label(frame_tela, textvariable=valorText, width=16, height=2, padx=6, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=azul, fg=white)
app_label.place(x=0, y=0)

b_1 = Button(frame_corpo, command=clear, text="Clear", width=11, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda: entrada('%'), text="%", width=5, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command=lambda: entrada('/'), text="/", width=5, height=2, bg=laranga, fg=white, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command=lambda: entrada('7'), text="7", width=5, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=53)
b_5 = Button(frame_corpo, command=lambda: entrada('8'), text="8", width=5, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=53)
b_6 = Button(frame_corpo, command=lambda: entrada('9'), text="9", width=5, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=53)
b_7 = Button(frame_corpo, command=lambda: entrada('*'), text="*", width=5, height=2, bg=laranga, fg=white, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=53)

b_8 = Button(frame_corpo, command=lambda: entrada('4'), text="4", width=5, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=106)
b_9 = Button(frame_corpo, command=lambda: entrada('5'), text="5", width=5, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=106)
b_10 = Button(frame_corpo, command=lambda: entrada('6'), text="6", width=5, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=106)
b_11 = Button(frame_corpo, command=lambda: entrada('-'), text="-", width=5, height=2, bg=laranga, fg=white, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=106)

b_12 = Button(frame_corpo, command=lambda: entrada('1'), text="1", width=5, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=159)
b_13 = Button(frame_corpo, command=lambda: entrada('2'), text="2", width=5, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=159)
b_14 = Button(frame_corpo, command=lambda: entrada('3'), text="3", width=5, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=159)
b_15 = Button(frame_corpo, command=lambda: entrada('+'), text="+", width=5, height=2, bg=laranga, fg=white, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=159)

b_1 = Button(frame_corpo, command=lambda: entrada('0'), text="0", width=11, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=212)
b_18 = Button(frame_corpo, command=lambda: entrada('.'), text=".", width=5, height=2, bg=cinza, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_18.place(x=118, y=212)
b_19 = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=laranga, fg=white, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_19.place(x=177, y=212)

janela.mainloop()
