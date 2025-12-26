import tkinter
import customtkinter
import webbrowser
import os
from PIL import ImageTk, Image
from functools import partial
#WE ARE USING DATABASE BUDGET1
def destroypi():
    pi.destroy()
def destroyfgp():
    win2.destroy()
import mysql.connector
import random
sqlobj=mysql.connector.connect(host='localhost',password='12345678',user='root')
f=sqlobj.cursor()
f.execute('create database if not exists Budget1')

f.execute('use Budget1')

f.execute('create table if not exists main_info(id varchar(4),u_name varchar(25),pas varchar(25),name varchar(25),age int, dob varchar(25))')
f.execute("create table if not exists personal_info(id int,salary int,exp int,sav int)")
def login_page():#LOGIN PAGE AND LEADS THEM TO HOMEPAGE IF DETAILS ARE CORRECT
    global entry1
    global entry2
    global l2
    customtkinter.set_appearance_mode('System') # can set light or dark
    customtkinter.set_default_color_theme("green") # themes: blue, dark-blue, or green

    win1 = customtkinter.CTk() # creating window
    win1.geometry('600x450')
    win1.title('Login')

    patt1 = customtkinter.CTkImage(Image.open(r"ASSETS/pattern_login.png"),size=(600, 450))
    l1 = customtkinter.CTkLabel(master=win1, image=patt1)
    l1.pack()

    frame = customtkinter.CTkFrame(master=l1, width=320, height=360)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    l2 = customtkinter.CTkLabel(master=frame, text='Log into your account',font=('Century Gothic', 20))
    l2.place(x=50, y=45)

    entry1 = customtkinter.CTkEntry(master=frame, width=220,placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2 = customtkinter.CTkEntry(master=frame, width=220, show='*',placeholder_text='Password')
    entry2.place(x=50, y=165)

    button1 = customtkinter.CTkButton(master=frame, text='ForgotPassword?', width=5, height=5, fg_color='#6495ED',font=('CenturyGothic', 12), command=frgtpg)
    button1.place(x=155, y=195)

    button2 = customtkinter.CTkButton(master=frame, width=220,text='Login', corner_radius=6, command=check)
    button2.place(x=50, y=240)

    l3 = customtkinter.CTkLabel(master=frame, text='Dont have an account? Sign Up', font=('Century Gothic', 10))
    l3.place(x=76, y=280)

    button3 = customtkinter.CTkButton(master=frame, text='Sign up!',font=('Century Gothic', 10), command=signupscreen)
    button3.place(x=90, y=310)

    win1.mainloop()
def check():#CHECKS IF LOGIN INFO IS CORRECT AND THEN LOGS IN
    global l2
    global f
    global entry1
    global entry2
    global iden
    un=entry1.get()
    password=entry2.get()
    f.execute("select u_name,pas from main_info where u_name='{}'".format(un))
    d=f.fetchall()
    if len(d)!=0:
        u_name=d[0][0]
        pas=d[0][1]
        print(u_name,pas)
        if un==u_name and pas==password:
            f.execute("select id from main_info where u_name='{}'".format(un))
            d=f.fetchall()
            iden=d[0][0]
            Homepage()
        else:
            l2.configure(text='Sorry wrong credentials!')
    else:
        l2.configure(text='Sorry wrong credentials!')
def frgtpg():#ALLOWS RESET OF PASSWORD AND THEN LOGIN
    global entry_1
    global entry_4
    global entry_2
    global entry_3
    global win2
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('blue')
    win2 = customtkinter.CTkToplevel()
    win2.geometry('600x450')
    win2.title('Forgot password?')
    win2.attributes('-topmost', True)
    patt2 = customtkinter.CTkImage(Image.open("ASSETS/forgot.jpeg"), size=(600,450))
    l_1 = customtkinter.CTkLabel(master=win2, image=patt2)
    l_1.pack()
    frame_2 = customtkinter.CTkFrame(master=l_1, width=350, height=350)
    frame_2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    l_2 = customtkinter.CTkLabel(master=frame_2, text="Reset Your Password", font=('Century Gothic', 20))
    l_2.place(x=50, y=45)
    entry_1 = customtkinter.CTkEntry(master=frame_2, width=220,placeholder_text='Enter Username')
    entry_1.place(x=50, y=110)
    entry_2 = customtkinter.CTkEntry(master=frame_2, width=220,placeholder_text='Enter Unique No')
    entry_2.place(x=50, y=150)
    entry_3 = customtkinter.CTkEntry(master=frame_2, width=220,placeholder_text='Enter Password', show='*')
    entry_3.place(x=50, y=190)
    entry_4 = customtkinter.CTkEntry(master=frame_2, width=220,placeholder_text='Confirm Password', show='*')
    entry_4.place(x=50, y=230)
    button_1 = customtkinter.CTkButton(master=frame_2, width=220,text='Continue', corner_radius=6,command=check2)
    button_1.place(x=50, y=290)
    win2.mainloop()
def check2():#CHECKS IF NEW PASSWORD CREDENTIALS ARE CORRECT
    global entry_1
    global entry_4
    global entry_2
    global entry_3
    iden2=entry_2.get()
    un2=entry_1.get()
    cp1=entry_3.get()
    cp2=entry_4.get()
    if cp1==cp2:
        try:
            f.execute("update main_info set pas='{}' where id='{}' and u_name='{}'".format(cp1,iden2,un2))
            sqlobj.commit()
        except:
            frgtpg()
        else:
            destroyfgp()
def signupscreen():#IF FIRST TIME USER ENTERS MAIN INFORMATION
    global swe1
    global swe2
    global swe3
    global swe4
    global swe5
    global f
    global sw1
    global iden
    global frame
    sw1= customtkinter.CTkToplevel()
    sw1.geometry('600x450')
    sw1.title('Sign up')
    sw1.attributes('-topmost', True)
    patt2 = customtkinter.CTkImage(Image.open("ASSETS/sign up.png"), size=(600,450))
    s1 = customtkinter.CTkLabel(master=sw1, image=patt2)
    s1.pack()
    frame = customtkinter.CTkFrame(master=sw1, width=320, height=450)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    sw2 = customtkinter.CTkLabel(master=frame, text='Lets Sign up!',font=('Century Gothic', 20))
    sw2.place(x=50, y=45)
    swe1=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Full Name')
    swe1.place(x=50,y=110)
    swe2=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Age')
    swe2.place(x=50,y=150)
    swe3=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='DOB(dd-mm-yyyy)')
    swe3.place(x=50,y=190)
    swe4=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Username')
    swe4.place(x=50,y=230)
    swe5=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Password',show='*')
    swe5.place(x=50,y=270)
    sw3= customtkinter.CTkLabel(master=frame, text='Please Read Terms and Conditions Before Continuing', font=('Century Gothic', 11))
    sw3.place(x=25, y=310)
    sw4= customtkinter.CTkLabel(master=frame, text='I agree and would like to Signup', font=('Century Gothic', 11))
    sw4.place(x=70, y=375)
    def callback(url):
        file_path = "/Users/pvneeharikha/Documents/VBUCKS/DOCS/Terms and Conditions.docx"
        webbrowser.open("file://" + os.path.abspath(file_path))
    swb1 = customtkinter.CTkButton(master=frame,text="Terms and conditions", cursor="hand2")
    swb1.place(x=90, y=340)
    swb1.bind("<Button-1>", lambda e:callback("Terms and Conditions.docx"))
    swb2 = customtkinter.CTkButton(master=frame, text='Agree And Signup!',font=('Century Gothic', 12), command=lambda: [insert(),personalinfo()])
    swb2.place(x=90, y=400)
    sw1.mainloop()
def insert():#INSERTS MAIN INFORMATION INTO TABLE MAIN_INFO
    global swe1
    global swe2
    global swe3
    global swe4
    global swe5
    global iden
    name=swe1.get()
    age=swe2.get()
    dob=swe3.get()
    un3=swe4.get()
    pas2=swe5.get()
    f.execute('select id from main_info')
    d=f.fetchall()
    print(d)
    iden3=random.randint(1000,9999)
    for i in d:
        if iden3==i[0]:iden3=random.randint(1000,9999)
    iden=iden3
    f.execute("insert into main_info values('{}','{}','{}','{}',{},'{}')".format(iden,un3,pas2,name,int(age),dob))
    sqlobj.commit()
def personalinfo():#IT ACCEPTS PERSONAL INFO LIKE SALARY & EXPENDITURE
    global pie1
    global pie2
    global pie3
    global pie4
    global pie5
    global pie6
    global pie7
    global pi
    pi = customtkinter.CTkToplevel()
    pi.geometry('600x450')
    pi.title('Personal Info')
    pi.attributes('-topmost', True)
    sw1.attributes('-topmost', False)
    piframe = customtkinter.CTkFrame(master=pi, width=320, height=360)
    patt3 = customtkinter.CTkImage(Image.open("ASSETS/personal_info.jpeg"),size=(600, 450))
    p1 = customtkinter.CTkLabel(master=pi, image=patt3)
    p1.pack()
    frame = customtkinter.CTkFrame(master=pi, width=320, height=450)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    pi1 = customtkinter.CTkLabel(master=frame, text='Enter Personal info',font=('Century Gothic', 20))
    pi1.place(x=50, y=45)
    pie1 = customtkinter.CTkEntry(master=frame, width=220,placeholder_text='Monthly Salary')
    pie1.place(x=50, y=90)
    pi2=customtkinter.CTkLabel(master=frame,text='Enter Monthly Expenditure', font=('Century Gothic', 16))
    pi2.place(x=50,y=120)
    pie2=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Water')
    pie2.place(x=50,y=150)
    pie3=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Electricity')
    pie3.place(x=50,y=190)
    pie4=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Gas')
    pie4.place(x=50,y=230)
    pie5=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Education')
    pie5.place(x=50,y=270)
    pie6=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Grocery')
    pie6.place(x=50,y=310)
    pie7=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Others')
    pie7.place(x=50,y=350)
    pib = customtkinter.CTkButton(master=frame, text='Continue',font=('Century Gothic', 12), command=lambda:[insert2(),destroypi()])
    pib.place(x=90, y=410)
    pi.mainloop()
def insert2():#INSERTS ACCEPTED VALUES INTO TABLE PERSONAL_INFO AND GOES TO HOMEPAGE
    global pie1
    global pie2
    global pie3
    global pie4
    global pie5
    global pie6
    global pie7
    global exp
    global salary
    global iden
    salary=int(pie1.get())
    ex1=int(pie2.get())
    ex2=int(pie3.get())
    ex3=int(pie4.get())
    ex4=int(pie5.get())
    ex5=int(pie6.get())
    ex6=int(pie7.get())
    exp=ex1+ex2+ex3+ex4+ex5+ex6
    f.execute("insert into personal_info values({},{},{},{})".format(iden,salary,exp,salary-exp))
    sqlobj.commit()
    Homepage()
def Homepage():#OFFERS ADD GOALS, EMI CALCULATOR, FINANCIAL INFO OPTIONS
    global win3
    global iden
    win3 = customtkinter.CTkToplevel()
    win3.geometry('530x500')
    win3.title('Home page')
    win3.attributes('-topmost', True)
    patt3 = customtkinter.CTkImage(Image.open("ASSETS/Home page.jpeg"),size=(530, 500))
    p1 = customtkinter.CTkLabel(master=win3, image=patt3)
    p1.pack()
    a = customtkinter.CTkLabel(master=win3, text='App', font=('century gothic',20))
    a.pack()
    b_1 = customtkinter.CTkButton(master=win3, width=200, height=150,text='EMI', font=('Century Gothic', 20),fg_color="#1E466F",hover_color="#242A2F",text_color="white",  command=emi_page)
    b_1.place(x=50, y=50)
    b_2 = customtkinter.CTkButton(master=win3, width=200, height=150,text="Previous Goals", font=('Century Gothic', 20),fg_color="#1E466F",hover_color="#242A2F",text_color="white", command=pre_goals)
    b_2.place(x=280, y=50)
    b_3 = customtkinter.CTkButton(master=win3, width=200, height=150,text="Add Goals", font=('Century Gothic', 20), fg_color="#1E466F",hover_color="#242A2F",text_color="white", command=addgoals)
    b_3.place(x=50, y=250)
    def financial_info():
        file_path = "/Users/pvneeharikha/Documents/VBUCKS/financial_info.html"
        webbrowser.open(f"file://"+file_path)
    b_4 = customtkinter.CTkButton(master=win3, width=200, height=150,text="Financial Information", font=('Century Gothic', 20),fg_color="#1E466F",hover_color="#242A2F",text_color="white", command=financial_info)
    b_4.place(x=280, y=250)
    randomno= customtkinter.CTkLabel(master=win3, text='Unique ID number :', font=('century gothic', 20))
    randomno.place(x=50,y=450)
    no=customtkinter.CTkLabel(master=win3, text='{}'.format(iden),font=('century gothic', 20))
    no.place(x=250,y=450)
    win3.mainloop()
def pre_goals():
    global iden
    try:
        f.execute("select * from {}".format('goals_'+str(iden)))
        L1=f.fetchall()
    except:
        kp = customtkinter.CTkToplevel()
        kp.geometry('600x450')
        kp.title('Financial Plan Page')
        kp.attributes('-topmost', True)
        patt6= customtkinter.CTkImage(Image.open("ASSETS/Financial Plan.jpg"),size=(600, 450))
        kp1= customtkinter.CTkLabel(master=kp, image=patt6)
        kp1.pack()
        frame3 = customtkinter.CTkFrame(master=kp, width=500, height=500)
        frame3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        kpt= customtkinter.CTkLabel(master=frame3, text='No existing Records',font=('Century Gothic', 25,'underline'))
        kpt.place(x=10, y=30)
        kp.mainloop()
    else:
        if len(L1)==0:  
            kp = customtkinter.CTkToplevel()
            kp.geometry('600x450')
            kp.title('Financial Plan Page')
            kp.attributes('-topmost', True)
            patt6= customtkinter.CTkImage(Image.open("ASSETS/Financial Plan.jpg"),size=(600, 450))
            kp1= customtkinter.CTkLabel(master=kp, image=patt6)
            kp1.pack()
            frame3 = customtkinter.CTkFrame(master=kp, width=500, height=500)
            frame3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            kpt= customtkinter.CTkLabel(master=frame3, text='No existing Records', font=('Century Gothic', 25,'underline'))
            kpt.place(x=10, y=30)
            kp.mainloop()
        else:
            kp = customtkinter.CTkToplevel()
            kp.geometry('600x450')
            kp.title('Financial Plan Page')
            kp.attributes('-topmost', True)
            patt6= customtkinter.CTkImage(Image.open("ASSETS/Financial Plan.jpg"),size=(600, 450))
            kp1= customtkinter.CTkLabel(master=kp, image=patt6)
            kp1.pack()
            frame3 = customtkinter.CTkFrame(master=kp, width=500, height=500)
            frame3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            kpt= customtkinter.CTkLabel(master=frame3, text='Your Financial Plan', font=('Century Gothic', 25,'underline'))
            kpt.place(x=10, y=30)
            kpt1= customtkinter.CTkLabel(master=frame3, text='{}'.format(L1[0][1]) ,font=('Century Gothic', 20, 'bold'))
            kpt1.place(x=10, y=80)
            kpt2= customtkinter.CTkLabel(master=frame3, text='Time :{}'.format(L1[0][4]), font=('Century Gothic', 15))
            kpt2.place(x=10, y=120)
            kpt3= customtkinter.CTkLabel(master=frame3, text='Monthly Requirement :{}'.format(L1[0][3]), font=('Century Gothic', 15))
            kpt3.place(x=200, y=120)
            kpt4= customtkinter.CTkLabel(master=frame3, text='{}'.format(L1[1][1]), font=('Century Gothic', 20, 'bold'))
            kpt4.place(x=10, y=200)
            kpt5= customtkinter.CTkLabel(master=frame3, text='Time :{}'.format(L1[1][4]), font=('Century Gothic', 15))
            kpt5.place(x=10, y=240)
            kpt6= customtkinter.CTkLabel(master=frame3, text='Monthly Requirement :{}'.format(L1[1][3]), font=('Century Gothic', 15))
            kpt6.place(x=200, y=240)
            kpt7= customtkinter.CTkLabel(master=frame3, text='{}'.format(L1[2][1]), font=('Century Gothic', 20, 'bold'))
            kpt7.place(x=10, y=320)
            kpt8= customtkinter.CTkLabel(master=frame3, text='Time :{}'.format(L1[2][4]), font=('Century Gothic', 15))
            kpt8.place(x=10, y=360)
            kpt9= customtkinter.CTkLabel(master=frame3, text='Monthly Requirement :{}'.format(L1[2][3]), font=('Century Gothic', 15))
            kpt9.place(x=200, y=360)
            kp.mainloop()
def addgoals():#ACCEPTS GOAL INFO AND LEADS TO FINANCIAL PLAN
    global ad
    global ade1
    global ade2
    global ade3
    global ade4
    global ade5
    global ade6
    global ade7
    global ade8
    global ade9
    ad = customtkinter.CTkToplevel()
    ad.geometry('600x450')
    ad.title('Add Goals')
    ad.attributes('-topmost', True)
    win3.attributes('-topmost', False)
    patt4 = customtkinter.CTkImage(Image.open("ASSETS/Add Goals.jpeg"), size=(600,450))
    p1 = customtkinter.CTkLabel(master=ad, image=patt4)
    p1.pack()
    frame = customtkinter.CTkFrame(master=ad, width=320, height=470)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    ad1 = customtkinter.CTkLabel(master=frame, text='Add Goals',font=('Century Gothic', 20))
    ad1.place(x=50, y=10)
    ad2 = customtkinter.CTkLabel(master=frame, text='Please Enter Your Goal Cost ' , font=('Century Gothic', 10))
    ad2.place(x=90, y=40)
    ad3 = customtkinter.CTkLabel(master=frame, text='After Deducting Any Pre-Existing Savings towards it', font=('Century Gothic', 10))
    ad3.place(x=40, y=60)
    ade1 = customtkinter.CTkEntry(master=frame, width=220,placeholder_text='Add Your Goal 1')
    ade1.place(x=50, y=90)
    ade2=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Enter Cost Of Goal 1')
    ade2.place(x=50,y=120)
    ade3=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Enter Priority')
    ade3.place(x=50,y=150)
    ade4=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Add Your Goal 2')
    ade4.place(x=50,y=200)
    ade5=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Enter Cost Of Goal 2')
    ade5.place(x=50,y=230)
    ade6=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Enter Priority')
    ade6.place(x=50,y=260)
    ade7=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Add your Goal 3')
    ade7.place(x=50,y=310)
    ade8=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Enter Cost of Goal 3')
    ade8.place(x=50,y=340)
    ade9=customtkinter.CTkEntry(master=frame,width=220,placeholder_text='Enter Priority')
    ade9.place(x=50,y=370)
    adb = customtkinter.CTkButton(master=frame, text='Add Goals & Continue', font=('Century Gothic', 12), command=financialpage)
    adb.place(x=90, y=420)
    ad.mainloop()
def financialpage():#DISPLAYS FINANCIAL PLAN IF VIABLE
    global ade1
    global ade2
    global ade3
    global ade4
    global ade5
    global ade6
    global ade7
    global ade8
    global ade9
    global iden
    global fp
    global L1
    f.execute("select sav from personal_info where id={}".format(iden))
    d=f.fetchall()
    try:
        f.execute("create table goals_{}(prior int,gn varchar(25),gc int,mc int,time int)".format(iden))
    except:
        f.execute('delete from goals_{}'.format(iden))
        sqlobj.commit()
        #d int,salary int,exp int,sav int
        L1=[[int(ade3.get()),ade1.get(),int(ade2.get())],[int(ade6.get()),ade4.get(),int(ade5.get())],[int(ade9.get()),ade7.get(),int(ade8.get())]]
        savings=d[0][0]
        L1.sort()#[prior,goalname,goalcost,monthlyreq,time]
        ma1=0.5*savings
        ma2=0.30*savings
        ma3=0.20*savings
        t1=round(L1[0][2]/ma1,3)
        t2=round(L1[1][2]/ma2,3)
        t3=round(L1[2][2]/ma3,3)
        L1[0].append(ma1)
        L1[0].append(t1)
        L1[1].append(ma2)
        L1[1].append(t2)
        L1[2].append(ma3)
        L1[2].append(t3)
        sqlobj.commit()
        if t1<36:
            fp = customtkinter.CTkToplevel()
            fp.geometry('600x450')
            fp.title('Financial Plan Page')
            fp.attributes('-topmost', True)
            ad.attributes('-topmost', False)
            patt6= customtkinter.CTkImage(Image.open("ASSETS/Financial Plan.jpg"),size=(600, 450))
            fp1= customtkinter.CTkLabel(master=fp, image=patt6)
            fp1.pack()
            frame = customtkinter.CTkFrame(master=fp, width=500, height=500)
            frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            fpt= customtkinter.CTkLabel(master=frame, text='Your Financial Plan',font=('Century Gothic', 25,'underline'))
            fpt.place(x=10, y=30)
            fpt1= customtkinter.CTkLabel(master=frame, text='{}'.format(L1[0][1]) ,font=('Century Gothic', 20, 'bold'))
            fpt1.place(x=10, y=80)
            fpt2= customtkinter.CTkLabel(master=frame, text='Time :{}'.format(L1[0][4]), font=('Century Gothic', 15))
            fpt2.place(x=10, y=120)
            fpt3= customtkinter.CTkLabel(master=frame, text='Monthly Requirement :{}'.format(L1[0][3]), font=('Century Gothic', 15))
            fpt3.place(x=200, y=120)
            fpt4= customtkinter.CTkLabel(master=frame, text='{}'.format(L1[1][1]),font=('Century Gothic', 20, 'bold'))
            fpt4.place(x=10, y=200)
            fpt5= customtkinter.CTkLabel(master=frame, text='Time :{}'.format(L1[1][4]), font=('Century Gothic', 15))
            fpt5.place(x=10, y=240)
            fpt6= customtkinter.CTkLabel(master=frame, text='Monthly Requirement :{}'.format(L1[1][3]), font=('Century Gothic', 15))
            fpt6.place(x=200, y=240)
            fpt7= customtkinter.CTkLabel(master=frame, text='{}'.format(L1[2][1]),font=('Century Gothic', 20, 'bold'))
            fpt7.place(x=10, y=320)
            fpt8= customtkinter.CTkLabel(master=frame, text='Time :{}'.format(L1[2][4]), font=('Century Gothic', 15))
            fpt8.place(x=10, y=360)
            fpt9= customtkinter.CTkLabel(master=frame, text='Monthly Requirement :{}'.format(L1[2][3]), font=('Century Gothic', 15))
            fpt9.place(x=200, y=360)
            fpb1= customtkinter.CTkButton(master=frame, text='Shorter Period Plans', font=('Century Gothic', 12), command=shorterplans)
            fpb1.place(x=20, y=420)
            fpb2= customtkinter.CTkButton(master=frame, text='Save',font=('Century Gothic', 12),command=insert_3)
            fpb2.place(x=180, y=420)
            fpb3= customtkinter.CTkButton(master=frame, text='EMI Options',font=('Century Gothic', 12), command=emichoice)
            fpb3.place(x=340, y=420)
            fp.mainloop()
        else:
                emichoice()
def insert_3():
    global iden
    global L1
    f.executemany("insert into goals_{} values(%s,%s,%s,%s,%s)".format(iden),L1)
    sqlobj.commit()
def shorterplans():#DISPLAYS IMPROVED PLAN IF PRIMARY GOAL NEEDS TO BE ACHIEVED FASTER
    global iden
    global L1
    L1[0][3]=L1[0][3]+0.25*L1[1][3]+0.25*L1[2][3]
    L1[1][3]=0.75*L1[1][3]
    L1[2][3]=0.75*L1[2][3]
    L1[0][4]=round(L1[0][2]/L1[0][3],3)
    L1[1][4]=round(L1[1][2]/L1[1][3],3)
    L1[2][4]=round(L1[2][2]/L1[2][3],3)
    f.executemany("insert into goals_{} values(%s,%s,%s,%s,%s)".format(iden),L1)
    sqlobj.commit()
    sp= customtkinter.CTkToplevel()
    sp.geometry('600x450')
    sp.title('Shorter Plans Page')
    sp.attributes('-topmost', True)
    fp.attributes('-topmost', False)
    patt7= customtkinter.CTkImage(Image.open("ASSETS/Financial Plan.jpg"),size=(600, 450))
    sp1= customtkinter.CTkLabel(master=sp, image=patt7)
    sp1.pack()
    frame = customtkinter.CTkFrame(master=sp, width=450, height=420)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    spt= customtkinter.CTkLabel(master=frame, text='Your Financial Plan',font=('Century Gothic', 25,'underline'))
    spt.place(x=10, y=30)
    spt1= customtkinter.CTkLabel(master=frame,text='{}'.format(L1[0][1]),font=('Century Gothic', 20, 'bold'))
    spt1.place(x=10, y=80)
    spt2= customtkinter.CTkLabel(master=frame, text='Time :{}'.format(L1[0][4]), font=('Century Gothic', 15))
    spt2.place(x=10, y=120)
    spt3= customtkinter.CTkLabel(master=frame, text='Monthly Requirement :{}'.format(L1[0][3]), font=('Century Gothic', 15))
    spt3.place(x=200, y=120)
    spt4= customtkinter.CTkLabel(master=frame,text='{}'.format(L1[1][1]),font=('Century Gothic', 20, 'bold'))
    spt4.place(x=10, y=200)
    spt5= customtkinter.CTkLabel(master=frame, text='Time :{}'.format(L1[1][4]), font=('Century Gothic', 15))
    spt5.place(x=10, y=240)
    spt6= customtkinter.CTkLabel(master=frame, text='Monthly Requirement :{}'.format(L1[1][3]), font=('Century Gothic', 15))
    spt6.place(x=200, y=240)
    spt7= customtkinter.CTkLabel(master=frame, text='{}'.format(L1[2][1]),font=('Century Gothic', 20, 'bold'))
    spt7.place(x=10, y=320)
    spt8= customtkinter.CTkLabel(master=frame, text='Time :{}'.format(L1[2][4]), font=('Century Gothic', 15))
    spt8.place(x=10, y=360)
    spt9= customtkinter.CTkLabel(master=frame, text='Monthly Requirement :{}'.format(L1[2][3]), font=('Century Gothic', 15))
    spt9.place(x=200, y=360)
def emichoice():
    global emi
    emi= customtkinter.CTkToplevel()
    emi.geometry('600x450')
    emi.title('Choice Of EMI')
    emi.attributes('-topmost', True)
    global L1
    customtkinter.set_appearance_mode('light')
    customtkinter.set_default_color_theme('blue')
    patt7= customtkinter.CTkImage(Image.open("ASSETS/Financial Plan.jpg"),size=(600, 450))
    emc= customtkinter.CTkLabel(master=emi, image=patt7)
    emc.pack()
    frame = customtkinter.CTkFrame(master=emi, width=350, height=450)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    emi1= customtkinter.CTkLabel(master=frame, text='Enter Your Choice Of EMI', font=('Century Gothic', 20,))
    emi1.place(x=20, y=30)
    action1=partial(emi_page_goal,L1[0][2])
    action2=partial(emi_page_goal,L1[1][2])
    action3=partial(emi_page_goal,L1[2][2])
    button1 = customtkinter.CTkButton(master=frame, text='Goal 1:{}'.format(L1[0][1]),width=190, height=90,font=('Century Gothic',18),command=action1)
    button1.place(x=70, y=80)
    button2 = customtkinter.CTkButton(master=frame, width=190, height=90,text='Goal 2:{}'.format(L1[1][1]), font=('Century Gothic',18),command=action2)
    button2.place(x=70, y=210)
    button3 = customtkinter.CTkButton(master=frame, text='Goal 3:{}'.format(L1[2][1]),width=190, height=90, font=('Century Gothic',18),command=action3)
    button3.place(x=70, y=340)
def emi_page_goal(gc):#ALLOWS THEM TO ENTER DETAILS TO CALCULATE EMI
    global entryemi
    global entryemi3
    global emi2
    global emi
    global emi1
    global L1
    global iden
    win10=customtkinter.CTkToplevel()
    win10.geometry('600x450')
    win10.title('EMI')
    win10.attributes('-topmost',True)
    emi.attributes('-topmost',False)
    patt_5=customtkinter.CTkImage(Image.open("ASSETS/EMI_Calculator.png"),size=(600, 450))
    l1=customtkinter.CTkLabel(master=win10, image=patt_5,text=None)
    l1.pack()
    frameemi=customtkinter.CTkFrame(master=l1,width=320,height=300)
    frameemi.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    emi1=customtkinter.CTkLabel(master=frameemi,text='EMI Calculator',font=('Century Gothic', 20))
    emi1.place(x=50,y=50)
    entryemi=customtkinter.CTkEntry(master=frameemi,width=220,placeholder_text='Rate')
    entryemi.place(x=50,y=150)
    entryemi3=customtkinter.CTkEntry(master=frameemi,width=220,placeholder_text='Time Duration')
    entryemi3.place(x=50,y=190)
    emi2=customtkinter.CTkLabel(master=frameemi,text='Loan Amount:{}'.format(gc),font=('Century Gothic', 16))
    emi2.place(x=50,y=110)
    action4=partial(emi_calculator2,gc)
    buttonemi=customtkinter.CTkButton(master=frameemi,text='Calculate',command=action4)
    buttonemi.place(x=100,y=230)
    win10.mainloop()
def emi_calculator2(P):#EMI CALCULATOR
    global entryemi
    global entryemi3
    global EMI2
    global N2
    R2=int(entryemi.get())/1200
    N2=int(entryemi3.get())
    EMI2 = P * R2 * (((1+R2)**N2)/(((1+R2)**N2)-1))
    i=0;flag=False
    while i<3 and flag==False:
        try:
            L1[i].index(P)
        except:
            i+=1
        else:
            p=i
            flag=True
    if p==0:
        goal_emi1()
    elif p==1:
        goal_emi2()
    elif p==2:
        goal_emi3()
    return EMI2
def goal_emi1():#PLAN IF THEY TAKE EMI FOR PRIMARY GOAL
    global emi1
    global L1
    global iden
    global EMI2
    global N2
    f.execute("select sav from personal_info where id={}".format(iden))
    d=f.fetchall()
    sav=d[0][0]
    savings2=sav-EMI2
    if savings2<=0:
        emi1.configure(text="Sorry your goal value is too high so you will not be able to achieve all the goals.Change your goal or increase time period of emi.Reset values.")
    else:
        ma1=0.55*savings2
        ma2=0.45*savings2
        t1=round(L1[1][2]/ma1,3)
        t2=round(L1[2][2]/ma2,3)
        if t1>=60 or t2>=60:
            emi1.configure(text='With the high cost of emi for primary goal it will take a very long time to achieve other goals. Increase time period of emi')
        else:
            f.execute("update personal_info set sav={} where id={}".format(savings2,iden))
            dp = customtkinter.CTkToplevel()
            dp.geometry('600x450')
            dp.title('Financial Plan Page')
            dp.attributes('-topmost', True)
            patt_6= customtkinter.CTkImage(Image.open("ASSETS/Financial Plan.jpg"),size=(600, 450))
            dp1= customtkinter.CTkLabel(master=dp, image=patt_6)
            dp1.pack()
            frame2 = customtkinter.CTkFrame(master=dp, width=500, height=500)
            frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            dpt= customtkinter.CTkLabel(master=frame2, text='Your Financial Plan', font=('Century Gothic', 25,'underline'))
            dpt.place(x=10, y=30)
            dpt1= customtkinter.CTkLabel(master=frame2, text='{}'.format(L1[0][1]),font=('Century Gothic', 20, 'bold'))
            dpt1.place(x=10, y=80)
            dpt2= customtkinter.CTkLabel(master=frame2, text='Time :{}'.format(N2), font=('Century Gothic', 15))
            dpt2.place(x=10, y=120)
            dpt3= customtkinter.CTkLabel(master=frame2, text='Monthly Requirement :{}'.format(EMI2), font=('Century Gothic', 15))
            dpt3.place(x=200, y=120)
            dpt4= customtkinter.CTkLabel(master=frame2, text='{}'.format(L1[1][1]), font=('Century Gothic', 20, 'bold'))
            dpt4.place(x=10, y=200)
            dpt5= customtkinter.CTkLabel(master=frame2, text='Time :{}'.format(t1), font=('Century Gothic', 15))
            dpt5.place(x=10, y=240)
            dpt6= customtkinter.CTkLabel(master=frame2, text='Monthly Requirement :{}'.format(ma1), font=('Century Gothic', 15))
            dpt6.place(x=200, y=240)
            dpt7= customtkinter.CTkLabel(master=frame2, text='{}'.format(L1[2][1]), font=('Century Gothic', 20, 'bold'))
            dpt7.place(x=10, y=320)
            dpt8= customtkinter.CTkLabel(master=frame2, text='Time :{}'.format(t2), font=('Century Gothic', 15))
            dpt8.place(x=10, y=360)
            dpt9= customtkinter.CTkLabel(master=frame2, text='Monthly Requirement :{}'.format(ma2), font=('Century Gothic', 15))
            dpt9.place(x=200, y=360)
            dp.mainloop()
            f.execute("update goals_{} set mc={} where prior={}".format(iden,EMI2,1))
            f.execute("update goals_{} set mc={} where prior={}".format(iden,ma1,2))
            f.execute("update goals_{} set mc={} where prior={}".format(iden,ma2,3))
            f.execute("update goals_{} set time={} where prior={}".format(iden,N2,1))
            f.execute("update goals_{} set time={} where prior={}".format(iden,t1,2))
            f.execute("update goals_{} set time={} whereprior={}".format(iden,t2,3))
    sqlobj.commit()
def goal_emi2():#PLAN IF THEY TAKE EMI FOR SECONDARY GOAL
    global emi1
    global L1
    global iden
    f.execute("select sav from personal_info where id={}".format(iden))
    d=f.fetchall()
    sav=d[0][0]
    global EMI2
    global N2
    savings2=sav-EMI2
    if savings2<=0:
        emi1.configure(text="Sorry your goal value is too high so you will not be able to achieve all the goals.Change your goal or increase time period of emi.Reset values.")
    else:
        ma1=0.55*savings2
        ma2=0.45*savings2
        t1=round(L1[0][2]/ma1,3)
        t2=round(L1[2][2]/ma2,3)
        if t1>=60 or t2>=60:
            emi1.configure(text='With the high cost of emi for primary goal it will take a very long time to achieve other goals.Change your goal or increase time period of emi')
        else:
            f.execute("update personal_info set sav={} where id={}".format(savings2,iden))
    dp = customtkinter.CTkToplevel()
    dp.geometry('600x450')
    dp.title('Financial Plan Page')
    dp.attributes('-topmost', True)
    patt_6= customtkinter.CTkImage(Image.open("ASSETS/Financial Plan.jpg"),size=(600, 450))
    dp1.pack()
    dp1= customtkinter.CTkLabel(master=dp, image=patt_6)
    frame2 = customtkinter.CTkFrame(master=dp1, width=500,height=500)
    frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    dpt= customtkinter.CTkLabel(master=frame2, text='Your Financial Plan', font=('Century Gothic', 25,'underline'))
    dpt.place(x=10, y=30)
    dpt1= customtkinter.CTkLabel(master=frame2, text='{}'.format(L1[1][1]),font=('Century Gothic', 20, 'bold'))
    dpt1.place(x=10, y=80)
    dpt2= customtkinter.CTkLabel(master=frame2, text='Time :{}'.format(N2), font=('Century Gothic', 15))
    dpt2.place(x=10, y=120)
    dpt3= customtkinter.CTkLabel(master=frame2, text='Monthly Requirement :{}'.format(EMI2), font=('Century Gothic', 15))
    dpt3.place(x=200, y=120)
    dpt4= customtkinter.CTkLabel(master=frame2, text='{}'.format(L1[0][1]), font=('Century Gothic', 20, 'bold'))
    dpt4.place(x=10, y=200)
    dpt5= customtkinter.CTkLabel(master=frame2, text='Time :{}'.format(t1), font=('Century Gothic', 15))
    dpt5.place(x=10, y=240)
    dpt6= customtkinter.CTkLabel(master=frame2, text='Monthly Requirement :{}'.format(ma1), font=('Century Gothic', 15))
    dpt6.place(x=200, y=240)
    dpt7= customtkinter.CTkLabel(master=frame2, text='{}'.format(L1[2][1]), font=('Century Gothic', 20, 'bold'))
    dpt7.place(x=10, y=320)
    dpt8= customtkinter.CTkLabel(master=frame2, text='Time :{}'.format(t2), font=('Century Gothic', 15))
    dpt8.place(x=10, y=360)
    dpt9= customtkinter.CTkLabel(master=frame2, text='Monthly Requirement :{}'.format(ma2), font=('Century Gothic', 15))
    dpt9.place(x=200, y=360)
    dp.mainloop()
    f.execute("update goals_{} set mc={} where prior={}".format(iden,EMI2,2))
    f.execute("update goals_{} set mc={} where prior={}".format(iden,ma1,1))
    f.execute("update goals_{} set mc={} where prior={}".format(iden,ma2,3))
    f.execute("update goals_{} set time={} where prior={}".format(iden,N2,2))
    f.execute("update goals_{} set time={} where prior={}".format(iden,t1,1))
    f.execute("update goals_{} set time={} where prior={}".format(iden,t2,3))
    sqlobj.commit()
def goal_emi3():#PLAN IF THEY TAKE EMI FOR TERTIARY GOAL
    global emi1
    global L1
    global iden
    f.execute("select sav from personal_info where id={}".format(iden))
    d=f.fetchall()
    sav=d[0][0]
    global EMI2
    global N2
    savings2=sav-EMI2
    if savings2<=0:
        emi1.configure(text="Sorry your goal value is too high so you will not be able to achieve all the goals.Change your goal or increase time period of emi.Reset values.")
    else:
        ma1=0.55*savings2
        ma2=0.45*savings2
        t1=round(L1[0][2]/ma1,3)
        t2=round(L1[1][2]/ma2,3)
        if t1>=60 or t2>=60:
            emi1.configure(text='With the high cost of emi for primary goal it will take a very long time to achieve other goals.Change your goal or increase time period of emi')
        else:
            f.execute("update personal_info set sav={} where id={}".format(savings2,iden))
            dp = customtkinter.CTkToplevel()
            dp.geometry('600x450')
            dp.title('Financial Plan Page')
            dp.attributes('-topmost', True)
            patt_6= customtkinter.CTkImage(Image.open("ASSETS/Financial Plan.jpg"),size=(600, 450))
            dp1= customtkinter.CTkLabel(master=dp, image=patt_6)
            dp1.pack()
            frame2 = customtkinter.CTkFrame(master=dp1, width=500,height=500)
            frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            dpt= customtkinter.CTkLabel(master=frame2, text='Your Financial Plan', font=('Century Gothic', 25,'underline'))
            dpt.place(x=10, y=30)
            dpt1= customtkinter.CTkLabel(master=frame2, text='{}'.format(L1[2][1]) ,font=('Century Gothic', 20, 'bold'))
            dpt1.place(x=10, y=80)
            dpt2= customtkinter.CTkLabel(master=frame2, text='Time :{}'.format(N2), font=('Century Gothic', 15))
            dpt2.place(x=10, y=120)
            dpt3= customtkinter.CTkLabel(master=frame2, text='Monthly Requirement :{}'.format(EMI2), font=('Century Gothic', 15))
            dpt3.place(x=200, y=120)
            dpt4= customtkinter.CTkLabel(master=frame2, text='{}'.format(L1[0][1]), font=('Century Gothic', 20, 'bold'))
            dpt4.place(x=10, y=200)
            dpt5= customtkinter.CTkLabel(master=frame2, text='Time :{}'.format(t1), font=('Century Gothic', 15))
            dpt5.place(x=10, y=240)
            dpt6= customtkinter.CTkLabel(master=frame2, text='Monthly Requirement :{}'.format(ma1), font=('Century Gothic', 15))
            dpt6.place(x=200, y=240)
            dpt7= customtkinter.CTkLabel(master=frame2, text='{}'.format(L1[1][1]), font=('Century Gothic', 20, 'bold'))
            dpt7.place(x=10, y=320)
            dpt8= customtkinter.CTkLabel(master=frame2, text='Time :{}'.format(t2), font=('Century Gothic', 15))
            dpt8.place(x=10, y=360)
            dpt9= customtkinter.CTkLabel(master=frame2, text='Monthly Requirement :{}'.format(ma2), font=('Century Gothic', 15))
            dpt9.place(x=200, y=360)
            dp.mainloop()
            f.execute("update goals_{} set mc={} where prior={}".format(iden,EMI2,3))
            f.execute("update goals_{} set mc={} where prior={}".format(iden,ma1,1))
            f.execute("update goals_{} set mc={} where prior={}".format(iden,ma2,2))
            f.execute("update goals_{} set time={} where prior={}".format(iden,N2,3))
            f.execute("update goals_{} set time={} where prior={}".format(iden,t1,1))
            f.execute("update goals_{} set time={} where prior={}".format(iden,t2,2))
            sqlobj.commit()
def emi_page():#CALCULATES EMI FOR HOME PAGE
    global entry_emi
    global entry_emi2
    global entry_emi3
    global emi_2
    win4=customtkinter.CTkToplevel()
    win4.geometry('600x450')
    win4.title('EMI')
    win4.attributes('-topmost',True)
    win3.attributes('-topmost',False)
    patt5=customtkinter.CTkImage(Image.open("ASSETS/EMI_Calculator.png"),size=(600, 450))
    l_1=customtkinter.CTkLabel(master=win4, image=patt5,text=None)
    l_1.pack()
    frame_emi=customtkinter.CTkFrame(master=l_1,width=320,height=360)
    frame_emi.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    emi_1=customtkinter.CTkLabel(master=frame_emi,text='EMI Calculator',font=('Century Gothic', 20))
    emi_1.place(x=50,y=50)
    entry_emi=customtkinter.CTkEntry(master=frame_emi,width=220,placeholder_text='Rate')
    entry_emi.place(x=50,y=110)
    entry_emi2=customtkinter.CTkEntry(master=frame_emi,width=220,placeholder_text='Principal Amount')
    entry_emi2.place(x=50,y=150)
    entry_emi3=customtkinter.CTkEntry(master=frame_emi,width=220,placeholder_text='Time Duration')
    entry_emi3.place(x=50,y=190)
    emi_2=customtkinter.CTkLabel(master=frame_emi,text='EMI:',font=('Century Gothic', 16))
    emi_2.place(x=50,y=280)
    button_emi=customtkinter.CTkButton(master=frame_emi,text='Calculate',command=emi_calculator)
    button_emi.place(x=50,y=230)
    win4.mainloop()
def emi_calculator():
    global entry_emi
    global entry_emi2
    global entry_emi3
    global emi_2
    R=float(entry_emi.get())/1200
    N=int(entry_emi3.get())
    P=int(entry_emi2.get())
    EMI = P * R * (((1+R)**N)/(((1+R)**N)-1))
    emi_2.configure(text="Loan Amount:{}".format(EMI))
login_page()