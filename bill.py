from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x940+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #=========variables=============\
        self.mem_phone = StringVar()
        self.mem_value = StringVar()
        #======cosmetic============\

        self.soap=IntVar()
        self.fwash=IntVar()
        self.fcream=IntVar()
        self.shampoo=IntVar()
        self.hgell=IntVar()
        self.blotion=IntVar()

        #==========grocery=====

        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #=========stationary=======
        self.pen=IntVar()
        self.pencil=IntVar()
        self.notebooks=IntVar()
        self.gset=IntVar()
        self.papers=IntVar()
        self.colors=IntVar()

        #=======Total product price and tax variable=======\
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.stationary_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.stationary_tax=StringVar()

        #=========customer details variables=========\
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.b_no=StringVar()
        x = random.randint(1,999)
        self.b_no.set(str(x))
        self.search_bill=StringVar()


        # customer details frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE, text="Customer Details",font=("times new roman", 15, "bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_label = Label(F1, text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_label = Label(F1, text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_label = Label(F1, text="Customer Bill No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn = Button(F1, text= "Search",command=self.find_bills,width=10,bd=7,font=("arial", 12,"bold")).grid(row=0,column=6,pady=10,padx=10)

        #===============cosmetic frame=================

        F2=LabelFrame(self.root,bd=10,relief=GROOVE, text="Cosmetics",font=("times new roman", 15, "bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        #bath soap
        bath_label = Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        #face wash
        face_wash_label = Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_wash_txt=Entry(F2,textvariable=self.fwash,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        #face cream
        face_cream_label = Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.fcream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        #shampoo
        hair_s_label = Label(F2,text="Shampoo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.shampoo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        #hair gell
        hair_g_label = Label(F2,text="Hair Gell",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F2,width=10,textvariable=self.hgell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        #body lotion
        body_lotion_label = Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_lotion_txt=Entry(F2,width=10,textvariable=self.blotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #===============grocery frame=================

        F3=LabelFrame(self.root,bd=10,relief=GROOVE, text="Grocery",font=("times new roman", 15, "bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        #rice
        g1_label = Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        #food oil
        g2_wash_label = Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_wash_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        #daal
        g3_cream_label = Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_cream_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        #wheat
        g4_label = Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        #sugar
        g5_label = Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        #tea
        g6_label = Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #===============stationary frame=================

        F4=LabelFrame(self.root,bd=10,relief=GROOVE, text="Stationary",font=("times new roman", 15, "bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        #pen
        s1_label = Label(F4,text="Pen",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        s1_txt=Entry(F4,width=10,textvariable=self.pen,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        #Pencil
        s2_wash_label = Label(F4,text="Pencil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        s2_wash_txt=Entry(F4,width=10,textvariable=self.pencil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        #Notebooks
        s3_cream_label = Label(F4,text="Notebooks",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        s3_cream_txt=Entry(F4,width=10,textvariable=self.notebooks,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        #geometry set
        s4_label = Label(F4,text="Geomety Set",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        s4_txt=Entry(F4,width=10,textvariable=self.gset,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        #Paper
        s5_label = Label(F4,text="Art Papers",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        s5_txt=Entry(F4,width=10,textvariable=self.papers,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        #Poster colors
        s6_label = Label(F4,text="Poster Colors",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        s6_txt=Entry(F4,width=10,textvariable=self.colors,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #==================Bill area=================
        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=380,height=380)
        bill_title = Label(F5,text="Bill Area",font=("arial",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea = Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #========Button Frame=============
        F6=LabelFrame(self.root,bd=10,relief=GROOVE, text="Bill Menu",font=("times new roman", 15, "bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=570,relwidth=1,height=140)

        m1_label=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_label=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_label=Label(F6,text="Total Stationary Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.stationary_price,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_label=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_label=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_label=Label(F6,text="Stationary Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.stationary_tax,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,relief=GROOVE,bd=7)
        btn_F.place(x=750,width=650,height=104)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",width=11,bd=5,font=("arial",15,"bold"),pady=15).grid(row=0,column=0,padx=5,pady=5)

        gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",width=11,bd=5,font=("arial",15,"bold"),pady=15).grid(row=0,column=1,padx=5,pady=5)

        clear_btn=Button(btn_F,text="Clear",command=self.clear_bill,bg="cadetblue",fg="white",width=11,bd=5,font=("arial",15,"bold"),pady=15).grid(row=0,column=2,padx=5,pady=5)

        exit_btn=Button(btn_F,text="Exit",command=self.exit_set,bg="cadetblue",fg="white",width=11,bd=5,font=("arial",15,"bold"),pady=15).grid(row=0,column=3,padx=5,pady=5)
        #========================offer section==============
        F7=LabelFrame(self.root,bd=2,relief=GROOVE, text="Creazy Offers",font=("times new roman", 15, "bold"),fg="gold",bg=bg_color)
        F7.place(x=0,y=710,relwidth=1,height=100)

        membership_btn=Button(F7,text="Membership",command=self.add_member,bg="cadetblue",fg="white",width=11,bd=5,font=("arial",15,"bold"),pady=0).grid(row=0,column=0,padx=5,pady=5)

        memtxt = Entry(F7,width=18,textvariable=self.mem_phone,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        memvalue = Entry(F7,width = 18,bd=5,textvariable=self.mem_value,font=("arial",10,"bold"),relief=SUNKEN).grid(row=0,column=2,padx=10,pady=1)

        


        self.welcome_bill()
    def add_member(self):
        self.mem_value = "750"
        f1=open("membership/"+str(self.c_phon.get())+".txt","w")
        f1.write("Membership Card")
        f1.close()
    
    def isMember(self):
        for i in os.listdir("membership/"):
            print(i.split('.')[0])
            print(self.mem_phone.get())
            if self.mem_phone.get() == i.split('.')[0]:
                self.to_pay = self.to_pay - 0.20*self.total_price
                self.txtarea.insert(END,f"\tNew Bill To Pay\t\t\t{self.to_pay}")


    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.fcream.get()*140
        self.c_fw_p=self.fwash.get()*90
        self.c_hg_p=self.hgell.get()*60
        self.c_s_p=self.shampoo.get()*180
        self.c_bl_p=self.blotion.get()*150
        self.total_cosmetic_price = float(

                                        self.soap.get()*40+
                                        self.c_fc_p+
                                        self.c_fw_p+
                                        self.c_hg_p+
                                        self.c_s_p+
                                        self.c_bl_p
        )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.cosmetic_tax.set("Rs. "+str(round((self.total_cosmetic_price*0.05),2)))


        self.g_r_p=self.rice.get()*45
        self.g_d_p=self.daal.get()*85
        self.g_fo_p=self.food_oil.get()*110
        self.g_s_p=self.sugar.get()*115
        self.g_t_p=self.tea.get()*250
        self.g_w_p=self.wheat.get()*18
        self.total_grocery_price = float(
                                        self.g_r_p+
                                        self.g_d_p+
                                        self.g_fo_p+
                                        self.g_s_p+
                                        self.g_t_p+
                                        self.g_w_p
        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.grocery_tax.set("Rs. "+str(round((self.total_grocery_price*0.05),2)))


        self.s_p_p=self.pen.get()*15
        self.s_pe_p=self.pencil.get()*10
        self.s_c_p=self.colors.get()*45
        self.s_gs_p=self.gset.get()*50
        self.s_n_p=self.notebooks.get()*25
        self.s_pa_p=self.papers.get()*5
        self.total_stationary_price = float(
                                        self.s_p_p+
                                        self.s_pe_p+
                                        self.s_c_p+
                                        self.s_gs_p+
                                        self.s_n_p+
                                        self.s_pa_p
        )
        self.stationary_price.set("Rs. "+str(self.total_stationary_price))
        self.stationary_tax.set("Rs. "+str(round((self.total_stationary_price*0.05),2)))

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END, "\tWelcome Creazy Retailer\n")
        self.txtarea.insert(END, f"\nBill Number : {self.b_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nCustomer Number : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n==========================================")
        self.txtarea.insert(END, f"\nProducts\tQty\tUnits\tPrice\tTax")
        self.txtarea.insert(END, f"\n==========================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error","Customer details are must")
        else:
            self.welcome_bill()
            #===================cosmetics===============
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t{self.soap.get()}\t"+"peice"+f"\t{self.soap.get()*40}\t{(self.soap.get()*40)*0.05}")
            if self.fcream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t{self.fcream.get()}\t"+"200ml"+f"\t{self.c_fc_p}\t{(self.c_fc_p)*0.05}")
            if self.fwash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t{self.fwash.get()}\t"+"250gm"+f"\t{self.c_fw_p}\t{(self.c_fw_p)*0.05}")
            if self.hgell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gell\t{self.hgell.get()}\t"+"250gm"+f"\t{self.c_hg_p}\t{(self.c_hg_p)*0.05}")
            if self.shampoo.get()!=0:
                self.txtarea.insert(END,f"\n Shampoo\t{self.shampoo.get()}\t"+"1l"+f"\t{self.c_s_p}\t{(self.c_s_p)*0.05}")
            if self.blotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t{self.blotion.get()}\t"+"500ml"+f"\t{self.c_bl_p}\t{(self.c_bl_p)*0.05}")  
            #=================grocery=========================
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t{self.rice.get()}\t"+"kg"+f"\t{self.g_r_p}\t{(self.g_r_p)*0.05}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t{self.daal.get()}\t"+"500g"+f"\t{self.g_d_p}\t{(self.g_d_p)*0.05}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t{self.food_oil.get()}\t"+"l"+f"\t{self.g_fo_p}\t{(self.g_fo_p)*0.05}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t{self.sugar.get()}\t"+"kg"+f"\t{self.g_s_p}\t{(self.g_s_p)*0.05}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t{self.tea.get()}\t"+"kg"+f"\t{self.g_t_p}\t{(self.g_t_p)*0.05}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t{self.wheat.get()}\t"+"kg"+f"\t{self.g_w_p}\t{(self.g_w_p)*0.05}")
            #===============stationary=========================
            if self.pen.get()!=0:
                self.txtarea.insert(END,f"\n Pen\t{self.pen.get()}\t"+"piece"+f"\t{self.s_p_p}\t{(self.s_p_p)*0.05}")
            if self.pencil.get()!=0:
                self.txtarea.insert(END,f"\n Pencil\t{self.pencil.get()}\t"+"peice"+f"\t{self.s_pe_p}\t{(self.s_pe_p)*0.05}")
            if self.colors.get()!=0:
                self.txtarea.insert(END,f"\n Colors\t{self.colors.get()}\t"+"peice"+f"\t{self.s_c_p}\t{(self.s_c_p)*0.05}")
            if self.gset.get()!=0:
                self.txtarea.insert(END,f"\n Geometry\t{self.gset.get()}\t"+"set"+f"\t{self.s_gs_p}\t{(self.s_gs_p)*0.05}")
            if self.notebooks.get()!=0:
                self.txtarea.insert(END,f"\n Notebooks\t{self.notebooks.get()}\t"+"peice"+f"\t{self.s_n_p}\t{(self.s_n_p)*0.05}")
            if self.papers.get()!=0:
                self.txtarea.insert(END,f"\n Art Papers\t{self.papers.get()}\t"+"peice"+f"\t{self.s_pa_p}\t{(self.s_pa_p)*0.05}")  
            
            #===============Total Section===========================
            self.total_price=self.total_stationary_price+self.total_grocery_price+self.total_cosmetic_price
            self.total_tax=(self.total_stationary_price+self.total_grocery_price+self.total_cosmetic_price)*0.05
            self.to_pay=self.total_price+self.total_tax
            self.new_pay = self.to_pay + 750
            if self.to_pay!=0.0:
                self.txtarea.insert(END, f"\n==========================================")
                self.txtarea.insert(END, f"\nTotal Price\t\t\t{self.total_price}")
                self.txtarea.insert(END, f"\nTotal Tax\t\t\t{self.total_tax}")
                self.txtarea.insert(END, f"\nTo Pay\t\t\t{self.to_pay}")
                if self.mem_value == "750":
                    self.txtarea.insert(END, f"\nNew Price after Membership\t\t{self.new_pay}")
                self.txtarea.insert(END, f"\n==========================================")
                res = messagebox.askquestion("Payment Mode","Cash")
                if res =="yes":
                    self.txtarea.insert(END, f"\nPayment Mode:\t\tCash")
                else:
                    self.txtarea.insert(END, f"\nPayment Mode:\t\tCard")
                
                self.isMember()
                self.save_bill()
            else:
                messagebox.showerror("Error","Should select atleast single product")

    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data = self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.c_phon.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
        else:
            return
        
    def find_bills(self):
        present = "no"
        for i in os.listdir("bills/"):
            print(i.split('.')[0])
            print(self.search_bill.get())
            if self.search_bill.get() == i.split('.')[0]:
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error","no such bill exists")

    def clear_bill(self):
        #======cosmetic============\

        self.soap.set(0)
        self.fwash.set(0)
        self.fcream.set(0)
        self.shampoo.set(0)
        self.hgell.set(0)
        self.blotion.set(0)

        #==========grocery=====

        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)

        #=========stationary=======
        self.pen.set(0)
        self.pencil.set(0)
        self.notebooks.set(0)
        self.gset.set(0)
        self.papers.set(0)
        self.colors.set(0)

        #=======Total product price and tax variable=======\
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.stationary_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.stationary_tax.set("")

        #=========customer details variables=========\
        self.c_name.set("")
        self.c_phon.set("")
        self.b_no.set("")
        x = random.randint(1,999)
        self.b_no.set(str(x))
        self.search_bill.set("")

        self.mem_phone.set("")
        self.mem_value = ""
        

        self.welcome_bill()
    
    def exit_set(self):
        op = messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()
