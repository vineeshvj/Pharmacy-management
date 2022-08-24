from cProfile import label
from cgitb import text
from faulthandler import disable
from os import stat
import random
import string
import time
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.messagebox
from tkinter.tix import COLUMN

class Doctor():
    def __init__(self,root):
        self.root = root
        self.root.title("Doctor Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background = "black")

        ######### Declareing all func together ############
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        DrId = StringVar()
        Drname  =  StringVar()
        DateofBirth =  StringVar()
        spes  =  StringVar()
        Govtpri  =  StringVar()
        Surgeries =  StringVar()
        Experiences  =  StringVar()
        Nurses  =  StringVar()
        DrMobile  =  StringVar()
        PtName  =  StringVar()
        Apptime  =  StringVar()
        PtAge = StringVar()
        PatientAddress =  StringVar()
        PtMobile  =  StringVar()
        Disease  =  StringVar()
        Case  =  StringVar()
        BenefitCard = StringVar()

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Doctor Management System", "Are you sure you want to exit ?")
            if exitbtn > 0:
                root.destroy()
            return

        def resetfunc():
            DrId.set("")
            Drname.set("")  
            DateofBirth.set("")
            spes.set("")
            Govtpri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0",END)
            return

        def deletefunc():
            DrId.set("")
            Drname.set("")  
            DateofBirth.set("")
            spes.set("")
            Govtpri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return

        def Patient_idFunc():
            ranumber = random.randint(10000,999999)
            randomnumber = str(ranumber)
            DrId.set(randomnumber)  

        def prescriptiondatafunc(): 
            Patient_idFunc()
            TextPrescriptionData.config(state = NORMAL)
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+DrId.get()+"\t"+Drname.get()+"\t"+DateofBirth.get()+"\t\t"+ spes.get()+"\t\t"+Govtpri.get()+"\t\t"+Surgeries.get()+"\t\t"+Experiences.get()+"\t\t"+Nurses.get()+"\t"+DrMobile.get()+"\t\t"+PtName.get()+"\t\t"+Case.get()+"\t"+PtAge.get()+"\n")           
            TextPrescriptionData.config(state = DISABLED)
            return

        def prescriptionfunc():
            Patient_idFunc()
            TextPrescription.config(state = NORMAL)
            TextPrescription.insert(END,"Date: \t\t"+Date_of_Registration.get()+"\n")
            TextPrescription.insert(END,"Date: \t\t"+PtName.get()+"\n")
            TextPrescription.insert(END,"Date: \t\t"+Apptime.get()+"\n")
            TextPrescription.insert(END,"Date: \t\t"+PtAge.get()+"\n")
            TextPrescription.insert(END,"Date: \t\t"+PatientAddress.get()+"\n")
            TextPrescription.insert(END,"Date: \t\t"+Disease.get()+"\n")
            TextPrescription.insert(END,"Date: \t\t"+Case.get()+"\n")
            TextPrescription.insert(END,"Date: \t\t"+BenefitCard.get()+"\n")
            TextPrescription.insert(END,"Date: \t\t"+Drname.get()+"\n")
            TextPrescription.insert(END,"Date: \t\t"+DrMobile.get()+"\n")
            TextPrescription.config(state = DISABLED)
            return    

        ######## Tite Label ####################
        title = Label(self.root  ,text = "Doctor Management System", font = ("monotype corsiva",42,"bold"),bd = 5,
            relief = GROOVE , bg = "#b7d8d6", fg = "black")
        title.pack(side = TOP , fill = X)

        ##### FRAME ######
        Manage_Frame = Frame(self.root , width = 1510 , height = 400 , bd = 5 , relief = RIDGE , bg = "#789e9e")
        Manage_Frame.place(x=10,y=80)

        Button_Frame = Frame(self.root , width = 1510 , height = 55 , bd = 4 , relief = RIDGE , bg = "#eef3db")
        Button_Frame.place(x=10,y=460)

        Data_Frame = Frame(self.root , width = 1510 , height = 270 , bd = 4 , relief = RIDGE , bg = "#eef3db")
        Data_Frame.place(x=10,y=510)

        Data_FrameLeft = LabelFrame(Manage_Frame , width = 1050 , text = "General Information",
        font = ("arial",20,"italic bold"), height = 390 , bd = 7 , pady=1 , relief = RIDGE , bg="#789e9e")
        Data_FrameLeft.pack(side = LEFT)

        Data_FrameData = LabelFrame(Data_Frame , width = 1050 , text = "Doctor's Details",
        font = ("arial",12,"italic bold"), height = 390 , bd = 7 ,  relief = RIDGE , bg="#b7d8d6")
        Data_FrameData.pack(side = LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame , width = 1050 , text = "Patient Information",
        font = ("arial",15,"italic bold"), height = 390 , bd = 7 ,  relief = RIDGE , bg="#789e9e")
        Data_FrameRight.pack(side = RIGHT)

        ######### Doctor's ID ##########

        DrIdlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20,text= "Doctor ID" , bg="#789e9e")
        DrIdlbl.grid(row= 0 , column = 0 , padx = 10, pady = 5 , sticky = W)
        DrIdtxt = Entry(Data_FrameLeft , font =("arial",12,"bold"),width = 27 , state = DISABLED,textvariable = DrId)
        DrIdtxt.grid(row = 0 , column = 1, padx = 10 , pady = 5 , sticky = E)

        DrNamelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20,text= "Doctor Name" , bg="#789e9e")
        DrNamelbl.grid(row= 1 , column = 0 , padx = 10, pady = 5 , sticky = W)
        DrNametxt = Entry(Data_FrameLeft , font =("arial",12,"bold"),width = 27 , textvariable = Drname)
        DrNametxt.grid(row = 1 , column = 1, padx = 10 , pady = 5 , sticky = E)

        Dateofbirthlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20,text= "Date of birth" , bg="#789e9e")
        Dateofbirthlbl.grid(row= 2 , column = 0 , padx = 10, pady = 5 , sticky = W)
        Dateofbirthtxt = Entry(Data_FrameLeft , font =("arial",12,"bold"),width = 27 ,textvariable = DateofBirth)
        Dateofbirthtxt.grid(row = 2 , column = 1, padx = 10 , pady = 5 , sticky = E)

        Speslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20,text= "Specialsation" , bg="#789e9e")
        Speslbl.grid(row= 3 , column = 0 , padx = 10, pady = 5 , sticky = W)
        Spestxt = Entry(Data_FrameLeft , font =("arial",12,"bold"),width = 27 , textvariable = spes)
        Spestxt.grid(row = 3 , column = 1, padx = 10 , pady = 5 , sticky = E)

        GovtPrlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20,text= "Gov/Private" , bg="#789e9e")
        GovtPrlbl.grid(row= 4 , column = 0 , padx = 10, pady = 5 , sticky = W)
        Govtpricmb = ttk.Combobox(Data_FrameLeft , textvariable = Govtpri , width = 25 , state = "readonly",
        font = ("arial",12,"bold"))
        Govtpricmb['values'] = ("","Government","Private")
        Govtpricmb.current(0)
        Govtpricmb.grid(row = 4 , column = 1, padx = 10 , pady = 5 , sticky = E)

        Surgerieslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20,text= "Surgeries" , bg="#789e9e")
        Surgerieslbl.grid(row= 5 , column = 0 , padx = 10, pady = 5 , sticky = W)
        Surgeriestxt = Entry(Data_FrameLeft , font =("arial",12,"bold"),width = 27 , textvariable = Surgeries)
        Surgeriestxt.grid(row = 5 , column = 1, padx = 10 , pady = 5 , sticky = E)

        Experiencelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20,text= "Experience" , bg="#789e9e")
        Experiencelbl.grid(row= 6 , column = 0 , padx = 10, pady = 5 , sticky = W)
        Experiencetxt = Entry(Data_FrameLeft , font =("arial",12,"bold"),width = 27 , textvariable = Experiences)
        Experiencetxt.grid(row = 6 , column = 1, padx = 10 , pady = 5 , sticky = E)

        Nurseslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20,text= "Nurses under Dr" , bg="#789e9e")
        Nurseslbl.grid(row= 7 , column = 0 , padx = 10, pady = 5 , sticky = W)
        Nursestxt = Entry(Data_FrameLeft , font =("arial",12,"bold"),width = 27 , textvariable = Nurses)
        Nursestxt.grid(row = 7 , column = 1, padx = 10 , pady = 5 , sticky = E)

        DrMobilelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20,text= "Doctor Mobile No." , bg="#789e9e")
        DrMobilelbl.grid(row= 8 , column = 0 , padx = 10, pady = 5 , sticky = W)
        DrMobiletxt = Entry(Data_FrameLeft , font =("arial",12,"bold"),width = 27 , textvariable =DrMobile )
        DrMobiletxt.grid(row = 8 , column = 1, padx = 10 , pady = 5 , sticky = E)

        Datelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20, text = "Date", padx = 2,bg = "#789e9e")
        Datelbl.grid(row= 0 , column=2 , padx= 10 , pady= 5 , sticky = W)

        Datetxt = Entry(Data_FrameLeft,font =("arial",12,"bold"),width = 27,textvariable= Date_of_Registration)
        Datetxt.grid(row=0 , column=3, padx=10 , pady= 5, sticky= E)

        PtNamelbl = Label(Data_FrameLeft, font=("arial",12,"bold"),width= 20 , text="Patient Name",padx=2,
        bg="#789e9e")
        PtNamelbl.grid(row= 1, column=2,padx= 10 ,pady= 5 , sticky= W )
        PtNametxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width= 27, textvariable= PtName)
        PtNametxt.grid(row= 1 , column= 3 , padx= 10 , pady= 5 , sticky= E)

        Apptimelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width= 20 , text= "Appointment Time",padx= 2, bg = "#789e9e")
        Apptimelbl.grid(row= 2 , column= 2, padx= 10 , pady= 5 , sticky= W)
        Apptimetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width= 27 , textvariable = Apptime)
        Apptimetxt.grid(row= 2, column= 3, padx = 10 , pady = 5, sticky = E) 

        PtAgelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width= 20 , text= "Patient Age",padx= 2, bg = "#789e9e")
        PtAgelbl.grid(row= 3 , column= 2, padx= 10 , pady= 5 , sticky= W)
        PtAgetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width= 27 , textvariable = PtAge)
        PtAgetxt.grid(row= 3, column= 3, padx = 10 , pady = 5, sticky = E)

        PtAddresslbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width= 20 , text= "Pateint Address",padx= 2, bg = "#789e9e")
        PtAddresslbl.grid(row= 4 , column= 2, padx= 10 , pady= 5 , sticky= W)
        PtAddresstxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width= 27 , textvariable = PatientAddress)
        PtAddresstxt.grid(row= 4, column= 3, padx = 10 , pady = 5, sticky = E)

        PtMobilelbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width= 20 , text= "Patient Mobile No",padx= 2, bg = "#789e9e")
        PtMobilelbl.grid(row= 5 , column= 2, padx= 10 , pady= 5 , sticky= W)
        PtMobiletxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width= 27 , textvariable = PtMobile)
        PtMobiletxt.grid(row= 5, column= 3, padx = 10 , pady = 5, sticky = E)

        Diseaselbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width= 20 , text= "Pateint Disease",padx= 2, bg = "#789e9e")
        Diseaselbl.grid(row= 6 , column= 2, padx= 10 , pady= 5 , sticky= W)
        Diseasetxt = Entry(Data_FrameLeft,font=("arial",12,"bold"),width= 27 , textvariable = Disease)
        Diseasetxt.grid(row= 6, column= 3, padx = 10 , pady = 5, sticky = E)

        Caselbl = Label(Data_FrameLeft,font=("arial",12,"bold"),width= 20 , text= "Case",padx= 2, bg = "#789e9e")
        Caselbl.grid(row= 7 , column= 2, padx= 10 , pady= 5 , sticky= W)
        Casecmb = ttk.Combobox(Data_FrameLeft, textvariable = Case, width= 25, state = "readonly",
        font = ("arial",12,"bold"))
        Casecmb['values'] = ("","New Case","Old Case")
        Casecmb.current(0)
        Casecmb.grid(row= 7, column= 3, padx = 10 , pady = 5, sticky = E)

        BenefitCardlbl = Label(Data_FrameLeft, font = ("arial",12,"bold"),text= "Benefit Card", width= 20 , pady = 10 ,
        bg= "#789e9e")
        BenefitCardlbl.grid(row = 8 , column = 2 , sticky = W)

        BenefitCardcmb = ttk.Combobox(Data_FrameLeft, textvariable = BenefitCard, width = 25 , state = "readonly",
        font = ("arial",12,"bold"))
        BenefitCardcmb['value'] = ("","Ayushman Card","Health Insurance","Senior Citizen","Army Card")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row = 8, column = 3, padx= 10 , sticky = E)

        ###################### Text Prescription ###################

        TextPrescription = Text(Data_FrameRight , font = ("arial",12,"bold"),width = 55 , height = 17 , padx = 3, 
        pady = 5,state = DISABLED)
        TextPrescription.grid(row= 0, column= 0)
        TextPrescriptionData = Text(Data_FrameData , font = ("arial",12,"bold"),width = 203 , height = 12,state = DISABLED)
        TextPrescriptionData.grid(row= 1, column= 0)

            ################### Button ###################
        Prescriptionbtn = Button(Button_Frame, text = "Patient Informtion", bg = "#fe615a", activebackground = "#cc6686",
        font = ("arial",15,"bold"),width = 22 , command = prescriptionfunc)
        Prescriptionbtn.grid(row = 0 , column = 0 , padx = 15)

        DoctorDetailbtn = Button(Button_Frame, text = "Doctor Details", bg = "#fe615a", activebackground = "#cc6686",
        font = ("arial",15,"bold"),width = 22 , command = prescriptiondatafunc)
        DoctorDetailbtn.grid(row = 0 , column = 1 , padx = 15)

        Resetbtn = Button(Button_Frame, text = "Reset", bg = "#fe615a", activebackground = "#cc6686",
        font = ("arial",15,"bold"),width = 22, command= resetfunc)
        Resetbtn.grid(row = 0 , column = 2 , padx = 15)

        Deletebtn = Button(Button_Frame, text = "Delete", bg = "#fe615a", activebackground = "#cc6686",
        font = ("arial",15,"bold"),width = 22, command = deletefunc)
        Deletebtn.grid(row = 0 , column = 3 , padx = 15)

        Exitbtn = Button(Button_Frame, text = "Exit", bg = "#fe615a", activebackground = "#cc6686",
        font = ("arial",15,"bold"),width = 22, command = exitbtn)
        Exitbtn.grid(row = 0 , column = 4 , padx = 15)

        Prescriptiondatarow = Label(Data_FrameData , bg = "white" , font = ("arial",12,"bold"),
        text = "Data\tDoctor Id\tDoctor Name\tDate of Birth\tSpecialisation\tGovt/Private\tSurgeries\tExperience\tNurses\tDr Mobile\tPatient Name\tCase\tPt. age")
        Prescriptiondatarow.grid(row = 0, column = 0 , sticky = W)



class Registration:
    def __init__(self,root):
        self.root  = root  
        self.root.title("Patient Registration system")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background = "black")   


        ########## live  time date by module #########
         
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        Mobile_no = StringVar()
        pincode = StringVar()
        Address = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
       
        ### var1,2,3,4,5 are fpr combobox
       
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()   #we will keep int ,we will keep here numerical value 


        Membership =  StringVar()
        Membership.set("0")  #when memebership os inclicked or reset has been done 

        #################   fuction  ################################
       
        def exitbtt():
            exitbtt = tkinter.messagebox.askyesno("Member Registration Form","Are you sure you want to exit ?")
            if exitbtt > 0:
                root.destroy()
            else:
                self.app = Toplevel(self.master)
                self.app =  Registration(self.newWindow)   
            return

        def resetbtt(): 
            Firstname.set("") 
            Ref.set("") 
            Mobile_no.set("") 
            pincode.set("") 
            Address.set("")  
            Lastname.set("")
            var1.set("")
            var2.set("") 
            var3.set("")
            var4.set("") 
            var5.set("") 
            Membership.set("0")
            member_gendercmb.current(0)     
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt(state = DISABLED)

        def reeesetbtt():
            reeesetbtt = tkinter.messagebox.askokcancel("member Regestration form","you want to add as new record")
            if reeesetbtt > 0:
                resetbtt()
            elif reeesetbtt <= 0:
                detail_labeltxt.delete("1.0", END)
            return     

        def Reference_number():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)  

        def membership_fees():
            if(var5.get() == 1):   #when checkbox is clicled 
                member_membershiptxt.configure(state = NORMAL)
                item = float(15000)   #random price    
                Membership.set(str(item)+"Rs")
            elif(var5.get() == 0):
                #when unclicked
                Membership.set("0")
                member_membershiptxt.configure(state = DISABLED)
                

        def Receipt():
            Reference_number()
            detail_labeltxt.insert(END,"\t" +Date_of_Registration.get()+ "    \t" + Ref.get() + "\t\t" +
            Firstname.get() + '     \t'+ Lastname.get()+ "\t " + Mobile_no.get() + "    \t" +
            '\t\t' + Address.get() + "     \t\t" + pincode.get() + "   \t" + member_gendercmb.get() +
            "   \t\t" + Membership.get() + "\n")



        ############### TITLE########################################
        title = Label(self.root, text = "Member Registration From", font = ("monotyepe corsiva",30,"bold"),bd = 5,
            relief = GROOVE,bg ="#E6005C", fg = "#000000")
        title.pack(side=TOP,fill = X ) 

        ###################### MEMBER FRAME ##########################
        manage_Frame = Frame(self.root , bd = 4, relief = RIDGE , bg = "#001a66")
        manage_Frame.place(x=20,y=100,width=450,height = 630)

        ####### text , label , comboboxes in manage frame #############
        Cus_title =Label(manage_Frame,text = "Customer Details", font = ("arail",20,"bold"),bg = "#001a66",fg = "white")
        Cus_title.grid(row =0 , columnspan= 2 , pady = 5 ) 

        member_datelbl = Label(manage_Frame,text = "Date",font = ("arial",15,"bold"),bg = "#001a66" , fg = "white")
        member_datelbl.grid(row = 1 , column = 0 ,padx = 10 , sticky = "w") 




        member_datetxt = Entry(manage_Frame, font= ("arail",15,"bold"), textvariable = Date_of_Registration)
        member_datetxt.grid(row = 1,column = 1 , pady = 5, padx = 10 , sticky = "w") 

        memeber_reflbl = Label(manage_Frame,text= "Reference ID", font = ("arial",15,"bold"),bg = "#001a66",
        fg = "white")
        memeber_reflbl.grid(row = 2 , column = 0 , pady = 5 , padx = 10 , sticky= "w")

        member_reftxt = Entry(manage_Frame, font= ("arail",15,"bold"), state = DISABLED , text = Ref)
        member_reftxt.grid(row = 2,column = 1 , pady = 5, padx = 10 , sticky = "w") 


        member_fnamelbl = Label(manage_Frame,text = "First Name",font = ("arial",15,"bold"),bg = "#001a66" , fg = "white")
        member_fnamelbl.grid(row = 3 , column = 0 ,padx = 10 , sticky = "w") 


        member_fnametxt = Entry(manage_Frame, font= ("arail",15,"bold"), textvariable = Firstname)
        member_fnametxt.grid(row = 3,column = 1 , pady = 5, padx = 10 , sticky = "w") 

        member_lnamelbl = Label(manage_Frame,text = "Last Name",font = ("arial",15,"bold"),bg = "#001a66" , fg = "white")
        member_lnamelbl.grid(row = 4 , column = 0 ,padx = 10 , sticky = "w") 


        member_lnametxt = Entry(manage_Frame, font= ("arail",15,"bold"), textvariable = Lastname)
        member_lnametxt.grid(row = 4,column = 1 , pady = 5, padx = 10 , sticky = "w") 


        member_mobilelbl = Label(manage_Frame,text = "Mobile No",font = ("arial",15,"bold"),bg = "#001a66" , fg = "white")
        member_mobilelbl.grid(row = 5 , column = 0 ,padx = 10 , sticky = "w") 


        member_mobiletxt = Entry(manage_Frame, font= ("arail",15,"bold"), textvariable = Mobile_no)
        member_mobiletxt.grid(row = 5 ,column = 1 , pady = 5, padx = 10 , sticky = "w") 


        member_addresslbl = Label(manage_Frame,text = "Address",font = ("arial",15,"bold"),bg = "#001a66" , fg = "white")
        member_addresslbl.grid(row = 6 , column = 0 ,padx = 10 , sticky = "w") 


        member_addresstxt = Entry(manage_Frame, font= ("arail",15,"bold"), textvariable = Address )
        member_addresstxt.grid(row = 6,column = 1 , pady = 5, padx = 10 , sticky = "w") 


        member_pincodelbl = Label(manage_Frame,text = "Pin code",font = ("arial",15,"bold"),bg = "#001a66" , fg = "white")
        member_pincodelbl.grid(row = 7 , column = 0 ,padx = 10 , sticky = "w") 


        member_pincodetxt = Entry(manage_Frame, font= ("arail",15,"bold"), textvariable = pincode)
        member_pincodetxt.grid(row = 7,column = 1 , pady = 5, padx = 10 , sticky = "w") 


        member_genderlbl = Label(manage_Frame,text = "Gender",font = ("arial",15,"bold"),bg = "#001a66" , fg = "white")
        member_genderlbl.grid(row = 8 , column = 0 ,padx = 10 , sticky = "w") 

        member_gendercmb = ttk.Combobox(manage_Frame, text = var4 ,  state = "readonly", font = ("arail",15,"bold"),
        width = 19)
        member_gendercmb['values'] = ("","Male","Female","Other")
        member_gendercmb.current(0) #when nothing it will be empty ,given  at index 0
        member_gendercmb.grid( row = 8 , column = 1 , pady = 5 , padx = 10 ,  sticky = "w")



        member_id_prooflbl = Label(manage_Frame,text = "ID Proof",font = ("arial",15,"bold"),bg = "#001a66" , fg = "white")
        member_id_prooflbl.grid(row = 9 , column = 0 ,padx = 10 , sticky = "w") 

        member_id_proofcmb = ttk.Combobox(manage_Frame, text = var3 ,  state = "readonly", font = ("arail",15,"bold"),
        width = 19)
        member_id_proofcmb['values'] = ("","Adhaar Card","Passport","Driving License", "Pan Card","Student ID")
        member_id_proofcmb.current(0) #when nothing it will be empty ,given  at index 0
        member_id_proofcmb.grid( row = 9 , column = 1 , pady = 5 , padx = 10 ,  sticky = "w")



        member_memtypelbl = Label(manage_Frame,text = "Member Type",font = ("arial",15,"bold"),bg = "#001a66" , fg = "white")
        member_memtypelbl.grid(row = 10 , column = 0 ,padx = 10 , sticky = "w") 

        member_memtypecmb = ttk.Combobox(manage_Frame, text = var2 ,  state = "readonly", font = ("arail",15,"bold"),
        width = 19)
        member_memtypecmb['values'] = ("","Ayushman Card","Insurance","Pay immediaitely", "pay when leaving")
        member_memtypecmb.current(0) #when nothing it will be empty ,given  at index 0
        member_memtypecmb.grid( row = 10 , column = 1 , pady = 5 , padx = 10 ,  sticky = "w")


        member_paymentwithlbl = Label(manage_Frame,text = "Gender",font = ("arial",15,"bold"),bg = "#001a66" , fg = "white")
        member_paymentwithlbl.grid(row = 11 , column = 0 ,padx = 10 , sticky = "w") 

        member_paymentwithcmb = ttk.Combobox(manage_Frame, text = var1 ,  state = "readonly", font = ("arail",15,"bold"),
        width = 19)
        member_paymentwithcmb['values'] = ("","Cash","Debit Card - Rupay","Debit Card - Visa", "Debit Card - Mastercard", "Credit Card", "Phonepe", "Googlepay", "Paytm")
        member_paymentwithcmb.current(0) #when nothing it will be empty ,given  at index 0
        member_paymentwithcmb.grid( row = 11 , column = 1 , pady = 5 , padx = 10 ,  sticky = "w")
        
        member_membership = Checkbutton(manage_Frame, text = "Membership Fees", variable = var5, onvalue = 1,
                    offvalue = 0, font = ("arial",15,"bold"), bg =  "#001a66",fg ="white", command = membership_fees )
        member_membership.grid(row = 12, column = 0, sticky = "w")
        member_membershiptxt = Entry(manage_Frame, font = ("arail",15,"bold"),state = DISABLED, justify = RIGHT,
                                        textvariable = Membership) 
        member_membershiptxt.grid(row = 12, column = 1, pady = 5, padx = 10, sticky = "w")                                           




        ################ DETAIL FRAME####################################
        detail_frame = Frame(self.root , bd = 4, relief = RIDGE , bg= "#001a66")
        detail_frame.place(x=500,y=100,width=820, height=630) 

        detail_label = Label(detail_frame, font = ("arail",11,"bold"),pady = 10,padx = 2 , width = 95,
            text = "Date\t Ref Id\t Firstname    Lastname    mobile No     Address     Pincode    Gender    Membership")
        detail_label.grid(row = 0, column = 0, columnspan = 4, sticky = "w")
        detail_labeltxt = Text(detail_frame, width = 123, height = 34, font = ("arial", 10 ))
        detail_labeltxt.grid(row = 1, column = 0, columnspan = 4)


       ########### Add button in detail frame ############################
 
        receiptbtn = Button(detail_frame, padx = 15, bd = 5, font = ("arail", 12 ,"bold"),
                    bg = "#ff9966", width = 20 , text = "Receipt", command =  Receipt )
        receiptbtn.grid(row = 2 , column = 0) 

        resetbtn = Button(detail_frame, padx = 15, bd = 5, font = ("arail", 12 ,"bold"),
                    bg = "#ff9966", width = 20 , text = "Reset", command = reeesetbtt )
        resetbtn.grid(row = 2 , column = 1) 

        exitbtn = Button(detail_frame, padx = 15, bd = 5, font = ("arail", 12 ,"bold"),
                    bg = "#ff9966", width = 20 , text = "Exit", command = exitbtt )
        exitbtn.grid(row = 2 , column = 2) 



def main():
    root = Tk()
    app = windows1(root)
    root.mainloop()

class windows1:
    def __init__(self,master):
        self.master=master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1350x750+0+0') #x-axis, y-axis,e,e are location from top leftmost
        self.frame=Frame(self.master)
        self.frame.pack()
        self.frame.configure(bg="#58c78d")
        self.master.configure(bg="#58c78d")

        self.Username = StringVar()
        self.password = StringVar()


        
        self.LableTitle = Label(self.frame,text = "    Pharmacy Management System   ",font = ("arial",40,"bold"),bd = 10,relief = "sunken")
        self.LableTitle.grid(row = 0 , column = 0 , columnspan = 2 , pady=20)    
       
        self.loginframe1 = Frame(self.frame, width = 1000, height = 300, bd = 10,relief = "groove" )
        self.loginframe1.grid(row=1 , column=0)

        self.loginframe2 = Frame(self.frame, width = 1000, height = 100, bd = 10, relief = "groove" )
        self.loginframe2.grid(row=2 , column=0, pady = 15)

        self.loginframe3 = Frame(self.frame, width = 1000, height = 200, bd = 10, relief = "groove" )
        self.loginframe3.grid(row=3 , column=0,pady = 5)

        self.button_reg = Button(self.loginframe3,text = "Patient Regristration Window",state = DISABLED,font = ("arail",15,"bold"),command = self.Registration_window)
        self.button_reg.grid(row = 0 , column = 0 , padx = 10 , pady = 10,columnspan = 2 )

        self.button_Hosp = Button(self.loginframe3,text = "Hosital Management Window",state = DISABLED,font = ("arail",15,"bold"), 
                           command = self.Hospital_window)
        self.button_Hosp.grid(row = 1 , column = 0 , padx = 10 , pady = 10 )

        self.button_Dr_appt = Button(self.loginframe3,text = "Doctor Management Window",state = DISABLED,font = ("arail",15,"bold"),
                           command = self.Dr_Apoint_window)
        self.button_Dr_appt.grid(row = 1 , column =1  , padx = 10 , pady = 10 )


        self.labelUsername = Label(self.loginframe1,text = "User Name", font = ("",20,"bold"),bd =3)
        self.labelUsername.grid(row = 0 , column = 0)

        self.textUsername = Entry(self.loginframe1,font = ("arial",20,"bold"), bd = 3, textvariable= self.Username)
        self.textUsername.grid(row = 0 , column = 1 , padx = 40 ,  pady = 15)

        self.labelPassword = Label(self.loginframe1,text = "password", font = ("arial",20,"bold"),bd =3 )
        self.labelPassword.grid(row = 1 , column = 0)

        self.textPassword = Entry(self.loginframe1,font = ("arial",20,"bold"),show = "*", bd = 3 , textvariable= self.password)
        self.textPassword.grid(row = 1 , column = 1 , padx = 40 ,  pady = 15)

        self.button_login = Button(self.loginframe2, text = "Login" , width = 20 , font = ("arial",18,"bold"),
                                command = self.login_system)
        self.button_login.grid(row = 0 , column = 0 , padx = 10 , pady = 10)

        self.button_Reset = Button(self.loginframe2, text = "Reset" , width = 20 , font = ("arial",18,"bold"),
                                command = self.reset_btn)
        self.button_Reset.grid(row = 0 , column = 3 , padx = 10 , pady = 10)

        self.button_Exit = Button(self.loginframe2, text = "Exit" , width = 20 , font = ("arial",18,"bold"),
                                command = self.Exit_btn)
        self.button_Exit.grid(row = 0 , column = 6 , padx = 10 , pady = 10)

    def login_system(self):                                
        user = self.Username.get()
        pswd = self.password.get()

        if(user == str("admin") and (pswd == str("admin"))):
            self.button_reg.config(state = NORMAL)
            self.button_Hosp.config(state = NORMAL)
            self.button_Dr_appt.config(state = NORMAL)
            self.button_med_stock.config(state = NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System", "You have entered an invalid user name or password")
            self.button_reg.config(state = DISABLED)
            self.button_Hosp.config(state = DISABLED)
            self.button_Dr_appt.config(state = DISABLED)
            self.button_med_stock.config(state = DISABLED) 


            self.Username.set("")
            self.password.set("")
            self.textUsername.focus()

    def reset_btn(self): 
        self.button_reg.config(state = DISABLED)
        self.button_Hosp.config(state = DISABLED)
        self.button_Dr_appt.config(state = DISABLED)
        self.button_med_stock.config(state = DISABLED)       
            # when we reset we haven't given correct user id and password
        self.Username.set("")
        self.password.set("")
        self.textUsername.focus()

    def Exit_btn(self):
        self.Exit_btn = tkinter.messagebox.askyesno("Pharmacy Management System", "Are you sure you want to exit? ")
        if self.Exit_btn > 0:
            #close that master screen 
           self.master.destroy()
           return


    def Registration_window(self):
        self.newwindow = Toplevel(self.master)
        self.app = Registration(self.newwindow)

    def Hospital_window(self):
        self.newwindow = Toplevel(self.master)
        self.app = Hospital(self.newwindow)

    def Dr_Apoint_window(self):
        self.newwindow = Toplevel(self.master)
        self.app = Doctor(self.newwindow)

  





class Hospital():
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0")    #Full screen (Maximum window)
        self.root.configure(background = "black")


    ##################### variable declaration #################
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        cmbTableName = StringVar()
        HospitalCode = StringVar()
        Number_of_Tablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInformation = StringVar()
        StorageAdvice = StringVar()
        Medication = StringVar()
        PatientId = StringVar()
        PatientNHnumber = StringVar()
        Patientname = StringVar()
        Dateofbirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        NHSnumber = StringVar()

        #######To generate Random Number automactically

        def Reference_numfunc():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def prescriptionfunc():
            Reference_numfunc()
            TextPresciption.insert(END,"Patient ID: \t\t"+PatientId.get()+"\n")
            TextPresciption.insert(END,"Patient Name: \t\t"+Patientname.get()+"\n")
            TextPresciption.insert(END,"Tablet: \t\t"+cmbTableName.get()+"\n")
            TextPresciption.insert(END,"Number of tablet: \t\t"+Number_of_Tablets.get()+"\n")
            TextPresciption.insert(END,"Daily Dose: \t\t"+DailyDose.get()+"\n")
            TextPresciption.insert(END,"Issued Date: \t\t"+IssuedDate.get()+"\n")
            TextPresciption.insert(END,"Expiry Date: \t\t"+ExpiryDate.get()+"\n")
            TextPresciption.insert(END,"Storage: \t\t"+StorageAdvice.get()+"\n")
            TextPresciption.insert(END,"More Information: \t\t"+MoreInformation.get()+"\n")
            return


        def prescriptiondatafunc():
            Reference_numfunc()
            TextPresciptionData.insert(END,Date_of_Registration.get()+"\t"+Ref.get()+"\t\t"
            +Patientname.get()+"\t\t"+Dateofbirth.get()+"\t\t"+NHSnumber.get()+"\t\t"+cmbTableName.get()+"\t"+
            Number_of_Tablets.get()+"\t\t"+IssuedDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t\t"+
            StorageAdvice.get()+"\t\t"+PatientId.get()+"\n")
            return     

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("hospital Magnagement System","Are you sure you want to exit ?")
            if exitbtn > 0:
                root.destroy()
                return   

        def deletefunc():          
            Ref.set("")
            cmbTableName.set("")
            HospitalCode.set("") 
            Number_of_Tablets.set("") 
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumber.set("")
            Patientname.set("") 
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPresciption.delete("1.0",END)   
            TextPresciptionData.delete("1.0",END) 
            return

        
        def resetfunc():
            Ref.set("")
            cmbTableName.set("")
            HospitalCode.set("") 
            Number_of_Tablets.set("") 
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumber.set("")
            Patientname.set("") 
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPresciption.delete("1.0",END)    
            return




    #################### TITLE ##################################
        title = Label(self.root, text = "Hospital Management System", font = ("monotype corsiva",42,"bold"),bd = 5,
              relief = GROOVE,bg = "#2eb8b8",fg = "black")
        title.pack(side = TOP , fill = X )      

     ######################### FRAME ###########################
        Manage_Frame = Frame(self.root,width = 1510 , height = 400 , bd = 5 , relief = RIDGE , bg = "#0099cc")
        Manage_Frame.place(x=10,y=80)

        Button_Frame = Frame(self.root, width =1510 , height = 55 , bd = 4 , relief = RIDGE , bg = "#328695")
        Button_Frame.place(x=10,y=460)

        Data_Frame = LabelFrame(self.root , width = 1510 , height = 270 , bd = 4 , relief = RIDGE , bg = "#266e73")
        Data_Frame.place(x=10,y=510)

        ###################### INNER FRAME ########################

        Data_FrameLeft = LabelFrame(Manage_Frame,width = 1050 , text = "General Information",
        font = ("arial",20,"bold"), height = 390 , bd = 7 , relief = RIDGE , bg="#0099cc")
        Data_FrameLeft.pack(side = LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame,width = 1050 , text = "Prescription",
        font = ("arial",15,"bold"), height = 390 , bd = 7 , relief = RIDGE , bg="#0099cc")
        Data_FrameRight.pack(side = RIGHT) 

        Data_Framedata = LabelFrame(Data_Frame,width = 1050, text = "Prescription Data", font = ("arial",12,"italic bold"),
        height = 390 , bd = 4 , relief = RIDGE , bg = "#3eb7bb")
        Data_Framedata.pack(side = LEFT)


        ###################### LABELS ##############################
        Datalbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Date" , padx = 2 , bg = "#0099cc")
        Datalbl.grid(row = 0, column = 0 , padx = 10 , pady = 5 , sticky = W)
        Datatxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Date_of_Registration)
        Datatxt.grid(row = 0 , column = 1 , padx = 10 , pady = 5 , sticky = E)


        #####REF Number
        Reflbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Reference Number" , padx = 2 , bg = "#0099cc")
        Reflbl.grid(row = 1, column = 0 , padx = 10 , pady = 5 , sticky = W)
        Reftxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 ,state = DISABLED, textvariable = Ref)
        Reftxt.grid(row = 1 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        #####Patient ID
        PatientIdlbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Patient Id" , padx = 2 , bg = "#0099cc")
        PatientIdlbl.grid(row = 2, column = 0 , padx = 10 , pady = 5 , sticky = W)
        PatientIdtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = PatientId)
        PatientIdtxt.grid(row = 2 , column = 1 , padx = 10 , pady = 5 , sticky = E)


        ######Patient Name
        PatientNamelbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Patient Name" , padx = 2 , bg = "#0099cc")
        PatientNamelbl.grid(row = 3, column = 0 , padx = 10 , pady = 5 , sticky = W)
        PatientNametxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Patientname)
        PatientNametxt.grid(row = 3 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        #####Date of birth
        Dateofbirthlbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Date of Birth" , padx = 2 , bg = "#0099cc")
        Dateofbirthlbl.grid(row = 4, column = 0 , padx = 10 , pady = 5 , sticky = W)
        Dateofbirthtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Dateofbirth)
        Dateofbirthtxt.grid(row = 4 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        #####Address
        Addresslbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Address" , padx = 2 , bg = "#0099cc")
        Addresslbl.grid(row = 5, column = 0 , padx = 10 , pady = 5 , sticky = W)
        Addresstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = PatientAddress)
        Addresstxt.grid(row = 5 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        ######NHS number

        NHSnumerlbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "NHS unique number" , padx = 2 , bg = "#0099cc")
        NHSnumerlbl.grid(row = 6, column = 0 , padx = 10 , pady = 5 , sticky = W)
        NHSnumbertxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = NHSnumber)
        NHSnumbertxt.grid(row = 6 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        #######Table name 

        Tabletlbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Tablet" , padx = 2 , bg = "#0099cc")
        Tabletlbl.grid(row = 7, column = 0 , padx = 10 , pady = 5 , sticky = W)

        Tabletcmb = ttk.Combobox(Data_FrameLeft , textvariable = cmbTableName , width = 25 , state = "readonly",
          font = ("arial",12,"bold"))
        Tabletcmb['values'] = ("", "paracetamol" , "dan-p", "Dio-l One", "Calpol", "Amlodipine Besylate", "Nexium",
                                    "Singulair","Plavix","Amoxicillian","Azithromycin","Licin-900")
        Tabletcmb.current(0)    # keep index 0 when nothing is selected 
        Tabletcmb.grid(row = 7 , column = 1 , padx = 10, pady=  5)  

        ######No of tablets to take 

        No_of_Tabletslbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Number of Tablets" , padx = 2 , bg = "#0099cc")
        No_of_Tabletslbl.grid(row = 8, column = 0 , padx = 10 , pady = 5 , sticky = W)
        No_of_Tabletstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Number_of_Tablets)
        No_of_Tabletstxt.grid(row = 8 , column = 1 , padx = 10 , pady = 5 , sticky = E)                            


        ####### 2nd column of other details in same frame

        ######hospital code  

        Hospitalcodelbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Hospital Code" , padx = 2 , bg = "#0099cc")
        Hospitalcodelbl.grid(row = 0, column = 2 , padx = 10 , pady = 5 , sticky = W)
        Hospitalcodetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = HospitalCode)
        Hospitalcodetxt.grid(row = 0 , column = 3 , padx = 10 , pady = 5 , sticky = E) 

        #######Strorage Advice where to kepp medicne

        StorageAdvicelbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Storage Advice" , padx = 2 , bg = "#0099cc")
        StorageAdvicelbl.grid(row = 1, column = 2 , padx = 10 , pady = 5 , sticky = W)

        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft , textvariable = StorageAdvice , width = 23 , state = "readonly",
          font = ("arial",12,"bold"))
        StorageAdvicecmb['values'] = ("", "Under room temp","below 0*C","Redrigration" )
        StorageAdvicecmb.current(0)   
        StorageAdvicecmb.grid(row = 1 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        #Lot number of medicine

        Lot_nolbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Lot number" , padx = 2 , bg = "#0099cc")
        Lot_nolbl.grid(row = 2, column = 2 , padx = 10 , pady = 5 , sticky = W)
        Lot_notxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = Lot)
        Lot_notxt.grid(row = 2 , column = 3 , padx = 10 , pady = 5 , sticky = E)  

        ### Issued date

        IssuedDatelbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Date of Issue" , padx = 2 , bg = "#0099cc")
        IssuedDatelbl.grid(row = 3, column = 2 , padx = 10 , pady = 5 , sticky = W)
        IssuedDatetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = IssuedDate)
        IssuedDatetxt.grid(row = 3 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        ### Expiry Date
        ExpiryDatelbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Date of Expiry" , padx = 2 , bg = "#0099cc")
        ExpiryDatelbl.grid(row = 4, column = 2 , padx = 10 , pady = 5 , sticky = W)
        ExpiryDatetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = ExpiryDate)
        ExpiryDatetxt.grid(row = 4 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        ###Daily Dose

        Dailydoselbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Daily Dose" , padx = 2 , bg = "#0099cc")
        Dailydoselbl.grid(row = 5, column = 2 , padx = 10 , pady = 5 , sticky = W)
        Dailydosetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = DailyDose)
        Dailydosetxt.grid(row = 5 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        ##Side Effects

        SideEffectslbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Side Effects" , padx = 2 , bg = "#0099cc")
        SideEffectslbl.grid(row = 6, column = 2 , padx = 10 , pady = 5 , sticky = W)
        SideEffectstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = SideEffects)
        SideEffectstxt.grid(row = 6 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        ###MOre Information like meet dr or any related to patient which is important but not coved in list 

        MoreInformationlbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "More Information" , padx = 2 , bg = "#0099cc")
        MoreInformationlbl.grid(row = 7, column = 2 , padx = 10 , pady = 5 , sticky = W)
        MoreInformationtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = MoreInformation)
        MoreInformationtxt.grid(row = 7 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        #####Medication (yes/no)

        Medicationlbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width = 20 , text = "Medication" , padx = 2 , bg = "#0099cc")
        Medicationlbl.grid(row = 8, column = 2 , padx = 10 , pady = 5 , sticky = W)
        Medicationtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = Medication)
        Medicationtxt.grid(row = 8 , column = 3 , padx = 10 , pady = 5 , sticky = E)

        ####Text field for prescription
        TextPresciption = Text(Data_FrameRight , font = ("arial",12 , "bold"), width = 55 , height = 17 , padx = 3 , 
           pady = 5 )
        TextPresciption.grid(row = 0 , column = 0 )   

        ######Ext for Prescription Data

        TextPresciptionData = Text(Data_Framedata , font = ("arial",12 , "bold"), width = 203 , height = 12  )
        TextPresciptionData.grid(row = 1 , column = 0 )

        ######Now we will add button to our middle frame

        Prescriptionbtn = Button(Button_Frame, text = "Prescription" , bg = '#ffaab0', activebackground = "#fcceb2",
        font = ("arial",15,"bold") , width = 22, command = prescriptionfunc)
        Prescriptionbtn.grid(row = 0, column = 0 , padx = 15 )

        Receiptbtn = Button(Button_Frame, text = "Prescription Data" , bg = '#ffaab0', activebackground = "#fcceb2",
        font = ("arial",15,"bold") , width = 22, command = prescriptiondatafunc)
        Receiptbtn.grid(row = 0, column = 1 , padx = 15 )

        Resetbtn = Button(Button_Frame, text = "Reset" , bg = '#ffaab0', activebackground = "#fcceb2",
        font = ("arial",15,"bold") , width = 22, command = resetfunc)
        Resetbtn.grid(row = 0, column = 2 , padx = 15 )

        Deletebtn = Button(Button_Frame, text = "Delete" , bg = '#ffaab0', activebackground = "#fcceb2",
        font = ("arial",15,"bold") , width = 22, command = deletefunc)
        Deletebtn.grid(row = 0, column = 3 , padx = 15 )

        Exitbtn = Button(Button_Frame, text = "Exit" , bg = '#ffaab0', activebackground = "#fcceb2",
        font = ("arial",15,"bold") , width = 22, command = exitbtn)
        Exitbtn.grid(row = 0, column = 4 , padx = 15 )

        prescriptiondatarow = Label(Data_Framedata , bg = "white" , font = ("arial", 12, "bold"),
        text = "Date\tReference Id\tPatient Name\tDate of birth\tNHS Number\tTable\tNo of Tablet\tIssued Date\tExpiry Date\tDaily Dose\tStorage Advice\tPatientID")
        prescriptiondatarow.grid(row = 0, column = 0 , sticky = W )





if __name__ == "__main__":
    main()
