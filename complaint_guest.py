import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
mycon = mysql.connect(host='localhost',user='root',passwd='Dhruv471__01',database='hotel_management')
mycursor = mycon.cursor()

def complaint():
    root = tk.Tk()
    root.geometry('1000x720')
    root.title('COMPLAINT WINDOW')
    root.config(bg='#480BAB')
    root.resizable(False,False)
    query = tk.StringVar()
    mycursor.execute('select * from user_login;')
    user_data = mycursor.fetchone()

    def submit():
        mycursor.execute('insert into complaint values({},"{}")'.format(user_data[1],query.get()))
        mycon.commit()
        messagebox.showinfo('Showinfo','Complaint has been submitted!')
        root.destroy()
        from guest_menu import guest_menu
        guest_menu()

    def back():
        root.destroy()
        from guest_menu import guest_menu
        guest_menu()

    main_label = tk.Label(root,
                        text='COMPLAINT PORTAL',
                        font='ARIAL 35 bold underline',
                        bg='#480BAB',
                        fg='white').place(x=270, y=10)

    query_label = tk.Label(root,
                        text='Enter your complaint',
                        font='calibri 15 bold',
                        bg='#480BAB',
                        fg='white').place(x=50, y=150)

    query_entry = tk.Entry(root,
                        text=query,
                        font='calibri 15',
                        bg='#361869',
                        fg='white').place(x=50, y=200, width=900, height=50)

    submit_button = tk.Button(root,
                            text='SUBMIT',
                            font='ARIAL 15 bold',
                            bg='#361869',
                            fg='white',
                            command=lambda:submit()).place(x=480, y=255)

    back_button = tk.Button(root,
                        text='BACK',
                        font='ARIAL 10 bold',
                        bg='#361869',
                        fg='white',
                        command=lambda:back()).place(x=5, y=5)

    root.mainloop()