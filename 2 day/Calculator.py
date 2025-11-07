import tkinter as tk
expr = ""

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("Errot")
        expr = ""


def clear():
    global expr
    expr = ""
    display.set("")





if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("270x150")
    root.title("Calculator")

    display = tk.StringVar()
    entry = tk.Entry(root,textvariable=display,bg="gray")
    entry.grid(columnspan=4,ipadx=70)


    #Number buttons
    btn1 = tk.Button(root,text="1",fg="black",bg="white" ,command=lambda:press('1'),height=1,width=7)
    btn1.grid(row=2,column=0)
    btn1 = tk.Button(root,text="2",fg="black",bg="white" ,command=lambda:press('2'),height=1,width=7)
    btn1.grid(row=2,column=1)
    btn1 = tk.Button(root,text="3",fg="black",bg="white" ,command=lambda:press('3'),height=1,width=7)
    btn1.grid(row=2,column=2)
    btn1 = tk.Button(root,text="4",fg="black",bg="white" ,command=lambda:press('4'),height=1,width=7)
    btn1.grid(row=3,column=0)
    btn1 = tk.Button(root,text="5",fg="black",bg="white" ,command=lambda:press('5'),height=1,width=7)
    btn1.grid(row=3,column=1)
    btn1 = tk.Button(root,text="6",fg="black",bg="white" ,command=lambda:press('6'),height=1,width=7)
    btn1.grid(row=3,column=2)
    btn1 = tk.Button(root,text="7",fg="black",bg="white" ,command=lambda:press('7'),height=1,width=7)
    btn1.grid(row=4,column=0)
    btn1 = tk.Button(root,text="8",fg="black",bg="white" ,command=lambda:press('8'),height=1,width=7)
    btn1.grid(row=4,column=1)
    btn1 = tk.Button(root,text="9",fg="black",bg="white" ,command=lambda:press('9'),height=1,width=7)
    btn1.grid(row=4,column=2)
    btn1 = tk.Button(root,text="0",fg="black",bg="white" ,command=lambda:press('0'),height=1,width=7)
    btn1.grid(row=5,column=1)

    #operator btn
    plus = tk.Button(root,text="+",fg="black",bg="white" ,command=lambda:press('+'),height=1,width=7)
    plus.grid(row=2,column=3)

    minus = tk.Button(root,text="-",fg="black",bg="white" ,command=lambda:press('-'),height=1,width=7)
    minus.grid(row=3,column=3)

    mult = tk.Button(root,text="*",fg="black",bg="white" ,command=lambda:press('*'),height=1,width=7)
    mult.grid(row=4,column=3)

    div = tk.Button(root,text="/",fg="black",bg="white" ,command=lambda:press('/'),height=1,width=7)
    div.grid(row=5,column=3)

#other buttons

    equ = tk.Button(root,text="=",fg="black",bg="white" ,command=equal,height=1,width=7)
    equ.grid(row=5,column=0)

    clr = tk.Button(root,text="clr",fg="black",bg="white" ,command=clear,height=1,width=7)
    clr.grid(row=6,column=1)

    dot = tk.Button(root,text=".",fg="black",bg="white" ,command=lambda:press('.'),height=1,width=7)
    dot.grid(row=5,column=2)

    root.mainloop()