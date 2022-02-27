import tkinter as tk
import mysql.connector as mysql
mycon = mysql.connect(host='localhost', user='root', passwd='dhruv_789_$1',database='hotel_management')
mycursor = mycon.cursor()
try:
    mycursor.execute('delete from user_login')
except:
    pass
global root

def admin_click():  #to be performed on admin button click
    global root
    root.destroy()
    from admin_login import admin_login #calling admin_login function from admin_login.py

def guest_click():  #to be performed on guest button click
    global root
    root.destroy()
    from guest_login import guest_login #calling guest_login function from guest_login.py


def homepage():   #main homepage
    global root
    root = tk.Tk()
    root.geometry('1000x720')
    root.config(bg='#480BA8')
    root.title('HOME PAGE')
    root.resizable(False,False)

    oak_label = tk.Label(root, 
                    text='OAK HOTEL', 
                    font='pacifico 100 underline', 
                    fg='white', 
                    bg='#480BA8').place(x=10, y=10, width=1000)

    button_emp = tk.Button(root,
                        text = 'Admin Login', 
                        font='helvectica 20',
                        fg='white', 
                        bg='#361869',
                        borderwidth=5,
                        command=lambda:admin_click()).place(x=250, y=450, width=200, height=70)

    or_label = tk.Label(root, 
                        text = 'OR',
                        font='Arial 15 bold', 
                        bg='#480BA8', 
                        fg='white').place(x=450, y=450, width=100, height=70)

    button_guest = tk.Button(root, 
                        text='Guest Login', 
                        fg='white',
                        bg='#361869',
                        font='helvectica 20',
                        borderwidth=5,
                        command=lambda:guest_click()).place(x=550, y=450, width=200, height=70)

    root.mainloop()
homepage()
