import tkinter as tk
import mysql.connector as mysql
import random
mycon = mysql.connect(host='localhost', user='root', passwd='dhruv_789_$1', database='hotel_management')
mycursor = mycon.cursor()
mycursor.execute('select guest_id, room_num from reg_portal;')
reg_data = mycursor.fetchall()
mycursor.execute('select * from guest_login where username = "{}";'.format('guest_'+str(reg_data[0][0])))
guest_data = mycursor.fetchone()

def display():
    root1 = tk.Tk()
    root1.geometry('1000x520')
    root1.title('Password Manager')
    root1.config(bg='#480BAB')
    root1.resizable(False, False)

    create_label = tk.Label(root1,
                        text='Congratulations! Registration Successful!',
                        font='ARIAL 30 bold underline',
                        bg='#480BAB',
                        fg='white').place(x=120, y=70)

    user_label = tk.Label(root1,
                        text='Username                 :',
                        font='Arial 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=250, y=170)

    passwd_label = tk.Label(root1,
                        text='Password                  :',
                        font='Arial 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=250, y=220)

    room_num_label = tk.Label(root1,
                            text='Room Number          :',
                            font='Arial 20 bold',
                            bg='#480BAB',
                            fg='white').place(x=250, y=270)

    user_label = tk.Label(root1,
                        text=guest_data[0][0],
                        font='Arial 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=650, y=170)    

    passwd_label = tk.Label(root1,
                        text=guest_data[0][1],
                        font='Arial 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=650, y=220)

    room_num_label = tk.Label(root1,
                            text=reg_data[0][1],
                            font='Arial 20 bold',
                            bg='#480BAB',
                            fg='white').place(x=650, y=270)

    root1.mainloop()
display()