from os import kill
from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
from tkinter import messagebox
import qrcode



root = Tk()
root.wm_state('zoomed')
# root.geometry("400x500")
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hp123",
            database="mystore1"
        )
my_cursor = mydb.cursor()

class title:
    def __init__(self):
        self.title = Label(root, text="Inventory", bg="blue", font=("Comic Sans MS", 30, "bold"), fg="black", width=1366, pady=10, relief=RIDGE)
        self.title.pack()
        self.cal = DateEntry(root, selectmode='day')
        self.cal.place(x=10, y=35)

class entry:
    def add_category_f(self,category):
        sql_command= "insert into item_category(category) values(%s)"
        values=(category)
       
        try:
                my_cursor.execute(sql_command,(values,))
                self.add_category.delete(0,END)
        except:
                messagebox.showerror("showerror","Some error occured")
        mydb.commit()
        self.fetch_category_list()

    def fetch_category_list(self):
        my_cursor.execute("select category from item_category")
        category_list=my_cursor.fetchall()
        self.item_category=Combobox(self.frame1)
        self.item_category_options=[]
        for x in category_list:
            self.item_category_options.append(x[0])
        self.item_category['values']=self.item_category_options
        self.item_category.grid(row=0,column=1,ipady=3)
        self.item_category.current(len(self.item_category_options)-1)

    def add_items(self):
        sql_command= "insert into products(name,category,price,stock) values(%s,%s,%s,%s);"
        values=( self.item_name.get(),self.item_category.get(),self.item_price.get(),self.item_stock.get())
       
        try:
            my_cursor.execute(sql_command,values)
        except:
                messagebox.showerror("showerror","Some error occured")
        mydb.commit()
        self.qrcode_generator()
    def qrcode_generator(self):
        img=qrcode.make(self.item_category.get()+","+self.item_name.get()+","+self.item_price.get())
        img.save("qr0.jpg")



    def __init__(self):

        self.frame1=LabelFrame(root,text="Items",pady=5,background="blue",fg="white",font=("Comic Sans MS", 15, "bold"),relief=GROOVE,bd=5)
        self.frame1.place(x=5,y=85,width=500)

        Label(self.frame1,text='Category:',font=('helvetica',15),height=1,relief=RAISED,width=10).grid(row=0,column=0,padx=20)


        self.fetch_category_list()

        # self.item_category=Entry(self.frame1,relief=GROOVE,bd=2,)
        # self.item_category.grid(row=0,column=1,ipady=3)

        Label(self.frame1,text='Item:',font=('helvetica',15),height=1,relief=RAISED,width=10).grid(row=1,column=0,padx=20)
        self.item_name=Entry(self.frame1,relief=GROOVE,bd=2,)
        self.item_name.grid(row=1,column=1,ipady=3)

        Label(self.frame1,text=' Price: ',font=('helvetica',15),height=1,relief=RAISED,width=10).grid(row=2,column=0,padx=20)
        self.item_price=Entry(self.frame1,relief=GROOVE,bd=2,)
        self.item_price.grid(row=2,column=1,ipady=3)

        Label(self.frame1,text=' Stock: ',font=('helvetica',15),height=1,relief=RAISED,width=10).grid(row=3,column=0,padx=20)
        self.item_stock=Entry(self.frame1,relief=GROOVE,bd=2,)
        self.item_stock.grid(row=3,column=1,ipady=3)

        Button(self.frame1,text=' Clear ',font=('helvetica',10),height=1,relief=RAISED).grid(row=4,column=0,padx=15,pady=10)
        Button(self.frame1,text=' Add ',font=('helvetica',10),height=1,relief=RAISED,command=self.add_items).grid(row=4,column=1,padx=15,)



        Label(self.frame1,text=' Remove Item: ',font=('helvetica',12),relief=RAISED).grid(row=5,column=0,padx=20)
        self.remove_item=Entry(self.frame1,relief=GROOVE,bd=2)
        self.remove_item.insert(0,"Enter name")
        self.remove_item.grid(row=5,column=1,ipady=3)
        Button(self.frame1,text=' Remove ',font=('helvetica',10),relief=RAISED).grid(row=5,column=2,padx=15,)

        Label(self.frame1,text='Add Category:',font=('helvetica',12),relief=RAISED).grid(row=6,column=0,padx=20)
        self.add_category=Entry(self.frame1,relief=GROOVE,bd=2)
        self.add_category.insert(0,"Enter name")
        self.add_category.grid(row=6,column=1,ipady=3)
        Button(self.frame1,text=' Add ',font=('helvetica',10),relief=RAISED,command=lambda:self.add_category_f(self.add_category.get())).grid(row=6,column=2,padx=15)
        # print(self.add_category.get())

        Label(self.frame1,text='Remove Category:',font=('helvetica',12),relief=RAISED).grid(row=7,column=0,padx=20)
        remove_category=Entry(self.frame1,relief=GROOVE,bd=2)
        remove_category.grid(row=7,column=1,ipady=3)
        Button(self.frame1,text=' Remove ',font=('helvetica',10),relief=RAISED).grid(row=7,column=2,padx=15,)


class customer:
    def add_category_f(self,category):
        sql_command= "insert into customer_category(category) values(%s)"
        values=(category)
       
        try:
                my_cursor.execute(sql_command,(values,))
                self.add_category.delete(0,END)
        except:
                messagebox.showerror("showerror","Some error occured")
        mydb.commit()
        self.fetch_category_list()
    def add_region(self,region):
        sql_command= "insert into region_(region) values(%s)"
        values=(region)
       
        try:
                my_cursor.execute(sql_command,(values,))
                self.region.delete(0,END)
        except:
                messagebox.showerror("showerror","Some error occured")
        mydb.commit()
        self.fetch_region_list()
    def fetch_category_list(self):
        my_cursor.execute("select category from customer_category")
        category_list=my_cursor.fetchall()
        self.customer_category=Combobox(self.frame2)
        self.customer_category.configure(width=10)
        self.customer_category_options=[]
        for x in category_list:
            self.customer_category_options.append(x[0])
        self.customer_category['values']=self.customer_category_options
        self.customer_category.grid(row=3,column=1,sticky=W)
        self.customer_category.current(len(self.customer_category_options)-1)
    def fetch_region_list(self):
        my_cursor.execute("select region from region_")
        region_list=my_cursor.fetchall()
        self.region_category=Combobox(self.frame2)
        self.region_category.configure(width=10)
        self.region_category_options=[]
        for x in region_list:
            self.region_category_options.append(x[0])
        self.region_category['values']=self.region_category_options
        self.region_category.grid(row=3,column=1,sticky=E)
        self.region_category.current(len(self.region_category_options)-1)
    def add_customer(self):
        sql_command= "insert into customer(name,mobile,address,category,total_sales,age,region) values(%s,%s,%s,%s,%s,%s,%s)"
        values=( self.name.get(),str(self.mobile.get()),self.address.get(),self.customer_category.get(),0,self.age.get(),self.region_category.get())
       
        # try:
        my_cursor.execute(sql_command,values)
        # except:
                # messagebox.showerror("showerror","Some error occured")
        mydb.commit()       
    def __init__(self) :
        self.frame2=LabelFrame(root,text="Add Customer",pady=8,background="blue",fg="white",font=("Comic Sans MS", 10, "bold"),relief=GROOVE,bd=5)
        self.frame2.place(x=5,y=380,width=500)

        Label( self.frame2,text='Name:',font=('helvetica',9),height=1,relief=RAISED,width=10).grid(row=0,column=0,padx=20)
        self.name=Entry( self.frame2,relief=GROOVE,bd=2,width=15)
        self.name.grid(row=0,column=1,ipady=2,sticky=W)

        Label( self.frame2,text='Age:',font=('helvetica',9),height=1,relief=RAISED,width=5).grid(row=0,column=1,padx=20)
        self.age=Entry( self.frame2,relief=GROOVE,bd=2,width=5)
        self.age.grid(row=0,column=1,ipady=2,sticky=E)

        Label( self.frame2,text='Mobile:',font=('helvetica',9),height=1,relief=RAISED,width=10).grid(row=1,column=0,padx=20)
        self.mobile=Entry( self.frame2,relief=GROOVE,bd=2,)
        self.mobile.grid(row=1,column=1,ipady=2,sticky=W)

        Label( self.frame2,text='Address:',font=('helvetica',9),height=1,relief=RAISED,width=10).grid(row=2,column=0,padx=20)
        self.address=Entry( self.frame2,relief=GROOVE,bd=2,width=50)
        self.address.grid(row=2,column=1,sticky=W)

        Label( self.frame2,text='Category:',font=('helvetica',9),height=1,relief=RAISED,width=10).grid(row=3,column=0)
        self.fetch_category_list()
        Label( self.frame2,text='Region:',font=('helvetica',9),height=1,relief=RAISED,width=10).grid(row=3,column=1)
        self.fetch_region_list()

        # self.category=Entry( self.frame2,relief=GROOVE,bd=2,width=5)
        # self.category.grid(row=3,column=1,sticky=W)

        Button( self.frame2,text=' Clear ',font=('helvetica',9),relief=RAISED).grid(row=4,column=0,pady=5)
        Button( self.frame2,text=' Add ',font=('helvetica',9),relief=RAISED,command=self.add_customer).grid(row=4,column=1)

        Label( self.frame2,text='Remove customer:',font=('helvetica',9),relief=RAISED).grid(row=5,column=0)
        self.remove_mobile=Entry( self.frame2,relief=GROOVE,bd=2,width=20)
        self.remove_mobile.grid(row=5,column=1,sticky=W)
        self.remove_mobile.insert(0,"Enter mobile no. ")
        Button( self.frame2,text='Remove',font=('helvetica',10),relief=RAISED).grid(row=5,column=1,sticky=E)

        Label( self.frame2,text='Add Category:',font=('helvetica',12),relief=RAISED).grid(row=6,column=0)
        self.add_category=Entry( self.frame2,relief=GROOVE,bd=2)
        self.add_category.grid(row=6,column=1,ipady=3,sticky=W)
        Button( self.frame2,text=' Add ',font=('helvetica',9),relief=RAISED,command=lambda:self.add_category_f(self.add_category.get())).grid(row=6,column=1,sticky=E)

        Label( self.frame2,text='Region:',font=('helvetica',9),relief=RAISED).grid(row=7,column=0)
        self.region=Entry( self.frame2,relief=GROOVE,bd=2)
        self.region.grid(row=7,column=1,ipady=3,sticky=W)
        Button( self.frame2,text=' Add ',font=('helvetica',10),relief=RAISED,command=lambda:self.add_region(self.region.get())).grid(row=7,column=1,sticky=E)

        Label( self.frame2,text='Remove Category:',font=('helvetica',9),relief=RAISED).grid(row=8,column=0)
        self.remove_category=Entry( self.frame2,relief=GROOVE,bd=2)
        self.remove_category.grid(row=8,column=1,ipady=3,sticky=W)
        Button( self.frame2,text=' Remove ',font=('helvetica',9),relief=RAISED).grid(row=8,column=1,sticky=E)


class lookup:
    def __init__(self):
        self.frame3=LabelFrame(root,text="Look Up",bd=5,padx=0,bg="blue",fg="white",relief=GROOVE,labelanchor=N,font=("Comic Sans MS", 10, "bold"))
        self.frame3.place(x=510,y=85,width=765,height=570)

        self.options = ["Item Categories","Customer Categories","Items","Customers","Bills"]
        self.clicked = StringVar()
        self.drop = OptionMenu( self.frame3  ,  self.clicked , * self.options )
        self.drop.pack()
        # drop.bind()

        #scroll bar attached to text area
        self.scroll_y=Scrollbar( self.frame3,orient=VERTICAL)
        self.text_area=Text( self.frame3,yscrollcommand= self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_y.config(command= self.text_area.yview)
        self.text_area.pack()
        
        



title_frame=title()
entry_window=entry()
customre_window=customer()
lookup_window=lookup()
root=mainloop()