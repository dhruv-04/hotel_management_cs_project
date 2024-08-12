import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
mycon = mysql.connect(host='localhost', user='root', passwd='Dhruv471__01',database='hotel_management')
mycursor = mycon.cursor()
mycursor.execute('select * from employee_login;')
admin_login_data = mycursor.fetchall()
global username

def admin_login():    #main function to call admin login page
    root_admin = tk.Tk()
    root_admin.geometry('1000x720')
    root_admin.config(bg='#480BA8')
    root_admin.title('ADMIN LOGIN PAGE')
    root_admin.resizable(False,False)
    global username
    def admin_check():    #checking for authorized admin access
        for i in range(len(admin_login_data)):
            if username.get() == admin_login_data[i][0]:   #checking for correct username
                if password.get() == admin_login_data[i][1]:    #checking for correct  password
                    messagebox.showinfo('SHOWINFO','LOGIN SUCCESSFUL!')  #if login is success
                    root_admin.destroy()
                    from admin_menu import admin_menu  #calling admin menu page function from admin_menu.py
                    admin_menu()
                else:
                    messagebox.showinfo('SHOWINFO','INVALID PASSWORD!')  #if password is invalid
            else:
                messagebox.showinfo('SHOWINFO','INVALID USERNAME!')  #if username is invalid

    def back():   #back to main homepage
        root_admin.destroy()
        from home_page import homepage  #calling homepage function from home_page.py
        homepage()
        

    username = tk.StringVar()
    password = tk.StringVar()

    admin_label = tk.Label(root_admin,
                        text='ADMIN LOGIN',
                        font='ARIAL 100 underline',
                        bg='#480BAB',
                        fg='white').place(x = 50, y=80)

    user_label = tk.Label(root_admin,
                        text='USERNAME',
                        font='ARIAL 18',
                        bg='#480BAB',
                        fg='white').place(x=250, y=439)

    pass_label = tk.Label(root_admin,
                        text='PASSWORD',
                        font='ARIAL 18',
                        bg='#480BAB',
                        fg='white',).place(x=250, y=509)

    user_entry = tk.Entry(root_admin,
                    textvariable=username,
                    font='calibri 15',
                    bg='#361869',
                    fg='white',
                    borderwidth=0,
                    border=5).place(x = 400, y=430, width=250, height=50)

    pass_entry = tk.Entry(root_admin,
                    textvariable=password,
                    font='calibri 15',
                    bg='#361869',
                    fg='white',
                    show='*',
                    border=5).place(x = 400, y=500, width=250, height=50)

    login_button = tk.Button(root_admin,
                        text='LOGIN',
                        font='calibri 15 bold',
                        bg='#361869',
                        fg='white',
                        border=2,
                        command=lambda:admin_check()).place(x=450, y=570, width=100, height=50)

    back_ = tk.Button(root_admin,
                    text='BACK',
                    font='calibri 10 bold',
                    bg='#361869',
                    fg='white',
                    border=2,
                    command=lambda:back()).place(x=5, y=5)
    root_admin.mainloop()

admin_login()