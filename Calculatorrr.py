from tkinter import *
a=Tk()
a.title("APP")
a.geometry("320x320")
a.title("Calculator")

def buttonclick(item):
    global expression
    expression=expression+str(item)
    intxt.set(expression)

def buttonclear():
    global expression
    expression=""
    intxt.set("")

def buttonequal():
    global expression
    final_answer=str(eval(expression))
    intxt.set(final_answer)
    expression=""

expression=""

intxt=StringVar()

e=Entry(a,width=50,bg="teal",bd=5,cursor="dot",textvariable=intxt).pack()

a1=Button(text=" 1 ",bd=20,command=lambda: buttonclick(1)).place(x=0,y=50)
a2=Button(text=" 4 ",bd=20,command=lambda: buttonclick(4)).place(x=0,y=110)
a3=Button(text=" 7 ",bd=20,command=lambda: buttonclick(7)).place(x=0,y=170)
a4=Button(text=" / ",bd=20,command=lambda: buttonclick("/")).place(x=0,y=230)

b1=Button(text=" 2 ",bd=20,command=lambda: buttonclick(2)).place(x=60,y=50)
b2=Button(text=" 5 ",bd=20,command=lambda: buttonclick(5)).place(x=60,y=110)
b3=Button(text=" 8 ",bd=20,command=lambda: buttonclick(8)).place(x=60,y=170)
b4=Button(text=" 0 ",bd=20,command=lambda: buttonclick(0)).place(x=60,y=230)

c1=Button(text=" 3 ",bd=20,command=lambda: buttonclick(3)).place(x=120,y=50)
c2=Button(text=" 6 ",bd=20,command=lambda: buttonclick(6)).place(x=120,y=110)
c3=Button(text=" 9 ",bd=20,command=lambda: buttonclick(9)).place(x=120,y=170)
c4=Button(text=" % ",bd=20,command=lambda: buttonclick("%")).place(x=120,y=230)

d1=Button(text=" + ",bd=20,command=lambda: buttonclick("+")).place(x=180,y=50)
d2=Button(text=" - ",bd=20,command=lambda: buttonclick("-")).place(x=180,y=110)
d3=Button(text=" x ",bd=20,command=lambda: buttonclick("*")).place(x=180,y=170)
d4=Button(text=" . ",bd=20,command=lambda: buttonclick(".")).place(x=180,y=230)

clear=Button(text=" C ",bd=20,command=lambda: buttonclear()).place(x=240,y=50)
equals=Button(text=" = ",bd=20,command=lambda: buttonequal()).place(x=240,y=110)
d3=Button(text="  ",bd=20).place(x=240,y=170)
d4=Button(text="  ",bd=20).place(x=240,y=230)



a.mainloop()