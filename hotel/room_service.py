import tkinter as tk
import mysql.connector as mysql
from tkinter import messagebox
mycon = mysql.connect(host='localhost', user='root', passwd='dhruv_789_$1', database='hotel_management')
mycursor = mycon.cursor()


def room_service():
    root = tk.Tk()
    root.title('ROOM SERVICE')
    root.geometry('1000x480')
    root.config(bg='#480BAB')
    root.resizable(False, False)
    mycursor.execute('select * from user_login;')
    user_login = mycursor.fetchall()
    mycursor.execute('select room_num from reg_portal where guest_id = {};'.format(int(user_login[0][0][6:9])))
    room_number_ = mycursor.fetchone()
    room_number = room_number_[0]
    print(room_number)

    service_code = tk.StringVar()
    gid = int(user_login[0][0][6:9]) 

    def submit(code):
        serve_cost = 0 
        if code == 'W' or code == 'w':
            serve_cost = 50
        elif code == 'C' or code == 'c':
            serve_cost = 30
        elif code == 'J' or code == 'j':
            serve_cost = 30
        elif code == 'CL' or code == 'cl':
            serve_cost = 00
        mycursor.execute('insert into room_service values({},{},{},"{}")'.format(gid, room_number, serve_cost, service_code.get()))
        mycon.commit()
        messagebox.showinfo('SUBMITTED!','Your request has been submitted.')

    def back():
        root.destroy()
        from guest_menu import guest_menu

    main_label = tk.Label(root,
                        text='ROOM SERVICE',
                        font='ARIAL 30 bold underline',
                        bg='#480BAB',
                        fg='white').place(x=350, y=10)

    code_label = tk.Label(root,
                        text='Service Code',
                        font='Calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=130, y=100)

    service_label = tk.Label(root,
                        text='Service Name',
                        font='Calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=430, y=100)

    service_cost = tk.Label(root,
                        text='Service Cost',
                        font='Calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=730, y=100)

    _1label = tk.Label(root,
                    text='W',
                    font='Calibri 15',
                    bg='#480BAB',
                    fg='white').place(x=190, y=150)

    _2label = tk.Label(root,
                    text='C',
                    font='Calibri 15',
                    bg='#480BAB',
                    fg='white').place(x=190, y=200)

    _3label = tk.Label(root,
                    text='J',
                    font='Calibri 15',
                    bg='#480BAB',
                    fg='white').place(x=190, y=250)

    _4label = tk.Label(root,
                    text='CL',
                    font='Calibri 15',
                    bg='#480BAB',
                    fg='white').place(x=184, y=300)

    water_label = tk.Label(root,
                        text='WATER',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=475, y=150)

    tea_label = tk.Label(root,
                        text='TEA/COFFEE',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=460, y=200)

    juice_label = tk.Label(root,
                        text='JUICE',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=480, y=250)

    clean_label = tk.Label(root,
                        text='CLEANING',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=465, y=300)

    wcost_label = tk.Label(root,
                        text='50',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=785, y=150)

    tcost_label = tk.Label(root,
                        text='30',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=785, y=200)

    jcost_label = tk.Label(root,
                        text='30',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=785, y=250)

    ccost_label = tk.Label(root,
                        text='---',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=785, y=300)

    code_label = tk.Label(root,
                        text='Enter the code : ',
                        font='ARIAL 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=400, y=370)

    code_entry = tk.Entry(root,
                        textvariable=service_code,
                        font='calibri 15',
                        bg='#361869',
                        fg='white',
                        border=2).place(x=350, y=410, width=300, height=50)

    submit_button = tk.Button(root,
                        text='SUBMIT',
                        font='ARIAL 15 bold',
                        bg='#361869',
                        fg='white',
                        border=2,
                        command=lambda:submit(service_code.get())).place(x=651, y=410, height=50)

    back_button = tk.Button(root,
                        text='BACK',
                        font='ARIAL 10 bold',
                        bg='#361869',
                        fg='white',
                        command=lambda:back()).place(x=5, y=5)


    root.mainloop()

room_service()