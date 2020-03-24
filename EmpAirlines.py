#Flight Management System
import tkinter as tk
from tkinter import *   
import mysql.connector

root = tk.Tk()
root.geometry('500x500')
root.title('EMP Airlines')

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="EMP_Airlines")


lbl = tk.Label(root, text='EMP Airlines', font=('bold', 30))
lbl.grid(row=0, column=0)

startBtn = tk.Button(root, text='START', width=10, font=('bold', 20), fg = 'blue')
startBtn.grid(row=1, column=0)
