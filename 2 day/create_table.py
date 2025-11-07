import tkinter as tk

root = tk.Tk()
root.geometry("950x150")
root.title("Entry table")
list1 = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]

for i in range(0,5):
    for j in range(0,4):

        e = tk.Entry(root,fg="blue",bg= "white",font=('Arial',16,'bold'))
        e.grid(row=i,column=j)
        e.insert(0,str(list1[i][j]))


root.mainloop()

