import tkinter as tk

class window:
    def __init__(self,root):
        self.root = root
        self.root.title("listbox")
        self.root.geometry("700x500+0+0")

        listbox = tk.Listbox(root,height=100,width=100,bg="gray",fg="blue",font="helvetica")
        listbox.pack()

        listbox.insert(tk.END,"pizza")
        listbox.insert(tk.END,"burger")
        listbox.insert(tk.END,"chowmin")
        listbox.insert(tk.END,"frinch frize")
        listbox.delete(tk.END)



        self.root.mainloop()





if __name__=="__main__":
    print("hello world")

    root = tk.Tk()
    window(root)


