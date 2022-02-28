import tkinter as tk
import mysql.connector as mysql
mycon = mysql.connect(host='localhost',user='root',passwd='dhruv_789_$1',database='hotel_management')
mycursor = mycon.cursor()
mycursor.execute('select * from room_aval;')
room_data = mycursor.fetchall()


def room_count():
    root = tk.Tk()
    root.geometry('920x350')
    root.config(bg='#480BA8')
    root.title('ROOMS AVAILABILITY')
    root.resizable(False,False)

    main_label = tk.Label(root,
                        text='ROOMS AVAILABILTY',
                        font='ARIAL 30 bold underline',
                        bg='#480BAB',
                        fg='white').place(x=265, y=5)

    room_label = tk.Label(root,
                        text='Rooms',
                        font='calibri 20 bold ',
                        bg='#480BAB',
                        fg='white').place(x=85, y=100)

    room_code = tk.Label(root,
                        text='Room Code',
                        font='calibri 20 bold ',
                        bg='#480BAB',
                        fg='white').place(x=255, y=100)

    room_avail = tk.Label(root,
                        text='No. of Rooms Available',
                        font='calibri 20 bold ',
                        bg='#480BAB',
                        fg='white').place(x=440, y=100)

    room_cost = tk.Label(root,
                        text='Room Cost',
                        font='calibri 20 bold ',
                        bg='#480BAB',
                        fg='white').place(x=755, y=100)

    room_label_sb = tk.Label(root,
                        text='Single Bed Room',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=58, y=150)

    room_code_sb = tk.Label(root,
                        text='SB',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=299, y=150)

    room_avail_sb = tk.Label(root,
                        text=room_data[2][3],
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=550, y=150)

    room_cost_sb = tk.Label(root,
                        text='5000',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=799, y=150)

    room_label_db = tk.Label(root,
                        text='Double Bed Room',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=58, y=200)

    room_code_db = tk.Label(root,
                        text='DB',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=299, y=200)

    room_avail_db = tk.Label(root,
                        text=room_data[0][3],
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=555, y=200)

    room_cost_db = tk.Label(root,
                        text='7000',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=799, y=200)

    room_label_lb = tk.Label(root,
                        text='Luxury Room',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=58, y=250)

    room_code_lb = tk.Label(root,
                        text='LB',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=299, y=250)

    room_avail_lb = tk.Label(root,
                        text=room_data[1][3],
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=555, y=250)

    room_cost_db = tk.Label(root,
                        text='15000',
                        font='calibri 15',
                        bg='#480BAB',
                        fg='white').place(x=795, y=250)

    root.mainloop()

room_count()