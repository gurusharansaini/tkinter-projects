import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.geometry("400x400")
root.title("File Explorar")

def select_file():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
     
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)



btn_explor = tk.Button(root,command=select_file,text="Search File")
btn_exit = tk.Button(root,command=exit,text="Exit")

label_file_explorer = tk.Label(root, 
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4, 
                            fg = "blue")


label_file_explorer.grid(row=1,column=1)
btn_explor.grid(row=1,column=2)
btn_exit.grid(row=1,column=3)

root.mainloop()
