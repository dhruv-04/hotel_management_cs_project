import tkinter as tk
import mysql.connector as mysql
import random
mycon = mysql.connect(host='localhost',user='root',passwd='dhruv_789_$1',database='hotel_management')
mycursor = mycon.cursor()

def registration():  #defining main registration function
    root = tk.Tk()
    root.geometry('1000x720')
    root.config(bg='#480BA8')
    root.title('REGISTRATION PROTAL')
    root.resizable(False,False)
    f_name = tk.StringVar()
    l_name = tk.StringVar()
    p_no = tk.StringVar()
    address_ = tk.StringVar()
    no_of_members = tk.StringVar()
    no_of_nights = tk.StringVar()
    room_code = tk.StringVar()

    def submit():  #allotment of room and creating of guest id and password
        mycursor.execute('select guest_id,room_num from reg_portal;')
        reg_data = mycursor.fetchall()
        global user_data
        global password
        global room_num
        room_num = 0
        user_data = 'guest_'
        password = 'guest_'

        def password_generator():
            def generate(): 
                global user_data
                global password
                code = ''
                code_rev = ''
                for i in range(0,3):
                    code_ = random.randint(0,9)
                    code = code + str(code_)
                    code_rev = str(code_) + code_rev
                for i in range(len(reg_data)):
                    if code_ == reg_data[i][0]:
                        generate()
                    else:
                        user_data = user_data+code
                        password = password+code_rev
                        mycursor.execute('insert into guest_login values("{}","{}")'.format(user_data,password))
                        mycon.commit()
            generate()

            def room_num_gen():
                global room_num
                if room_code.get() == 'SB':
                    room_num = random.randint(1,100)
                    mycursor.execute('update room_aval set rooms_available = rooms_available - 1 where room_code="SB";')
                    mycon.commit()
                elif room_code.get() == 'DB':
                    room_num = random.randint(101,170)
                    mycursor.execute('update room_aval set rooms_available = rooms_available - 1 where room_code="DB";')
                    mycon.commit()
                elif room_code.get() == 'LB':
                    room_num = random.randint(171,190)
                    mycursor.execute('update room_aval set rooms_available = rooms_available - 1 where room_code="LB";')
                    mycon.commit()                
                print(room_num)
                for i in range(len(reg_data)):
                    if room_num == reg_data[i][1]:
                        room_num_gen()
                    else:
                        pass
            room_num_gen()

        password_generator()

        user_gid = int(user_data[6:9])
        f_name_tk = f_name.get()
        l_name_tk = l_name.get()
        p_no_tk = p_no.get()
        address_tk = address_.get()
        no_of_members_tk = no_of_members.get()
        no_of_nights_tk = no_of_nights.get()
        room_code_tk = room_code.get()
        mycursor.execute('insert into reg_portal values({},"{}","{}","{}","{}","{}","{}","{}","{}")'.format(user_gid, f_name_tk, l_name_tk, p_no_tk, address_tk, no_of_members_tk, no_of_nights_tk, room_num, room_code_tk))
        mycon.commit()

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
                            text=user_data,
                            font='Arial 20 bold',
                            bg='#480BAB',
                            fg='white').place(x=650, y=170)    

        passwd_label = tk.Label(root1,
                            text=password,
                            font='Arial 20 bold',
                            bg='#480BAB',
                            fg='white').place(x=650, y=220)

        room_num_label = tk.Label(root1,
                                text=room_num,
                                font='Arial 20 bold',
                                bg='#480BAB',
                                fg='white').place(x=650, y=270)

    def showrooms():
        from rooms_count import room_count

    def back():
        root.destroy()
        from admin_menu import admin_menu    

    def button_click(code):
        if code == 'SB':
            room_code.set('SB')
        elif code == 'DB':
            room_code.set('DB')
        elif code == 'LB':
            room_code.set('LB')

    reg_label = tk.Label(root,
                        text='REGISTRATION PORTAL',
                        font='ARIAL 30 bold underline',
                        bg='#480BAB',
                        fg='white').place(x=300, y=15)

    first_name = tk.Label(root,
                        text='First Name',
                        font='CALIBRI 15 bold',
                        bg='#480BAB',
                        fg='white').place(x=75,y=130)

    fname_entry = tk.Entry(root,
                        textvariable=f_name,
                        font='calibri 15',
                        bg='#361869',
                        fg='white',
                        border=5).place(x=75, y=170, width=350, height=50)

    phone_number = tk.Label(root,
                        text='Phone Number',
                        font='CALIBRI 15 bold',
                        bg='#480BAB',
                        fg='white').place(x=75,y=230)

    pno_entry = tk.Entry(root,
                        textvariable=p_no,
                        font='calibri 15',
                        bg='#361869',
                        fg='white',
                        border=5).place(x=75, y=270, width=350, height=50)

    num_member = tk.Label(root,
                        text='Number of Members (in numerals)',
                        font='CALIBRI 15 bold',
                        bg='#480BAB',
                        fg='white').place(x=75,y=330)

    num_member_entry = tk.Entry(root,
                            textvariable=no_of_members,
                            font='calibri 15',
                            bg='#361869',
                            fg='white',
                            border=5).place(x=75, y=370, width=350, height=50)

    last_name = tk.Label(root,
                        text='Last Name',
                        font='CALIBRI 15 bold',
                        bg='#480BAB',
                        fg='white').place(x=560,y=130)

    lname_entry = tk.Entry(root,
                        textvariable=l_name,
                        font='calibri 15',
                        bg='#361869',
                        fg='white',
                        border=5).place(x=560, y=170, width=350, height=50)

    address_label = tk.Label(root,
                        text='Address',
                        font='CALIBRI 15 bold',
                        bg='#480BAB',
                        fg='white').place(x=560,y=230)

    address_entry = tk.Entry(root,
                        textvariable=address_,
                        font='calibri 15',
                        bg='#361869',
                        fg='white',
                        border=5).place(x=560, y=270, width=350, height=50)

    num_nights_label = tk.Label(root,
                        text='Number of Nights (in numerals)',
                        font='CALIBRI 15 bold',
                        bg='#480BAB',
                        fg='white').place(x=560,y=330)

    num_nights_entry = tk.Entry(root,
                        textvariable=no_of_nights,
                        font='calibri 15',
                        bg='#361869',
                        fg='white',
                        border=5).place(x=560, y=370, width=350, height=50)

    room_code_label = tk.Label(root,
                            text='Room Code',
                            font='calibri 15 bold',
                            bg='#480BAB',
                            fg='white').place(x=70, y=457)

    sb_button = tk.Button(root,
                        text='SB',
                        font='ARIAL 15 bold',
                        bg='#361869',
                        fg='white',
                        border=7,
                        command = lambda:button_click('SB')).place(x=445, y=450, width=100, height=50)

    db_button = tk.Button(root,
                        text='DB',
                        font='ARIAL 15 bold',
                        bg='#361869',
                        fg='white',
                        border=7,
                        command = lambda:button_click('DB')).place(x=545, y=450, width=100, height=50)

    lb_button = tk.Button(root,
                        text='LB',
                        font='ARIAL 15 bold',
                        bg='#361869',
                        fg='white',
                        border=7,
                        command = lambda:button_click('LB')).place(x=645, y=450, width=100, height=50)

    show_room_button = tk.Button(root,
                            text='SHOW ROOMS',
                            font='ARIAL 15 bold',
                            bg='#361869',
                            fg='white',
                            border=7,
                            command=lambda:showrooms()).place(x=745, y=450, height=50)

    room_code_entry = tk.Entry(root,
                            text=room_code,
                            font='calibri 15',
                            bg='#361869',
                            fg='white',
                            border=5).place(x=190, y=450, width=250, height=50)

    submit_button = tk.Button(root,
                            text='SUBMIT',
                            font='ARIAL 15 bold',
                            bg='#361869',
                            fg='white',
                            border=10,
                            command=lambda:submit()).place(x=450, y=525, width=130, height=50)

    back_button = tk.Button(root,
                        text='BACK',
                        font='ARIAL 15 bold',
                        bg='#361869',
                        fg='white',
                        command=lambda:back()).place(x=5, y=5)

    root.mainloop()

registration()