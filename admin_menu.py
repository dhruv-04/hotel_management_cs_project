import tkinter as tk
import mysql.connector as mysql
mycon = mysql.connect(host='localhost', user='root', passwd='Dhruv471__01',database='hotel_management')
mycursor = mycon.cursor()

def admin_menu():   #defining admin_menu function
    root = tk.Tk()
    root.geometry('1000x720')
    root.title('ADMIN MENU')
    root.config(bg='#480BAB')
    root.resizable(False, False)

    def call_reg():  #to be performed on registration button click
        root.destroy()
        from registration import registration #calling registration function from registration.py
        registration()

    def call_billing(): #to be performed on billing button click
        root.destroy()
        from billing import billing_process #calling billing_process from billing.py
        billing_process()

    def call_search():
        root.destroy()
        from search_info import search_label
        search_label()

    def call_complaint():
        root.destroy()
        from complaint_admin import complaint
        complaint()

    def logout(): #takes back to main homepage
        root.destroy()
        from home_page import homepage #calling homepage function from home_page.py
        homepage()
    
    main_heading = tk.Label(root,
                        text='ADMIN MENU',
                        font='ARIAL 40 bold underline',
                        bg='#480BAB',
                        fg='white').place(x=350, y=10)

    reg_button = tk.Button(root,
                            text='Registration Portal',
                            font='ARIAL 20 bold',
                            bg='#361869',
                            fg='white',
                            borderwidth=8,
                            command=lambda:call_reg()).place(x=380, y=130, width=290)

    search_button = tk.Button(root,
                            text='Search details',
                            font='ARIAL 20 bold',
                            bg='#361869',
                            fg='white',
                            borderwidth=8,
                            command=lambda:call_search()).place(x=380, y=220, width=290)

    billing_button = tk.Button(root,
                            text='Billing Portal',
                            font='ARIAL 20 bold',
                            bg='#361869',
                            fg='white',
                            borderwidth=8,
                            command=lambda:call_billing()).place(x=380, y=310, width=290)

    complaint_button = tk.Button(root,
                            text='Complaint Portal',
                            font='ARIAL 20 bold',
                            bg='#361869',
                            fg='white',
                            borderwidth=8,
                            command=lambda:call_complaint()).place(x=380, y=400, width=290)

    logout_button = tk.Button(root,
                            text='Logout',
                            font='ARIAL 20 bold',
                            bg='#361869',
                            fg='white',
                            borderwidth=8,
                            command=lambda:logout()).place(x=380, y=490, width=290)

    root.mainloop()