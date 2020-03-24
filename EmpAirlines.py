#Flight Management System
import tkinter as tk
from tkinter import *   
import mysql.connector
from tkinter import messagebox 

root = tk.Tk()
root.geometry('500x130')
root.title('EMP Airlines - Start Page')

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="EMP_Airlines")


def FlightForm():

	def ShowStart():
		dstntn.withdraw()
		root.update()
		root.deiconify()

	def CreateFlight():
	
		flyingFrom 		= entryFrom.get()
		flyingTo 		= entryTo.get()
		departingOn 	= entryDepOn.get()
		returningOn 	= entryRetOn.get()
		departureTime	= entryDepTime.get()
		returningTime 	= entryRetTime.get()

		fullName 			= entryName.get()
		email 				= entryEmail.get()
		phone 				= entryPhone.get()
		nationality 		= entryNtnlty.get()
		gender 				= entryGndr.get()
		passportNo 			= entryPsprt.get()
		passportExpiryDate 	= entryPsprtExp.get()

		cursor = connection.cursor()
		mysql_insert_query = "INSERT INTO flightForm VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

		recordUser = (flyingTo,flyingTo,departingOn,returningOn,departureTime,returningTime,fullName,email,phone,nationality,gender,passportNo,passportExpiryDate)
		cursor.execute(mysql_insert_query, recordUser)
		connection.commit()
		messagebox.showinfo('Flight has been created successfully!')
		#print('Flight Successfully Created...')
		#ClearFields()

	root.withdraw()
	dstntn = tk.Toplevel(root)
	dstntn.geometry('800x500')
	dstntn.title('EMP Airlines - Flight Form')

	frame = LabelFrame(dstntn, text='Choose a Destination')
	frame.grid(row=0, column=1, padx=20, pady=20)

	lblFrom = Label(frame, text='Flying From :', font=('bold', 15))
	lblFrom.grid(row=1, column=0)
	entryFrom = Entry(frame)
	entryFrom.grid(row=1, column=1, pady=10)

	lblTo = Label(frame, text='Flying To :', font=('bold', 15))
	lblTo.grid(row=2, column=0)
	entryTo = Entry(frame)
	entryTo.grid(row=2, column=1, pady=10)

	lblDepOn = Label(frame, text='Departing On :', font=('bold', 15))
	lblDepOn.grid(row=3, column=0)
	entryDepOn = Entry(frame)
	entryDepOn.grid(row=3, column=1, pady=10)

	lblRetOn = Label(frame, text='Returning On :', font=('bold', 15))
	lblRetOn.grid(row=4, column=0)
	entryRetOn = Entry(frame)
	entryRetOn.grid(row=4, column=1, pady=10)

	lblDepTime = Label(frame, text='Departure Time :', font=('bold', 15))
	lblDepTime.grid(row=5, column=0)
	entryDepTime = Entry(frame)
	entryDepTime.grid(row=5, column=1, pady=10)

	lblRetTime = Label(frame, text='Returning Time :', font=('bold', 15))
	lblRetTime.grid(row=6, column=0)
	entryRetTime = Entry(frame)
	entryRetTime.grid(row=6, column=1, pady=10)


	frame1 = LabelFrame(dstntn, text='Personal Information')
	frame1.grid(row=0, column=2, padx=20, pady=20)

	lblName = Label(frame1, text='Full Name :', font=('bold', 15))
	lblName.grid(row=1, column=2)
	entryName = Entry(frame1)
	entryName.grid(row=1, column=3, pady=10)

	lblEmail = Label(frame1, text='Email :', font=('bold', 15))
	lblEmail.grid(row=2, column=2)
	entryEmail = Entry(frame1)
	entryEmail.grid(row=2, column=3, pady=10)

	lblPhone = Label(frame1, text='Phone No. :', font=('bold', 15))
	lblPhone.grid(row=3, column=2)
	entryPhone = Entry(frame1)
	entryPhone.grid(row=3, column=3, pady=10)

	lblNtnlty = Label(frame1, text='Nationality :', font=('bold', 15))
	lblNtnlty.grid(row=4, column=2)
	entryNtnlty = Entry(frame1)
	entryNtnlty.grid(row=4, column=3, pady=10)

	lblGndr = Label(frame1, text='Gender :', font=('bold', 15))
	lblGndr.grid(row=5, column=2)
	entryGndr = Entry(frame1)
	entryGndr.grid(row=5, column=3, pady=10)

	lblPsprt = Label(frame1, text='Passport No. :', font=('bold', 15))
	lblPsprt.grid(row=6, column=2)
	entryPsprt = Entry(frame1)
	entryPsprt.grid(row=6, column=3, pady=10)

	lblPsprtExp = Label(frame1, text='Passport Expiry Date :', font=('bold', 15))
	lblPsprtExp.grid(row=7, column=2)
	entryPsprtExp = Entry(frame1)
	entryPsprtExp.grid(row=7, column=3, pady=10)

	createBtn = Button(dstntn, text='Create Flight', width=20, font=('bold', 20), fg='blue', command=CreateFlight)
	createBtn.grid(row=8, column=1, columnspan=5, pady=15)







#StartPage
lbl = tk.Label(root, text='EMP AIRLINES', font=('bold', 30))
lbl.grid(row=0, column=0, padx=150, pady=10)

startBtn = tk.Button(root, text='START', width=10, font=('bold', 16), fg = 'blue', command=FlightForm)
startBtn.grid(row=1, column=0)



