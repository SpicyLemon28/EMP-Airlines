#Flight Management System
import tkinter as tk
from tkinter import *   
import mysql.connector
from tkinter import messagebox 

root = tk.Tk()
root.geometry('500x400')
root.title('EMP Airlines - Start Page')

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Airlines")


def FlightForm():

	def ShowStart():
		flight.withdraw()
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
		ClearFields()
		messagebox.showinfo('EMP Airlines', 'Flight has been created successfully!')

	def ClearFields():
		entryFrom.delete(0,END)
		entryTo.delete(0,END)
		entryDepOn.delete(0,END)
		entryRetOn.delete(0,END)
		entryDepTime.delete(0,END)
		entryRetTime.delete(0,END)
		entryName.delete(0,END)
		entryEmail.delete(0,END)
		entryPhone.delete(0,END)
		entryNtnlty.delete(0,END)
		entryGndr.delete(0,END)
		entryPsprt.delete(0,END)
		entryPsprtExp.delete(0,END)


	root.withdraw()
	flight = tk.Toplevel(root)
	flight.geometry('1000x500')
	flight.title('EMP Airlines - Flight Form')

	bckBtn = Button(flight, text='Back', width=10, fg='orange', font=('bold', 15), command=ShowStart)
	bckBtn.grid(row=0,column=0, padx=3, pady=5)

	frame = LabelFrame(flight, text='Choose a Destination')
	frame.grid(row=1, column=1, padx=20, pady=20)

	lblFrom = Label(frame, text='Flying From :', font=('bold', 15))
	lblFrom.grid(row=2, column=0)
	entryFrom = Entry(frame)
	entryFrom.grid(row=2, column=1, pady=10)

	lblTo = Label(frame, text='Flying To :', font=('bold', 15))
	lblTo.grid(row=3, column=0)
	entryTo = Entry(frame)
	entryTo.grid(row=3, column=1, pady=10)

	lblDepOn = Label(frame, text='Departing On :', font=('bold', 15))
	lblDepOn.grid(row=4, column=0)
	entryDepOn = Entry(frame)
	entryDepOn.grid(row=4, column=1, pady=10)

	lblRetOn = Label(frame, text='Returning On :', font=('bold', 15))
	lblRetOn.grid(row=5, column=0)
	entryRetOn = Entry(frame)
	entryRetOn.grid(row=5, column=1, pady=10)

	lblDepTime = Label(frame, text='Departure Time :', font=('bold', 15))
	lblDepTime.grid(row=6, column=0)
	entryDepTime = Entry(frame)
	entryDepTime.grid(row=6, column=1, pady=10)

	lblRetTime = Label(frame, text='Returning Time :', font=('bold', 15))
	lblRetTime.grid(row=7, column=0)
	entryRetTime = Entry(frame)
	entryRetTime.grid(row=7, column=1, pady=10)


	frame1 = LabelFrame(flight, text='Personal Information')
	frame1.grid(row=1, column=2, padx=20, pady=20)

	lblName = Label(frame1, text='Full Name :', font=('bold', 15))
	lblName.grid(row=2, column=2)
	entryName = Entry(frame1)
	entryName.grid(row=2, column=3, pady=10)

	lblEmail = Label(frame1, text='Email :', font=('bold', 15))
	lblEmail.grid(row=3, column=2)
	entryEmail = Entry(frame1)
	entryEmail.grid(row=3, column=3, pady=10)

	lblPhone = Label(frame1, text='Phone No. :', font=('bold', 15))
	lblPhone.grid(row=4, column=2)
	entryPhone = Entry(frame1)
	entryPhone.grid(row=4, column=3, pady=10)

	lblNtnlty = Label(frame1, text='Nationality :', font=('bold', 15))
	lblNtnlty.grid(row=5, column=2)
	entryNtnlty = Entry(frame1)
	entryNtnlty.grid(row=5, column=3, pady=10)

	lblGndr = Label(frame1, text='Gender :', font=('bold', 15))
	lblGndr.grid(row=6, column=2)
	entryGndr = Entry(frame1)
	entryGndr.grid(row=6, column=3, pady=10)

	lblPsprt = Label(frame1, text='Passport No. :', font=('bold', 15))
	lblPsprt.grid(row=7, column=2)
	entryPsprt = Entry(frame1)
	entryPsprt.grid(row=7, column=3, pady=10)

	lblPsprtExp = Label(frame1, text='Passport Expiry Date :', font=('bold', 15))
	lblPsprtExp.grid(row=8, column=2)
	entryPsprtExp = Entry(frame1)
	entryPsprtExp.grid(row=8, column=3, pady=10)

	createBtn = Button(flight, text='Create Flight', width=40, font=('bold', 20), fg='blue', command=CreateFlight)
	createBtn.grid(row=9, column=1, columnspan=5, pady=15)

#Sign In
def Admin():
	lblTitle = Label(root, text='Sign in to show list of flights', font=('bold', 14))
	lblTitle.grid(row=3, column=0)
	frame3 = LabelFrame(root, text='Admin')
	frame3.grid(row=4, column=0)

	lblUname = Label(frame3, text='Username :', font=('bold', 12))
	lblUname.grid(row=4, column=0)
	entryUname = Entry(frame3)
	entryUname.grid(row=4, column=1)
	entryUname.insert(0, 'admin')

	lblPass = Label(frame3, text='Password :', font=('bold', 12))
	lblPass.grid(row=5, column=0)
	entryPass = Entry(frame3, show='*')
	entryPass.grid(row=5, column=1, pady=5)
	entryPass.insert(0, 'admin.admin')

	signInBtn = Button(frame3, width=10,text='Sign In', fg='orange', font=('bold', 12), command=FlightList)
	signInBtn.grid(row=6, column=1)

#Show List of Flights
def FlightList():
	root.withdraw()
	flightlist = tk.Toplevel(root)
	flightlist.geometry('1500x500')
	flightlist.title('List of Flights')

	cursor = connection.cursor()
	mysql_select_query = "SELECT flyingFrom, flyingTo, departingOn, returningOn, departureTime, returningTime, fullName, email, phone, nationality, gender, passportNo, passportExpiryDate FROM flightForm"
	cursor.execute(mysql_select_query)
	result = cursor.fetchall()
	cursor.close()
	space=50

	lblFlyingFrom = Label(flightlist, text='Flying\nFrom', font=('bold', 15))
	lblFlyingFrom.grid(row=0, column=0)
	lblFlyingTo = Label(flightlist, text='Flying\nTo', font=('bold', 15))
	lblFlyingTo.grid(row=0, column=1, padx=10)
	lblDepartingOn = Label(flightlist, text='Departing\nOn', font=('bold', 15))
	lblDepartingOn.grid(row=0, column=2, padx=10)
	lblReturningOn = Label(flightlist, text='Returning\n On', font=('bold', 15))
	lblReturningOn.grid(row=0, column=3, padx=10)
	lblDepartureTime = Label(flightlist, text='Departure\nTime', font=('bold', 15))
	lblDepartureTime.grid(row=0, column=4, padx=10)
	lblReturningTime = Label(flightlist, text='Returning\nTime', font=('bold', 15))
	lblReturningTime.grid(row=0, column=5, padx=10)
	lblFullName = Label(flightlist, text='Full\nName', font=('bold', 15))
	lblFullName.grid(row=0, column=6, padx=20)
	lblEmail = Label(flightlist, text='Email', font=('bold', 15))
	lblEmail.grid(row=0, column=7, padx=10)
	lblPhone = Label(flightlist, text='Phone', font=('bold', 15))
	lblPhone.grid(row=0, column=8, padx=20)
	lblNationality = Label(flightlist, text='Nation-\nality', font=('bold', 15))
	lblNationality.grid(row=0, column=9, padx=10)
	lblGender = Label(flightlist, text='Gender', font=('bold', 15))
	lblGender.grid(row=0, column=10, padx=10)
	lblPassport = Label(flightlist, text='Passport\nNo', font=('bold', 15))
	lblPassport.grid(row=0, column=11, padx=10)
	lblPassportExp = Label(flightlist, text='Passport\nExpiry Date', font=('bold', 15))
	lblPassportExp.grid(row=0, column=12, padx=10)

	for a in result:
		flight_list = Label(flightlist, text=a[0], font=10)
		flight_list.grid(row=1, column=0)

		flight_list = Label(flightlist, text=a[1], font=10)
		flight_list.grid(row=1, column=1)

		flight_list = Label(flightlist, text=a[2], font=10)
		flight_list.grid(row=1, column=2)

		flight_list = Label(flightlist, text=a[3], font=10)
		flight_list.grid(row=1, column=3)

		flight_list = Label(flightlist, text=a[4], font=10)
		flight_list.grid(row=1, column=4)

		flight_list = Label(flightlist, text=a[5], font=10)
		flight_list.grid(row=1, column=5)

		flight_list = Label(flightlist, text=a[6], font=10)
		flight_list.grid(row=1, column=6)

		flight_list = Label(flightlist, text=a[7], font=10)
		flight_list.grid(row=1, column=7)

		flight_list = Label(flightlist, text=a[8], font=10)
		flight_list.grid(row=1, column=8)

		flight_list = Label(flightlist, text=a[9], font=10)
		flight_list.grid(row=1, column=9)

		flight_list = Label(flightlist, text=a[10], font=10)
		flight_list.grid(row=1, column=10)

		flight_list = Label(flightlist, text=a[11], font=10)
		flight_list.grid(row=1, column=11)

		flight_list = Label(flightlist, text=a[12], font=10)
		flight_list.grid(row=1, column=12)
		space = space + 50






#StartPage
lbl = tk.Label(root, text='EMP AIRLINES', font=('bold', 30))
lbl.grid(row=0, column=0, padx=150, pady=10)

startBtn = tk.Button(root, text='START', width=10, font=('bold', 16), fg = 'blue', command=FlightForm)
startBtn.grid(row=1, column=0, pady=10)

listBtn = tk.Button(root, text='Show List of Flights', width=20, font=('bold', 12), fg = 'green', command=Admin)
listBtn.grid(row=2, column=0, pady=10)



