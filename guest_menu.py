import tkinter as tk
import mysql.connector as mysql
mycon = mysql.connect(host='localhost', user='root', passwd='Dhruv471__01', database='hotel_management')
mycursor = mycon.cursor()

def guest_menu():
    root = tk.Tk()
    root.geometry('1000x720')
    root.title('GUEST HOME PAGE')
    root.resizable(False, False)
    root.config(bg='#480BAB')

    def personal_details_():
        root.destroy()
        from personal_details import personal_details
        personal_details()

    def roomservice():
        root.destroy()
        from room_service import room_service
        room_service()

    def logout():
        mycursor.execute('delete from user_login')
        mycon.commit()
        root.destroy()
        from home_page import homepage
        homepage()

    def complain():
        root.destroy()
        from complaint_guest import complaint
        complaint()

    main_label = tk.Label(root,
                        text='GUEST HOME PAGE',
                        font='ARIAL 40 bold underline',
                        bg='#480BAB',
                        fg='white').place(x=260, y=10)

    pdetails_button = tk.Button(root,
                            text='Personal details',
                            font='ARIAL 20 bold',
                            bg='#361869',
                            fg='white',
                            borderwidth=8,
                            command=lambda:personal_details_()).place(x=380, y=130, width=290)

    roomservice_button = tk.Button(root,
                            text='Room Service',
                            font='ARIAL 20 bold',
                            bg='#361869',
                            fg='white',
                            borderwidth=8,
                            command=lambda:roomservice()).place(x=380, y=220, width=290)

    complaint_button = tk.Button(root,
                            text='Complaint Portal',
                            font='ARIAL 20 bold',
                            bg='#361869',
                            fg='white',
                            borderwidth=8,
                            command=lambda:complain()).place(x=380, y=310, width=290)

    logout_button = tk.Button(root,
                            text='Logout',
                            font='ARIAL 20 bold',
                            bg='#361869',
                            fg='white',
                            borderwidth=8,
                            command=lambda:logout()).place(x=380, y=400, width=290)

    root.mainloop()