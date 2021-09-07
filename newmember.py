from tkinter import *
from tkinter import messagebox
import sqlite3
con = sqlite3.connect("lms.db")
cur = con.cursor()

class StoreMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("800x800")
        self.title("Add Member")
        self.resizable(False,False)

        self.top_frame = Frame(self, height=150, bg='grey')
        self.top_frame.pack(fill=X)
        heading = Label(self.top_frame, text="Add New member", font='arial 18 bold', bg='grey', fg='white')
        heading.place(x=300, y=60)
        self.bodyframe = Frame(self, height=650, bg='white')
        self.bodyframe.pack(fill=X)

        self.lbl_author = Label(self.bodyframe, text="Enter Member Name:", font='arial 12 bold', bg='white')
        self.lbl_author.place(x=40, y=80)
        self.txt_member_name = Entry(self.bodyframe, width=30, bd=2)
        self.txt_member_name.place(x=200, y=80)

        self.lbl_pages = Label(self.bodyframe, text="Enter Phone no:", font='arial 12 bold', bg='white')
        self.lbl_pages.place(x=40, y=120)
        self.txt_member_phone_no = Entry(self.bodyframe, width=30, bd=2)
        self.txt_member_phone_no.place(x=200, y=120)

        savebutton = Button(self.bodyframe, text="Save Now", command=self.savemember)
        savebutton.place(x=300, y=170)

    def savemember(self):
        name = self.txt_member_name.get()
        phone = self.txt_member_phone_no.get()

        if(name and phone != ""):
            try:
                query = "INSERT INTO 'Members'(Member_name, Member_phone_no)VALUES(?,?)"
                cur.execute(query,(name,phone))
                con.commit()
                messagebox.showinfo("Success","Member details has been save sucessfully",icon='info')
            except:
                messagebox.showerror("Error","Transaction not commit",icon='warning')
        else:
            messagebox.showerror("Error","All fields are mandatory",icon='warning')