#updation of room count and deleting guest entry

import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
mycon = mysql.connect(host='localhost', user='root', passwd='dhruv_789_$1',database='hotel_management')
mycursor = mycon.cursor()

def billing_process(): #main billing function 
    root = tk.Tk()
    root.geometry('1000x720')
    root.title('BILLING PORTAL')
    root.config(bg='#480BAB')
    root.resizable(False, False)
    gid = tk.StringVar()

    def generate_bill():  #function denerating bill
        try:
            mycursor.execute('select * from  reg_portal where guest_id={}'.format(int(gid.get())))
            reg_data = mycursor.fetchone()
            mycursor.execute('select sum(service_cost) from room_service_used group by guest_id having guest_id={}'.format(int(gid.get())))
            room_service_cost = mycursor.fetchone()

            root1 = tk.Tk()
            root1.geometry('1000x720')
            root1.title('GENERATING BILL...')
            root1.config(bg='#480BAB')
            root1.resizable(False, False)
            bill = 0.0

            name_label = tk.Label(root1,
                    text='Name                                           :',
                    font='calibri 20 bold',
                    bg='#480BAB',
                    fg='white').place(x=80, y=150)

            pno_label = tk.Label(root1,
                                text='Phone Number                          :',
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=80, y=200)

            address_label = tk.Label(root1,  
                                text='Address                                       :',
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=80, y=250)

            nights_label = tk.Label(root1,
                                text='Number of Nights                     :',
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=80, y=350)

            members_label = tk.Label(root1,
                                text='Number of Members               :',
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=80, y=300)

            room_no_label = tk.Label(root1,
                                text='Room number                            :',
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=80, y=400)

            name_val = tk.Label(root1,
                                text=reg_data[1]+' '+reg_data[2],
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=450, y=150)

            phone_val = tk.Label(root1,  
                                text=reg_data[3],
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=450, y=200)

            add_val = tk.Label(root1,
                            text=reg_data[4],
                            font='calibri 20 bold',
                            bg='#480BAB',
                            fg='white').place(x=450, y=250)

            mem_val = tk.Label(root1,
                            text=reg_data[5],
                            font='calibri 20 bold',
                            bg='#480BAB',
                            fg='white').place(x=450, y=300)

            nights_val = tk.Label(root1,
                            text=reg_data[6],
                            font='calibri 20 bold',
                            bg='#480BAB',
                            fg='white').place(x=450, y=350)

            room_val = tk.Label(root1,
                            text=reg_data[7],
                            font='calibri 20 bold',
                            bg='#480BAB',
                            fg='white').place(x=450, y=400)

            bill_label = tk.Label(root1,
                                text='Total Amount (in rupees)         :',
                                font='calibri 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=80, y=450)

            if reg_data[8] == 'SB':
                bill = float(reg_data[6]) * 5000.0
                mycursor.execute('update room_aval set rooms_available = rooms_available + 1 where room_code="SB";')
                mycon.commit()
            elif reg_data[8] == 'DB':
                bill = float(reg_data[6]) * 7000.0
                mycursor.execute('update room_aval set rooms_available = rooms_available + 1 where room_code="DB";')
                mycon.commit()
            elif reg_data[8] == 'LB':
                bill = float(reg_data[6]) * 15000.0
                mycursor.execute('update room_aval set rooms_available = rooms_available + 1 where room_code="LB";')
                mycon.commit()

            if room_service_cost == None:
                pass
            else:
                bill = bill + float(room_service_cost[0])
            
            bill_val = tk.Label(root1,
                            text=bill,
                            font='calibri 20 bold',
                            bg='#480BAB',
                            fg='white').place(x=450, y=450)

            mycursor.execute('insert into past_guests values({},"{}","{}","{}","{}")'.format(reg_data[0], reg_data[1], reg_data[2], reg_data[3], reg_data[4]))
            mycon.commit()
            mycursor.execute('delete from reg_portal where guest_id = {}'.format(int(gid.get())))
            mycon.commit()
            mycursor.execute('delete from guest_login where username = {}'.format('guest_'+gid.get()))
            mycon.commit()
            mycursor.execute('delete from room_service_used where guest_id = {}').format(int(gid.get()))
            mycon.commit()

            messagebox.showinfo('SHOWINFO','Record has been shifted to past guests table.')

            root1.mainloop()

        except:
            messagebox.showerror('INVALID ID','There exists no entry for the given Guest ID!')

    def back():
        root.destroy()
        from admin_menu import admin_menu


    main_label = tk.Label(root,
                    text='BILLING PORTAL',
                    font='ARIAL 40 bold underline',
                    bg='#480BAB',
                    fg='white').place(x=300, y=10)

    enter_label = tk.Label(root,
                        text='Enter Guest ID',
                        font='ARIAL 20 bold',
                        bg='#480BAB',
                        fg='white').place(x=400, y=200)    

    enter_code = tk.Entry(root,
                        textvariable=gid,
                        font='calibri 15',
                        bg='#361869',
                        fg='white',
                        border=5).place(x=345, y=250, width=300, height=50)

    bill_button = tk.Button(root,
                        text='GENERATE BILL',
                        font='arial 20 bold',
                        bg='#361869',
                        fg='white',
                        border=5,
                        command=lambda:generate_bill()).place(x=365, y=310)

    back_button = tk.Button(root,
                        text='BACK',
                        font='ARIAL 15 bold',
                        bg='#361869',
                        fg='white',
                        command=lambda:back()).place(x=5, y=5)

    root.mainloop()

billing_process()