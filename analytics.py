from os import kill
from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk, Image
import sqlite3
from tkcalendar import *
import mysql.connector
import pyzbar.pyzbar as pyzbar
import cv2
import qr
from tkinter.ttk import Combobox
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




root=Tk()
# root.wm_state('zoomed')
root.geometry("1920x1080")
# root.configure(bg="grey")

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



class Region_wise:
    def fetch_data(self):
        my_cursor.execute("select region,sum(total_sales) from mystore1.customer group by region;")
        customer_list=my_cursor.fetchall()
        total_sales_list=[]
        region_labels=[]
        for x in customer_list:
            # print(x[1])
            total_sales_list.append(x[1])
            region_labels.append(x[0])

        # print(labels)
        fig=plt.figure(figsize=(6,4),dpi=100)
        
        plt.pie(total_sales_list,labels=region_labels)       
        # plt.show() 
        plt.axis("equal")
        plt.legend()
        Canvas1=FigureCanvasTkAgg(fig,master=self.frame1)
        Canvas1.draw()
        Canvas1.get_tk_widget().pack()
    def __init__(self):
        self.frame1=LabelFrame(root,text="Region Wise",fg="black",bg="white",font=("Comic Sans MS", 10, "bold"),relief=GROOVE,labelanchor=N,bd=5)
        self.frame1.place(x=10,y=90)
        self.fetch_data()

class Age_Distribution:
    def fetch_data(self):
        my_cursor.execute("select age from mystore1.customer;")
        customer_list=my_cursor.fetchall()
        age_list=[]
        for x in customer_list:
            # print(x[1])
            age_list.append(x[0])

        # print(age_list)
        fig=plt.figure(figsize=(6,4),dpi=100)
        plt.hist(age_list)
        Canvas1=FigureCanvasTkAgg(fig,master=self.frame1)
        Canvas1.draw()
        Canvas1.get_tk_widget().pack()

    def __init__(self):
        self.frame1=LabelFrame(root,text="Age Distribution",fg="black",bg="white",font=("Comic Sans MS", 10, "bold"),relief=GROOVE,labelanchor=N,bd=5)
        self.frame1.place(x=650,y=90)
        self.fetch_data()

class Age_by_sales:
    def fetch_data(self):
        my_cursor.execute(" SELECT age,sum(total_sales) FROM mystore1.customer group by age;")
        customer_list=my_cursor.fetchall()
        age_list=[]
        sales=[]
        for x in customer_list:
            # print(x[1])
            age_list.append(x[0])
            sales.append(x[1])


        # print(age_list)
        # print(sales)

        fig=plt.figure(figsize=(6,4),dpi=100)
        plt.scatter(age_list,sales)
        Canvas1=FigureCanvasTkAgg(fig,master=self.frame1)
        Canvas1.draw()
        Canvas1.get_tk_widget().pack()

    def __init__(self):
        self.frame1=LabelFrame(root,text="Age by Total Sales",fg="black",bg="white",font=("Comic Sans MS", 10, "bold"),relief=GROOVE,labelanchor=N,bd=5)
        self.frame1.place(x=1300,y=90)
        self.fetch_data()
class Age_by_purchaseCount:
    def fetch_data(self):
        my_cursor.execute(" select age,count(age) from mystore1.customer group by age;")
        customer_list=my_cursor.fetchall()
        age_list=[]
        purchaseCount=[]
        for x in customer_list:
            # print(x[1])
            age_list.append(x[0])
            purchaseCount.append(x[1])


        # print(age_list)
        # print(sales)

        fig=plt.figure(figsize=(17,4),dpi=100)
        plt.scatter(age_list,purchaseCount)
        Canvas1=FigureCanvasTkAgg(fig,master=self.frame1)
        Canvas1.draw()
        Canvas1.get_tk_widget().pack()

    def __init__(self):
        self.frame1=LabelFrame(root,text="Age by Total Sales",fg="black",bg="white",font=("Comic Sans MS", 10, "bold"),relief=GROOVE,labelanchor=N,bd=5)
        self.frame1.place(x=120,y=550)
        self.fetch_data()



def on_closing():
    # if messagebox.askokcancel("Quit", "Do you want to quit?"):
    root.quit()


title_frame=title()
region_frame=Region_wise()
age_frame=Age_Distribution()
age_by_sales_frame=Age_by_sales()
age_by_purchase=Age_by_purchaseCount()



root.protocol("WM_DELETE_WINDOW", on_closing)


# print(bill_frame.text_area.get("1.0",END))


















































root=mainloop()