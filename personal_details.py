import tkinter as tk
import mysql.connector as mysql
from numpy import place
mycon = mysql.connect(host='localhost', user='root', passwd='dhruv_789_$1', database='hotel_management')
mycursor = mycon.cursor()

def personal_details():
    def logout():
        mycursor.execute('delete from user_login;')
        root.destroy()
        from home_page import homepage

    def back():
        root.destroy()
        from guest_menu import guest_menu

    
    mycursor.execute('select * from user_login')
    data = mycursor.fetchall()
    print(data)
    code = data[0][0]
    print(code)
    code_ = code[6:9]
    print(code_)
    int_code = int(code_)
    print(int_code)
    mycursor.execute('select * from reg_portal where guest_id = {};'.format(int_code))
    personal_data = mycursor.fetchall()
    print(personal_data)

    root = tk.Tk()
    root.title('PERSONAL DETAILS')
    root.config(bg='#480BAB')
    root.geometry('1000x720')
    root.resizable(False, False)

    main_label = tk.Label(root,
                        text='PERSONAL DETAILS',
                        font='ARIAL 40 bold underline',
                        bg='#480BAB',
                        fg='white').place(x=225, y=15)

    name_label = tk.Label(root,
                        text='Name                                     :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=150)

    pno_label = tk.Label(root,
                        text='Phone Number                    :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=200)

    address_label = tk.Label(root,  
                        text='Address                                 :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=250)

    nights_label = tk.Label(root,
                        text='Number of Nights               :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=350)

    members_label = tk.Label(root,
                        text='Number of Members         :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=300)

    room_no_label = tk.Label(root,
                        text='Room number                      :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=400)

    name_val = tk.Label(root,
                        text=personal_data[0][1]+' '+personal_data[0][2],
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=450, y=150)

    phone_val = tk.Label(root,  
                        text=personal_data[0][3],
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=450, y=200)

    add_val = tk.Label(root,
                    text=personal_data[0][4],
                    font='calibri 20 bold',
                    bg='#480BAB',
                    fg='white').place(x=450, y=250)

    mem_val = tk.Label(root,
                    text=personal_data[0][5],
                    font='calibri 20 bold',
                    bg='#480BAB',
                    fg='white').place(x=450, y=300)

    nights_val = tk.Label(root,
                    text=personal_data[0][6],
                    font='calibri 20 bold',
                    bg='#480BAB',
                    fg='white').place(x=450, y=350)

    room_val = tk.Label(root,
                    text=personal_data[0][7],
                    font='calibri 20 bold',
                    bg='#480BAB',
                    fg='white').place(x=450, y=400)

    back_button = tk.Button(root,
                        text='BACK',
                        font='ARIAL 15 bold',
                        bg='#361869',
                        fg='white',
                        command=lambda:back()).place(x=5, y=5)

    logout_button = tk.Button(root,
                        text='LOGOUT',
                        font='ARIAL 15 bold',
                        bg='#361869',
                        fg='white',
                        command=lambda:logout()).place(x=890, y=5)

    root.mainloop()

personal_details()
