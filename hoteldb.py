import mysql.connector as ms

db = ms.connect(host="localhost",user="root",passwd='Dhruv471__01')

if db.is_connected():
    print("Connection Established")
else:
    print("Connection Not Connected")

cs = db.cursor()

cs.execute("drop database if exists hotel_management;")
cs.execute("create database hotel_management;")
cs.execute("use hotel_management;")

cs.execute("create table employee_login(\
    Username varchar(20) primary key,\
    Password varchar(20) not null);")

cs.execute('insert into employee_login values("employee_admin","employee_01")')

cs.execute("create table guest_login(\
    Username varchar(20) primary key,\
    Password varchar(20) not null,\
    Room_num integer not null);")

cs.execute('insert into guest_login values("guest_012","guest_210",123)')

cs.execute("create table reg_portal(\
    GuestID integer primary key,\
    FirstName varchar(20) not null,\
    LastName varchar(20) not null,\
    PhoneNumber char(10) not null,\
    Address varchar(50) not null,\
    Num_Members char(2) not null,\
    Num_Nights char(2) not null,\
    Room_Num integer not null,\
    Room_Code char(2) not null);")

cs.execute('insert into reg_portal values(012,"Dhruv","Kumar","9903847103","Patparganj","02","07",123,"DB")')

cs.execute("create table room_aval(\
    Room_Name varchar(30),\
    Room_Code char(2),\
    Room_Costs int,\
    Room_Available int);")
cs.execute("insert into room_aval values ('DOUBLE BED ROOM','DB',7000,69);")
cs.execute("insert into room_aval values ('LUXURY ROOM','LB',15000,20);")
cs.execute("insert into room_aval values ('SINGLE BED ROOM','SB',5000,100);")

cs.execute("create table room_service(\
    Guest_ID int not null,\
    Room_Num int,\
    Service_Cost int,\
    Service_Code char(2));")

cs.execute("create table user_login(\
    Username varchar(20) primary key,\
    Room_Num int);")

cs.execute("create table past_guests(\
    GuestID int not null,\
    FirstName varchar(20) not null,\
    LastName varchar(20) not null,\
    PhoneNumber char(10) not null,\
    Address varchar(50) not null);")

cs.execute("create table complaint(\
    Room_Num int not null,\
    Complaint varchar(100) not null);")

db.commit()
