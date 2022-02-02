import random
import ticket_gen
import exit_check
from tkinter import *
import tkinter.messagebox
# import db
from datetime import datetime
from datetime import date


#=========================================#
#=========================================#


class pms:
    def __init__(self, root):
        self.root = root
        self.root.title("Parking Management System")
        self.root.geometry("1040x460+0+0")
        self.root.config(bg="SteelBlue1")

        carId = StringVar()
        carCompany = StringVar()
        carPlate = StringVar()
        #entr_time = StringVar()

        
# =========================================# functions

        def genticket():
            # car_hash = "MH01AE8017"
            if(len(carPlate.get()) != 0):
                f = ticket_gen.ticket_gen(carPlate.get())
                info.delete(0, END)
                info.insert(END,  ("Plate: "+str(carPlate.get()).upper()),
                            ("Brand: "+str(carCompany.get()).upper()), ("ID: "+str(f)))
            else:
                pass

        def checkticket():

            if(len(carId.get()) != 0):
                # print(carPlate.get())
                f = exit_check.chexit(carId.get(), carPlate.get())
                info.delete(0, END)
                info.insert(END, carId.get(), ("INR: "+str(f)+"/-"), str(" "))

            else:
                pass

        def clearEnt():
            self.txtcarID.delete(0, END)
            self.txtcarp.delete(0, END)
            self.txtmodel.delete(0, END)

        # def display():

        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Parking Management System", "Are you sure you want to Exit?")
            if iExit > 0:
                root.destroy()
                return

        #=========================================#
        

        MainFrame = Frame(self.root, bg="SteelBlue3")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2, padx=54,
                           pady=8, bg="gray20", relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTit = Label(TitleFrame, font=(
            'serif', 47, 'bold'), text="Parking Management System", bg="gray20", fg="white")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1250, height=70,
                            padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1100, height=500,
                          padx=20, pady=10, relief=RIDGE, bg="SteelBlue1")
        DataFrame.pack(side=BOTTOM)

        DataFrameL = LabelFrame(DataFrame, bd=1, width=800, height=400,
                                padx=20, pady=20, relief=RIDGE, bg="Ghost White", font=('serif', 25, 'bold'), text="Parking Ticket Info\n")
        DataFrameL.pack(side=LEFT)

        DataFrameR = LabelFrame(DataFrame, bd=1, width=450, height=140,
                                padx=6, pady=6, relief=RIDGE, bg="Ghost White", font=('serif', 25, 'bold'), text="Car Details\n")
        DataFrameR.pack(side=RIGHT)

        # =========================================# LABELS + ENTRY
        self.lblcarID = Label(DataFrameL, font=(
            'serif', 20, 'bold'), text="Ticket ID ", padx=2, pady=5, bg="Ghost White")
        self.lblcarID.grid(row=0, column=0, sticky=W)
        self.txtcarID = Entry(DataFrameL, font=(
            'serif', 20, 'bold'), textvariable=carId, width=30)
        self.txtcarID.grid(row=0, column=1, sticky=W)

        self.lblcarp = Label(DataFrameL, font=(
            'serif', 20, 'bold'), text="Plate Number ", padx=2, pady=5, bg="Ghost White")
        self.lblcarp.grid(row=1, column=0, sticky=W)
        self.txtcarp = Entry(DataFrameL, font=(
            'serif', 20, 'bold'), textvariable=carPlate, width=30)
        self.txtcarp.grid(row=1, column=1, sticky=W)

        self.lblmodel = Label(DataFrameL, font=(
            'serif', 20, 'bold'), text="Car Brand ", padx=2, pady=4, bg="Ghost White")
        self.lblmodel.grid(row=2, column=0, sticky=W)
        self.txtmodel = Entry(DataFrameL, font=(
            'serif', 20, 'bold'), textvariable=carCompany, width=30)
        self.txtmodel.grid(row=2, column=1, sticky=W)

        # =========================================# R box

        info = Listbox(DataFrameR, width=31, height=8,
                       font=('serif', 12, 'bold'))
        info.grid(row=0, column=0, padx=5)

        # =========================================# BUTTONS

        self.btngen = Button(ButtonFrame, text="Create", font=(
            'serif', 20, 'bold'), height=1, width=10, bd=4, command=genticket)
        self.btngen.grid(row=0, column=0)
        self.btnchk = Button(ButtonFrame, text="Check", font=(
            'serif', 20, 'bold'), height=1, width=10, bd=4, command=checkticket)
        self.btnchk.grid(row=0, column=1)
        self.btnclr = Button(ButtonFrame, text="Clear", font=(
            'serif', 20, 'bold'), height=1, width=10, bd=4, command=clearEnt)
        self.btnclr.grid(row=0, column=2)
        self.btnex = Button(ButtonFrame, text="Exit", font=(
            'serif', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnex.grid(row=0, column=3)
    
    
        #=========================================#
        #=========================================#

if __name__ == '__main__':
    root = Tk()
    application = pms(root)
    root.mainloop()
