import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
mycon = mysql.connect(host='localhost', user='root', passwd='Dhruv471__01',database='hotel_management')
mycursor = mycon.cursor()
mycursor.execute('delete from user_login;')
mycon.commit()
mycursor.execute('select * from guest_login;')
guest_login_data = mycursor.fetchall()
print(guest_login_data)
global username
global password
root = tk.Tk()
root.geometry('1000x720')
root.config(bg='#480BA8')
root.title('GUEST LOGIN PAGE')
root.resizable(False,False)
username = tk.StringVar()
password = tk.StringVar()

def guest_login():
    global username
    global password
    def guest_check():
        count = 0
        for i in range(len(guest_login_data)):
            if username.get() == guest_login_data[i][0]:
                if password.get() == guest_login_data[i][1]:
                    mycursor.execute('insert into user_login values("{}",{})'.format(username.get(),guest_login_data[i][2]))
                    mycon.commit()
                    messagebox.showinfo('SHOWINFO','LOGIN SUCCESSFUL!')
                    root.destroy()
                    from guest_menu import guest_menu
                    guest_menu()
                else:
                    messagebox.showinfo('SHOWINFO','INVALID PASSWORD!')
            else:
                count = count + 1
                print(count)
                if count < len(guest_login_data):
                    pass
                else:
                    messagebox.showinfo('SHOWINFO','INVALID USERNAME!')


    def back():
        root.destroy()
        from home_page import homepage
        homepage()        

    admin_label = tk.Label(root,
                        text='GUEST LOGIN',
                        font='ARIAL 100 underline',
                        bg='#480BAB',
                        fg='white').place(x = 50, y=80)

    user_label = tk.Label(root,
                        text='USERNAME',
                        font='ARIAL 18',
                        bg='#480BAB',
                        fg='white').place(x=250, y=439)

    pass_label = tk.Label(root,
                        text='PASSWORD',
                        font='ARIAL 18',
                        bg='#480BAB',
                        fg='white',).place(x=250, y=509)

    user_entry = tk.Entry(root,
                    textvariable=username,
                    font='calibri 15',
                    bg='#361869',
                    fg='white',
                    borderwidth=0,
                    border=5).place(x = 400, y=430, width=250, height=50)

    pass_entry = tk.Entry(root,
                    textvariable=password,
                    font='calibri 15',
                    bg='#361869',
                    fg='white',
                    show='*',
                    border=5).place(x = 400, y=500, width=250, height=50)

    login_button = tk.Button(root,
                        text='LOGIN',
                        font='calibri 15 bold',
                        bg='#361869',
                        fg='white',
                        border=2,
                        command=lambda:guest_check()).place(x=450, y=570, width=100, height=50)

    back_ = tk.Button(root,
                    text='BACK',
                    font='calibri 10 bold',
                    bg='#361869',
                    fg='white',
                    border=2,
                    command=lambda:back()).place(x=5, y=5)

    root.mainloop()