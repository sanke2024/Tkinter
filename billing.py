from os import kill
from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk, Image
import sqlite3
from babel.dates import DateTimeFormat
from tkcalendar import *
import mysql.connector
import pyzbar.pyzbar as pyzbar
import cv2
import qr
from tkinter.ttk import Combobox
from tkinter import messagebox


root=Tk()
root.wm_state('zoomed')
# root.geometry("400x500")
root.configure(bg="blue")

mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hp123",
            database="mystore1"
        )
my_cursor = mydb.cursor()

class title:
    def __init__(self):
        self.title = Label(root, text="Billing", bg="blue", font=("Comic Sans MS", 30, "bold"), fg="black", width=1366, pady=10, relief=RIDGE)
        self.title.pack()
        self.cal = DateEntry(root, selectmode='day',date_pattern='dd/mm/yyyy')
        self.cal.place(x=10, y=35)
        # print(self.cal.get_date())               2021-12-06




##################### BILL FRAME
bill_frame=LabelFrame(root,text="Bill",relief=GROOVE,labelanchor=N,bg="blue",font=("Comic Sans MS", 20, "bold"),bd=5,fg="white")
bill_frame.place(x=710,y=85,width=560)

        #scroll bar attached to text area
scroll_y=Scrollbar(bill_frame,orient=VERTICAL)
text_area=Text(bill_frame,yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=text_area.yview)
text_area.pack()
default="                         Mystore limited      \n                       New delhi, 100001,India\n                 ***********************************\n  Date:                                 	       Bill no:        \n -----------------------------------------------------------------\nName                     Price                     Amount"
text_area.insert(END,default)



class execute:
    
    # @staticmethod
    def update_bill_table(self):
        print("hello")
        sql_command= "insert into mystore1.sales(product_name,product_category,bill_number,product_price,amount) values(%s,%s,(select id from mystore1.bill where id=last_insert_id()),%s,%s);"

        try:
            my_cursor.executemany(sql_command,self.values)
            # print(self.values)
            # print("executed")
        except:
                messagebox.showerror("showerror","Some error occured")
        mydb.commit()
        # fetch_category_list()
    def __init__(self):
        self.values=[]

class Entry_frame:
    def to_database(self):
        pass
        
    def delete_last_line(self):
        text_area.delete("end-1c linestart",END)
        
    total=1
    is_same_item=""   
    def sc1(self,execute1):
        # self.total=int(self.amount.get())
        self.update_bill(self.all_items.get(),self.price.get(),1)
        tuple_for_database=(self.all_items.get(),self.item_category.get(),self.price.get(),self.amount.get())
        execute1.values.append(tuple_for_database)
        # execute1.update_bill_table()
        
        # print(type(execute.values[0]))

        # print(tuple_for_database)
    def sc2(self):
        qr.scan()
        self.update_bill(qr.final_result[1],qr.final_result[2])   
        # self.amount.insert(0,1)
        tuple_for_database=(qr.final_result[1],qr.final_result[0],qr.final_result[2],1)
        # print(tuple_for_database)
        execute1.values.append(tuple_for_database)
        # execute1.update_bill_table()
       
    def update_bill(self,name,price,fromsc1=None):
            if str(self.is_same_item) == str(name):
                if fromsc1:
                    self.total=self.total+int(self.amount.get())
                else:
                    self.total+=1
                to_text=str("\n"+name)+"                 "+str(price)+"                      "+str(self.total)
                self.is_same_item=name
                self.delete_last_line()
                text_area.insert(END,to_text)
                # print(self.total)
            else:
                if fromsc1:
                    self.total=int(self.amount.get())
                else:
                    self.total=1
                to_text="\n"+str(name)+"                 "+str(price)+"                      "+str(self.total)
                self.is_same_item=name
                text_area.insert(END,to_text)

            
    # def add_items(self):
    #     sql_command= "insert into products(name,category,price,stock) values(%s,%s,%s,%s);"
    #     values=( self.item.get(),self.item_category.get(),self.price.get(),self.item_stock.get())
       
    #     try:
    #         my_cursor.execute(sql_command,values)
    #     except:
    #             messagebox.showerror("showerror","Some error occured")
    #     mydb.commit()

    def fetch_category_list(self):
        my_cursor.execute("select category from item_category")
        category_list=my_cursor.fetchall()
        self.item_category=Combobox(self.frame1)
        self.item_category_options=[]
        for x in category_list:
            self.item_category_options.append(x[0])
        self.item_category['values']=self.item_category_options
        self.item_category.grid(row=0,column=1)
        self.item_category.current(len(self.item_category_options)-1)
        self.fetch_item_list()
        #simple binding don't work with comboboxes
        self.item_category.bind('<<ComboboxSelected>>',lambda event: self.fetch_item_list())


    def fetch_item_list(self):
        # print(self.item_category.get())
        sql="select name from products where category=%s;"
        values=(self.item_category.get())
        my_cursor.execute(sql,(values,))
        item_list=my_cursor.fetchall()
        self.all_items=Combobox(self.frame1)
        self.all_items_options=[]
        for x in item_list:
            self.all_items_options.append(x[0])
        self.all_items['values']=self.all_items_options
        self.all_items.grid(row=1,column=1)
        self.all_items.current(0)
        self.all_items.bind('<<ComboboxSelected>>',lambda event: self.fill_price())
    def fill_price(self):
        sql="select price from products where name=%s;"
        values=(self.all_items.get())
        my_cursor.execute(sql,(values,))
        item_list=my_cursor.fetchall()
        self.price.delete(0,END)
        self.price.insert(END,item_list[0])
        # print(item_list[0])
    def __init__(self):
        self.frame1=LabelFrame(root,text="Entry",padx=0,pady=20,background="blue",fg="white",font=("Comic Sans MS", 20, "bold"),relief=GROOVE,labelanchor=N,bd=5)
        self.frame1.place(x=5,y=85,width=700)

        # bg = ImageTk.PhotoImage(Image.open("bg.jpg"))
        # label = Label(frame1,image=bg)
        # label.place(x=-550, y=-550)

        Label(self.frame1,text='Category:',font=('helvetica',15),height=1,relief=RAISED,width=10).grid(row=0,column=0,pady=10)
        self.fetch_category_list()
        # Entry(self.frame1,relief=GROOVE,bd=2,).grid(row=0,column=1,ipady=3,pady=10)
        Label(self.frame1,text='Item:',font=('helvetica',15),height=1,relief=RAISED,width=10).grid(row=1,column=0,padx=20,pady=10)
        # self.item=Entry(self.frame1,relief=GROOVE,bd=2,)
        # self.item.grid(row=1,column=1,ipady=3,pady=10)
        Label(self.frame1,text=' Price: ',font=('helvetica',15),height=1,relief=RAISED,width=10).grid(row=2,column=0,padx=20,pady=10)
        self.price=Entry(self.frame1,relief=GROOVE,bd=2,)
        self.price.grid(row=2,column=1,ipady=3,pady=10)
        self.fill_price()

        Label(self.frame1,text=' Amount: ',font=('helvetica',15),height=1,relief=RAISED,width=10).grid(row=3,column=0,padx=20,pady=10)
        self.amount=Entry(self.frame1,relief=GROOVE,bd=2,)
        self.amount.grid(row=3,column=1,ipady=3,pady=10)
        Button(self.frame1,text=' Clear ',font=('helvetica',15),height=1,relief=RAISED).grid(row=4,column=0,padx=15,pady=30)
        Button(self.frame1,text=' Add ',font=('helvetica',15),height=1,relief=RAISED,command=lambda:self.sc1(execute1)).grid(row=4,column=1,padx=15,pady=30)

        self.qr_bg = ImageTk.PhotoImage(Image.open("qr1.jpg"))
        self.label = Label(root,image=self.qr_bg)
        self.label.place(x=530, y=160)
        Button(root,text=' Scan ',font=('helvetica',12),height=1,relief=RAISED,bg="lightblue",command=self.sc2).place(x=570,y=300)
        





######### Generate

class generate:
    def __init__(self):
        self.frame3=LabelFrame(root,relief=GROOVE,labelanchor=N,bg="blue",bd=5,fg="white",pady=15)
        self.frame3.place(x=710,y=500,width=560)

        Label(self.frame3,text='Total:',font=('helvetica',12),height=1,relief=RAISED,width=10).grid(row=0,column=0,padx=20,pady=5)
        total=Entry(self.frame3,relief=GROOVE,bd=2,)
        total.grid(row=0,column=1,ipady=2,pady=5,sticky=W)
        total.insert(0,"0.0")
        Label(self.frame3,text='Discount(%):',font=('helvetica',12),height=1,relief=RAISED,width=10).grid(row=1,column=0,padx=20,pady=5)
        discount=Entry(self.frame3,relief=GROOVE,bd=2,)
        discount.grid(row=1,column=1,ipady=2,pady=5,sticky=W)
        discount.insert(0,"NA")
        Label(self.frame3,text='Grand Total:',font=('helvetica',12),height=1,relief=RAISED,width=10).grid(row=2,column=0,padx=20,pady=5)
        grand_total=Entry(self.frame3,relief=GROOVE,bd=2,)
        grand_total.grid(row=2,column=1,ipady=2,pady=5,sticky=W)
        grand_total.insert(0,"0.0")
        Button(self.frame3,text=' Reset ',relief=RAISED,font=20).grid(row=1,column=2,padx=30)
        Button(self.frame3,text=' Generate ',relief=RAISED,font=20).grid(row=1,column=3)






################Customer
class customer:
    def fetch_category_list(self):
        my_cursor.execute("select category from customer_category")
        category_list=my_cursor.fetchall()
        self.customer_category=Combobox(self.frame2)
        self.customer_category_options=[]
        for x in category_list:
            self.customer_category_options.append(x[0])
        self.customer_category['values']=self.customer_category_options
        self.customer_category.grid(row=3,column=1,sticky=W)
        self.customer_category.current(len(self.customer_category_options)-1)
    def add_customer(self):
        sql_command= "insert into customer(name,mobile,address,category,total_sales,age) values(%s,%s,%s,%s,%s,%s)"
        values=( self.name.get(),str(self.mobile.get()),self.address.get(),self.customer_category.get(),0,self.age.get())
       
        # try:
        my_cursor.execute(sql_command,values)
        # except:
                # messagebox.showerror("showerror","Some error occured")
        mydb.commit() 

    def __init__(self) :
        self.frame2=LabelFrame(root,text="Customer",padx=100,background="blue",fg="white",font=("Comic Sans MS", 20, "bold"),relief=GROOVE,bd=5)
        self.frame2.place(x=5,y=470,width=700)

        Label(self.frame2,text='Name:',font=('helvetica',12),height=1,relief=RAISED,width=10).grid(row=0,column=0,padx=20,pady=5)
        self.name=Entry(self.frame2,relief=GROOVE,bd=2,)
        self.name.grid(row=0,column=1,ipady=2,pady=5,sticky=W)
        self.name.insert(0,"NA")
        Label( self.frame2,text='Age:',font=('helvetica',12),height=1,relief=RAISED,width=5).grid(row=0,column=1,padx=20)
        self.age=Entry( self.frame2,relief=GROOVE,bd=2,width=5)
        self.age.grid(row=0,column=1,ipady=2,sticky=E)
        Label(self.frame2,text='Mobile:',font=('helvetica',12),height=1,relief=RAISED,width=10).grid(row=1,column=0,padx=20,pady=5)
        self.mobile=Entry(self.frame2,relief=GROOVE,bd=2,)
        self.mobile.grid(row=1,column=1,ipady=2,pady=5,sticky=W)
        self.mobile.insert(0,"NA")
        Label(self.frame2,text='Address:',font=('helvetica',12),height=1,relief=RAISED,width=10).grid(row=2,column=0,padx=20,pady=5)
        self.address=Entry(self.frame2,relief=GROOVE,bd=2,width=50)
        self.address.grid(row=2,column=1,ipady=2,pady=5,sticky=W)
        self.address.insert(0,"NA")
        Label(self.frame2,text='Category:',font=('helvetica',12),height=1,relief=RAISED,width=10).grid(row=3,column=0,padx=20,pady=5)
        self.fetch_category_list()
        






title_frame=title()
billing_frame=Entry_frame()
generate_frame=generate()
customer_frame=customer()
execute1=execute()

# print(bill_frame.text_area.get("1.0",END))

root=mainloop()