import tkinter as tk
from tkinter import messagebox,ttk
import pandas as pd
import sqlite3
import sqlite_engine as sg
from threading import Thread
import sqlalchemy

root = tk.Tk()

appLabel = tk.Label(root, text="Web Scrapping")
appLabel.pack()

def loadData():
    ThreadTask("load").start()
    messagebox.showinfo("Success", "Values have been saved successfully.")
def showData():
    ThreadTask("show").start()
    # messagebox.showinfo("showing", "you are going to watch the data loaded")

class ThreadTask(Thread):

    def __init__(self, value):
        Thread.__init__(self)
        self.value=value

    def run(self):
        connection = sg.connection_start()
        if (self.value == "load"):
            data = pd.read_csv('book.csv')
            data=data.set_index("BOOK_ID")
            data.to_sql("WebScrapTable", connection, if_exists='append')
            print("Data inserted successfully.")
        else:
            cursor=sg.read_data()
            createNewFrame(cursor)

def createNewFrame(data):
    displaywindow=tk.Tk()
    displayHeading=tk.Label(displaywindow,text="displaying scraped data")
    displayHeading.pack()

    treeview=ttk.Treeview(displaywindow)
    treeview["columns"]=(1,2,3)
    treeview.heading(1,text="book name")
    treeview.heading(2,text="price")
    treeview.heading(3,text="availability")
    i=0
    for row in data:
        treeview.insert('',i,text=str(i+1) ,values=(row[1],row[2],row[3]))
        i=i+1
    treeview.pack()
    displaywindow.mainloop()



loadButton = tk.Button(root, text="Load data", command=lambda : loadData())
loadButton.pack()

showButton = tk.Button(root, text="Show data", command=lambda: showData())
showButton.pack()

root.mainloop()

