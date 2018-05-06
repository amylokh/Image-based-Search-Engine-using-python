from Tkinter import * 
window = Tk()
window.title("Image-Search Engine")
window.geometry('450x550') 
lbl = Label(window, text="Welcome to the Image Search Engine",
            font=("Times New Roman",20 ))
lbl.grid(column=0, row=0)

lbl_2 = Label(window,text="Enter Image name:",font=("Times New Roman",14))
lbl_2.grid(column=0,row=1)
txt = Entry(window,width=20)
txt.grid(column=0, row=2)

def clicked():
 
    res = txt.get()
 
    lbl.configure(text= res) #Change configure function to image search

btn = Button(window, text="Search", command=clicked)
btn.grid(column=0, row=3)
window.mainloop()
