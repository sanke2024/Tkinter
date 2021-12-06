from tkinter import *
from PIL import ImageTk, Image

import sqlite3

def billing():
    pass
def inventory():
    pass
def analytics():
    pass

root=Tk()

# #setting tkinter window size
# width= root.winfo_screenwidth() 
# height= root.winfo_screenheight()
# root.geometry("%dx%d" % (width, height))
# root.attributes('-zoomed', True)
# root.geometry("1366x768")

bg = ImageTk.PhotoImage(Image.open("bg.jpg"))
label = Label(root,image=bg)
label.place(x=-10, y=-10)

# root.configure(background='green')
root.wm_state('zoomed')
# root.attributes('-fullscreen', True)
root.title("myStore")
button1=Button(root,text="Billing",padx=2,pady=2,width=30,height=3,command=billing,bg='white',font=10).pack(pady=(140,10))
button2=Button(root,text="Inventory",width=30,height=3,padx=2,pady=2,command=inventory,bg='white',font=10).pack(pady=10)
button2=Button(root,text="Analytics",width=30,height=3,padx=2,pady=2,command=analytics,bg='white',font=10).pack(pady=10)



root=mainloop()