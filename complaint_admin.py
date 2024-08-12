from itertools import count
import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
mycon = mysql.connect(host='localhost',user='root',passwd='Dhruv471__01',database='hotel_management')
mycursor = mycon.cursor()
mycursor.execute('select * from complaint;')
complaint_data = mycursor.fetchall()

def complaint():
    root = tk.Tk()
    root.geometry('1000x720')
    root.title('COMPLAINT WINDOW')
    root.config(bg='#480BAB')
    root.resizable(False,False)
    query = tk.StringVar()
    mycursor.execute('select * from user_login;')
    user_data = mycursor.fetchone()

    def back():
        root.destroy()
        from admin_menu import admin_menu
        admin_menu()

    main_label = tk.Label(root,
                        text='COMPLAINT PORTAL',
                        font='ARIAL 35 bold underline',
                        bg='#480BAB',
                        fg='white').place(x=270, y=10)

    room_num_label = tk.Label(root,
                        text='ROOM NUMBER',
                        font='Calibri 25 bold',
                        bg='#480BAB',
                        fg='white').place(x=50, y=100)                    

    complaint_label = tk.Label(root,
                        text='COMPLAINT',
                        font='Calibri 25 bold',
                        bg='#480BAB',
                        fg='white').place(x=550, y=100)

    count = 0
    for i in range(len(complaint_data)):
        comp_1 = tk.Label(root, 
                        text=complaint_data[i][0],
                        font='calibri 20',
                        bg='#480BAB',
                        fg='white').place(x=120,y=150+count)

        comp_val = tk.Label(root, 
                        text=complaint_data[i][1],
                        font='calibri 20',
                        bg='#480BAB',
                        fg='white').place(x=500,y=150+count)
        count = 50

    back_button = tk.Button(root,
                        text='BACK',
                        font='ARIAL 10 bold',
                        bg='#361869',
                        fg='white',
                        command=lambda:back()).place(x=5, y=5)

    root.mainloop()