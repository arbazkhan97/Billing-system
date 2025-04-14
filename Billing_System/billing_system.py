from tkinter import*
import random
import os
from tkinter import messagebox, END

import os
if not os.path.exists("bills"):
    os.makedirs("bills")

# ============main============================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1265x635+0+0")
        self.root.title("Billing System")
        bg_color = "#badc57"
        title = Label(self.root, text="Billing System", font=('times new roman', 20, 'bold'), pady=2, bd=8, bg="#ADD8E6", fg="Black", relief=GROOVE)
        title.pack(fill=X)
    # ================medical variables=======================
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.neosporin = IntVar()
        self.thermal_gun = IntVar()
    # ============grocery variables==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        #=============coldDrinks variables=============================
        self.sprite = IntVar()
        self.limca = IntVar()
        self.maaza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_dew = IntVar()
    # ==============Total product price================
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=8, fg="Black", bg="#ADD8E6")
        F1.place(x=0, y=52, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg="#ADD8E6", font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#ADD8E6", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        cbill_lbl = Label(F1, text="Find Bill No:", bg="#ADD8E6", font=('times new roman', 15, 'bold'))
        cbill_lbl.grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        cbill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=8, cursor="hand2", bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=0)

    # ===================MedicalItems====================================
        F2 = LabelFrame(self.root, text="Medical items", font=('times new roman', 15, 'bold'), bd=8, fg="Black", bg="#ADD8E6")
        F2.place(x=0, y=139, width=310, height=370)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Mask", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = Entry(F2, width=10, textvariable=self.mask, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('times new roman', 16, 'bold'), bd=5, relief =GROOVE)
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        dettol_lbl = Label(F2, text="Dettol", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        dettol_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        dettol_txt = Entry(F2, width=10, textvariable=self.dettol, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        dettol_txt.grid(row=3, column=1, padx=10, pady=10)

        neosporin_lbl = Label(F2, text="Neosporin", font =('times new roman', 16, 'bold'), bg="#ADD8E6", fg = "black")
        neosporin_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        neosporin_txt = Entry(F2, width=10, textvariable=self.neosporin, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        neosporin_txt.grid(row=4, column=1, padx=10, pady=10)

        thermal_gun_lbl = Label(F2, text="Thermal Gun", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        thermal_gun_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        thermal_gun_txt = Entry(F2, width=10, textvariable=self.thermal_gun, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        thermal_gun_txt.grid(row=5, column=1, padx=10, pady=10)

    # ==========GroceryItems=========================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=8, fg="Black", bg="#ADD8E6")
        F3.place(x=310, y=139, width=280, height=370)

        rice_lbl = Label(F3, text="Rice", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        daal_lbl = Label(F3, text="Daal", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        daal_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        daal_txt = Entry(F3, width=10, textvariable=self.daal, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        daal_txt.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F3, text="Flour", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        flour_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        flour_txt = Entry(F3, width=10, textvariable=self.flour, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        flour_txt.grid(row=4, column=1, padx=10, pady=10)

        maggi_lbl = Label(F3, text="Maggi", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        maggi_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        maggi_txt = Entry(F3, width=10, textvariable=self.maggi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        maggi_txt.grid(row=5, column=1, padx=10, pady=10)

    # ===========ColdDrinks================================
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('times new roman', 15, 'bold'), bd=8, fg="Black", bg="#ADD8E6")
        F4.place(x=590, y=139, width=320, height=370)

        sprite_lbl = Label(F4, text="Sprite", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sprite_txt = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        limca_lbl = Label(F4, text="Limca", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        limca_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        limca_txt = Entry(F4, width=10, textvariable=self.limca, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        limca_txt.grid(row=1, column=1, padx=10, pady=10)

        maaza_lbl = Label(F4, text="Maaza", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        maaza_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        maaza_txt = Entry(F4, width=10, textvariable=self.maaza, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        maaza_txt.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        fanta_lbl = Label(F4, text="Fanta", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        fanta_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        fanta_txt = Entry(F4, width=10, textvariable=self.fanta, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        fanta_txt.grid(row=4, column=1, padx=10, pady=10)

        mountain_dew_lbl = Label(F4, text="Mountain Dew", font=('times new roman', 16, 'bold'), bg="#ADD8E6", fg="black")
        mountain_dew_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        mountain_dew_txt = Entry(F4, width=10, textvariable=self.mountain_dew, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mountain_dew_txt.grid(row=5, column=1, padx=10, pady=10)

    # =================BillArea======================
        F5 = Frame(self.root, bd=8, relief=GROOVE)
        F5.place(x=910, y=139, width=350, height=370)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=8, fg="Black", bg="#ADD8E6")
        F6.place(x=0, y=510, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Medical Price", font=('times new roman', 14, 'bold'), bg="#ADD8E6", fg="black")
        m1_lbl.grid(row=0, column=0, padx=12, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.medical_price, font='arial 10 bold', bd=5, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=('times new roman', 14, 'bold'), bg="#ADD8E6", fg="black")
        m2_lbl.grid(row=1, column=0, padx=12, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=5, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=('times new roman', 14, 'bold'), bg="#ADD8E6", fg="black")
        m3_lbl.grid(row=2, column=0, padx=12, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font='arial 10 bold', bd=5, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Medical Tax", font=('times new roman', 14, 'bold'), bg="#ADD8E6", fg="black")
        m4_lbl.grid(row=0, column=2, padx=12, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.medical_tax, font='arial 10 bold', bd=5, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Grocery Tax", font=('times new roman', 14, 'bold'), bg="#ADD8E6", fg="black")
        m5_lbl.grid(row=1, column=2, padx=12, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=5, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Cold Drinks Tax", font=('times new roman', 14, 'bold'), bg="#ADD8E6", fg="black")
        m6_lbl.grid(row=2, column=2, padx=12, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='arial 10 bold', bd=5, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

    # =======Buttons-======================================
        btn_f = Frame(F6, bd=5, relief=GROOVE)
        btn_f.place(x=750, width=490, height=90)

        total_btn = Button(btn_f, command=self.total, text="Total", cursor="hand2", bg="#535C68", bd=2, fg="white", pady=10, width=10, font='arial 12 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=15)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", cursor="hand2", bd=2, bg="#535C68", fg="white", pady=10, width=10, font='arial 12 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=15)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", cursor="hand2", bg="#535C68", bd=2, fg="white", pady=10, width=10, font='arial 12 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=15)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", cursor="hand2", bd=2, bg="#535C68", fg="white", pady=10, width=10, font='arial 12 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=15)
        self.welcome_bill()

#================TotalBill==========================
    def total(self):
        self.m_h_g_p = self.hand_gloves.get()*10
        self.m_s_p = self.sanitizer.get()*25
        self.m_m_p = self.mask.get()*10
        self.m_d_p = self.dettol.get()*60
        self.m_n_p = self.neosporin.get()*60
        self.m_t_g_p = self.thermal_gun.get()*380
        self.total_medical_price = float(self.m_m_p+self.m_h_g_p+self.m_d_p+self.m_n_p+self.m_t_g_p+self.m_s_p)

        self.medical_price.set("Rs. "+str(self.total_medical_price))
        self.m_tax = round((self.total_medical_price*0.12), 2)
        self.medical_tax.set("Rs. "+str(self.m_tax))

        self.g_r_p = self.rice.get()*50
        self.g_f_o_p = self.food_oil.get()*144
        self.g_w_p = self.wheat.get()*29
        self.g_d_p = self.daal.get()*95
        self.g_f_p = self.flour.get()*37
        self.g_m_p = self.maggi.get()*14
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_d_p+self.g_f_p+self.g_m_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.12), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.sprite.get()*50
        self.c_d_l_p = self.limca.get()*50
        self.c_d_m_p = self.maaza.get()*60
        self.c_d_c_p = self.coke.get()*55
        self.c_d_f_p = self.fanta.get()*50
        self.c_m_d = self.mountain_dew.get()*55
        self.total_cold_drinks_price = float(self.c_d_s_p+self.c_d_l_p+self.c_d_m_p+self.c_d_c_p+self.c_d_f_p+self.c_m_d)

        self.cold_drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.18), 2)
        self.cold_drinks_tax.set("Rs. "+str(self.c_d_tax))

        self.total_bill = round(float(self.total_medical_price+self.total_grocery_price+self.total_cold_drinks_price+self.m_tax+self.g_tax+self.c_d_tax),2)

#==============welcome-bill==============================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome To India Mart")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n====================================")
        self.txtarea.insert(END, f"\nProducts\t\t  QTY\t  Price")

#=========billArea=================================================
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
    # ============Medical===========================
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\nSanitizer\t\t   {self.sanitizer.get()}\t  Rs. {self.m_s_p}")
        if self.mask.get() != 0:
            self.txtarea.insert(END, f"\nMask\t\t   {self.mask.get()}\t  Rs. {self.m_m_p}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(END, f"\nHand Gloves\t\t   {self.hand_gloves.get()}\t  Rs. {self.m_h_g_p}")
        if self.dettol.get() != 0:
            self.txtarea.insert(END, f"\nDettol\t\t   {self.dettol.get()}\t  Rs. {self.m_d_p}")
        if self.neosporin.get() != 0:
            self.txtarea.insert(END, f"\nNeosporin\t\t   {self.neosporin.get()}\t  Rs. {self.m_n_p}")
        if self.thermal_gun.get() != 0:
            self.txtarea.insert(END , f"\nThermal Gun\t\t   {self.thermal_gun.get()}\t  Rs. {self.m_t_g_p}")
    # ==============Grocery============================
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\nRice\t\t   {self.rice.get()}\t  Rs. {self.g_r_p}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\nFood Oil\t\t   {self.food_oil.get()}\t  Rs. {self.g_f_o_p}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\nWheat\t\t   {self.wheat.get()}\t  Rs. {self.g_w_p}")
        if self.daal.get() != 0:
            self.txtarea.insert(END, f"\nDaal\t\t   {self.daal.get()}\t  Rs. {self.g_d_p}")
        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\nFlour\t\t   {self.flour.get()}\t  Rs. {self.g_f_p}")
        if self.maggi.get() != 0:
            self.txtarea.insert(END, f"\nMaggi\t\t   {self.maggi.get()}\t  Rs. {self.g_m_p}")
        #================ColdDrinks==========================
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\nSprite\t\t   {self.sprite.get()}\t  Rs. {self.c_d_s_p}")
        if self.limca.get() != 0:
            self.txtarea.insert(END, f"\nLimca\t\t   {self.limca.get()}\t  Rs. {self.c_d_l_p}")
        if self.maaza.get() != 0:
            self.txtarea.insert(END, f"\nMaaza\t\t   {self.maaza.get()}\t  Rs. {self.c_d_m_p}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\nCoke\t\t   {self.coke.get()}\t  Rs. {self.c_d_c_p}")
        if self.fanta.get() != 0:
            self.txtarea.insert(END, f"\nFanta\t\t   {self.fanta.get()}\t  Rs. {self.c_d_f_p}")
        if self.mountain_dew.get() != 0:
            self.txtarea.insert(END, f"\nMountain Dew\t\t   {self.mountain_dew.get()}\t  Rs. {self.c_m_d}")

        self.txtarea.insert(END, f"\n---------------------------------------")
        # ===============taxes==============================
        if self.medical_tax.get() != '0.0':
            self.txtarea.insert(END, f"\nMedical Tax\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\nCold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n\nTotal Bill:\t\t\tRs. {self.total_bill}")
        self.txtarea.insert(END, f"\n---------------------------------------")
        self.save_bill()

    #====================savebill============================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    # ===================find_bill================================
    def find_bill(self):
        present = False
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                present = True
                break
        if present == False:
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
    #=============medical===========================
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.dettol.set(0)
            self.neosporin.set(0)
            self.thermal_gun.set(0)
    # ============grocery==============================
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.flour.set(0)
            self.maggi.set(0)
    # =============coldDrinks=============================
            self.sprite.set(0)
            self.limca.set(0)
            self.maaza.set(0)
            self.coke.set(0)
            self.fanta.set(0)
            self.mountain_dew.set(0)
    # ====================taxes================================
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    # ===========exit=======================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()