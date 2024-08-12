import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
mycon = mysql.connect(host='localhost', user='root', passwd='Dhruv471__01', database='hotel_management')
mycursor = mycon.cursor()

def search_label():  #defining main search page function
    root = tk.Tk()
    root.geometry('1000x720')
    root.title('SEARCH RECORD')
    root.config(bg='#480BAB')
    root.resizable(False, False)
    code = tk.StringVar()

    def back():
        root.destroy()
        from admin_menu import admin_menu #calling admin_menu function from admin_menu.py
        admin_menu()

    def logout():
        root.destroy()
        from home_page import homepage #calling homepage function from home_page.py
        homepage()

    def search(): #checks for entered room code
        mycursor.execute('select * from reg_portal where room_num = {};'.format(int(code.get())))
        data_search = mycursor.fetchone()
        code_int = int(code.get())

        try:
            if code_int == data_search[7]:  #matching room code
                name_label = tk.Label(root,
                                text=data_search[1]+' '+data_search[2],
                                font='calibri 20 bold ',
                                bg='#480BAB',
                                fg='white').place(x=480, y=250)

                pno_label = tk.Label(root,
                                text=data_search[3],
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=480, y=300)

                address_label = tk.Label(root,  
                                    text=data_search[4],
                                    font='calibri 20 bold',
                                    bg='#480BAB',
                                    fg='white').place(x=480, y=350)

                nights_label = tk.Label(root,
                                    text=data_search[6],
                                    font='calibri 20 bold',
                                    bg='#480BAB',
                                    fg='white').place(x=480, y=450)

                members_label = tk.Label(root,
                                    text=data_search[5],
                                    font='calibri 20 bold',
                                    bg='#480BAB',
                                    fg='white').place(x=480, y=400)

                room_no_label = tk.Label(root,
                                    text=data_search[7],
                                    font='calibri 20 bold',
                                    bg='#480BAB',
                                    fg='white').place(x=480, y=500)
        except:
            name_label = tk.Label(root,
                            text='                                              ',
                            font='calibri 20 bold ',
                            bg='#480BAB',
                            fg='white').place(x=480, y=250)

            pno_label = tk.Label(root,
                            text='                                     ',
                            font='calibri 20 bold',
                            bg='#480BAB',
                            fg='white').place(x=480, y=300)

            address_label = tk.Label(root,  
                                text='                              ',
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=480, y=350)

            nights_label = tk.Label(root,
                                text='                                ',
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=480, y=450)

            members_label = tk.Label(root,
                                text='                                      ',
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=480, y=400)

            room_no_label = tk.Label(root,
                                text='                                      ',
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=480, y=500)
            messagebox.showinfo('SHOWINFO','Entered Room Number is not occupied!')

    main_label = tk.Label(root, 
                        text='SEARCH RECORD',
                        font='ARIAL 40 bold underline',
                        bg='#480BAB',
                        fg='white').place(x=260, y=10)

    entry_label = tk.Label(root,
                        text='Enter Room Code : ',
                        font='ARIAL 15 bold',
                        bg='#480BAB',
                        fg='white').place(x=370, y=130)

    code_entry = tk.Entry(root,
                        textvariable=code,
                        font='calibri 15',
                        bg='#361869',
                        fg='white',
                        border=4).place(x=340, y=170, width=200, height=50)

    submit = tk.Button(root,
                    text='SEARCH',
                    font='ARIAL 15 bold',
                    bg='#361869',
                    fg='white',
                    border=5,
                    command=lambda:search()).place(x=542, y=170, height=50)

    name_label = tk.Label(root,
                        text='Name                                     :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=250)

    pno_label = tk.Label(root,
                        text='Phone Number                    :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=300)

    address_label = tk.Label(root,  
                        text='Address                                 :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=350)

    nights_label = tk.Label(root,
                        text='Number of Nights               :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=450)

    members_label = tk.Label(root,
                        text='Number of Members         :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=400)

    room_no_label = tk.Label(root,
                        text='Room number                      :',
                        font='calibri 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=80, y=500)

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