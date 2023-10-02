import os          # FOR SAVING  FILES TO SYSTEM
import random      # RANDOM MODULE FOR RANDOM GENERATION OF BILL NUMBER
import smtplib     #  FOR EMAIL TO BE SENT
import tempfile    #
from tkinter import *   # Module to help us create Graphical Interface(Label & Frame)
from tkinter import messagebox   # TO DISPLAY SUMMARY IN THE BILL  AREA


# FUNCTIONALITY PART

# FUNCTION FOR DELETE ATTACHED TO DELETE BUTTON
def clear():
    bathsoapEntry.delete(0, END)
    FacecreamEntry.delete(0, END)
    FacewashEntry.delete(0, END)
    HairsprayEntry.delete(0, END)
    HairgelEntry.delete(0, END)
    BodylotionEntry.delete(0, END)

    bathsoapEntry.insert(0,0)
    FacecreamEntry.insert(0, 0)
    FacewashEntry.insert(0,0)
    HairsprayEntry.insert(0,0)
    HairgelEntry.insert(0,0)
    BodylotionEntry.insert(0,0)

    riceEntry.delete(0, END)
    VegoilEntry.delete(0, END)
    PalmoilEntry.delete(0, END)
    WheatEntry.delete(0, END)
    SugarEntry.delete(0, END)
    TeaEntry.delete(0, END)

    riceEntry.insert(0, 0)
    VegoilEntry.insert(0, 0)
    PalmoilEntry.insert(0, 0)
    WheatEntry.insert(0, 0)
    SugarEntry.insert(0, 0)
    TeaEntry.insert(0, 0)

    SevenUpEntry.delete(0, END)
    SpriteEntry.delete(0, END)
    CocacolaEntry.delete(0, END)
    FantaEntry.delete(0, END)
    MaltEntry.delete(0, END)
    PepsiEntry.delete(0, END)

    SevenUpEntry.insert(0, 0)
    SpriteEntry.insert(0, 0)
    CocacolaEntry.insert(0, 0)
    FantaEntry.insert(0, 0)
    MaltEntry.insert(0, 0)
    PepsiEntry.insert(0, 0)



    cosmeticTaxEntry.delete(0,END)
    groceryTaxEntry.delete(0,END)
    drinkTaxEntry.delete(0,END)


    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0,END)
    drinkpriceEntry.delete(0, END)

    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    textarea.delete(1.0, END)


 #FUNCTION FOR EMAIL ATTACHED TO EMAIL BUTTON
def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is susccessfully sent', parent=root1)
            root1.destroy()
        except:
            messagebox.showinfo('Error, Something went wrong, please,try again',parent=root1)

    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error!', 'Bill is Empty')
    else:
        root1 = Toplevel()
        root1.grab_set() #to disable main window
        root1.grab_set()
        root1.title('Send gmail')
        root1.config(bg='gray20')
        root1.resizable(0, 0)

        senderFrame = LabelFrame(root1, text='SENDER', font=('arial', 16, 'bold'))
        senderFrame.grid(row=0, column=0)

        senderLabel = Label(senderFrame, text="Sender's Email", font=('arial', 14, 'bold'))
        senderLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'))
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), relief=RIDGE, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'))
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        receiverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'))
        receiverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'))
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'))
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(recipientFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN,
                              width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END))

        sendButton = Button(root1, text='SEND', font=('arial', 16, 'bold'), width=15, command=send_gmail)
        sendButton.grid(row=2, column=0, pady=20)

    root1.mainloop()


def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror("ERROR", "Invalid Number")


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f"bills/{billnumber}.txt", 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f' BILL {billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)


billnumber = random.randint(500, 1000)


def total():
    global soapprice, facecreamprice, facewashprice, Hairsprayprice, Hairgelprice, Bodylotionprice
    global riceprice, vegoilprice, palmoilprice, wheatprice, Sugarprice, Teaprice
    global sevenupprice, spriteprice, cocacolaprice, fantaprice, maltprice, pepsiprice
    global totalbill

    # cosmetic Price Calculation

    soapprice = int(bathsoapEntry.get()) * 20
    facecreamprice = int(FacecreamEntry.get()) * 50
    facewashprice = int(FacewashEntry.get()) * 100
    Hairsprayprice = int(HairsprayEntry.get()) * 150
    Hairgelprice = int(HairgelEntry.get()) * 80
    Bodylotionprice = int(BodylotionEntry.get()) * 60

    totalcosmeticprice = soapprice + facecreamprice + facewashprice + Hairsprayprice + Hairgelprice + Bodylotionprice

    cosmeticpriceEntry.insert(0, str(totalcosmeticprice) + ('NAIRA'))

    # Grocery Price Calculation
    riceprice = int(riceEntry.get()) * 20
    vegoilprice = int(VegoilEntry.get()) * 50
    palmoilprice = int(PalmoilEntry.get()) * 100
    wheatprice = int(WheatEntry.get()) * 150
    Sugarprice = int(SugarEntry.get()) * 80
    Teaprice = int(TeaEntry.get()) * 60

    totalgroceryprice = riceprice + vegoilprice + palmoilprice + wheatprice + Sugarprice + Teaprice
    grocerypriceEntry.insert(0, str(totalgroceryprice) + ('NAIRA'))

    # Drink Price Calculation
    sevenupprice = int(SevenUpEntry.get()) * 20
    spriteprice = int(SpriteEntry.get()) * 50
    cocacolaprice = int(CocacolaEntry.get()) * 100
    fantaprice = int(FantaEntry.get()) * 150
    maltprice = int(MaltEntry.get()) * 80
    pepsiprice = int(PepsiEntry.get()) * 60

    totaldrinkprice = sevenupprice + spriteprice + cocacolaprice + fantaprice + maltprice + pepsiprice
    drinkpriceEntry.insert(0, str(totaldrinkprice) + ('NAIRA'))

    # COSMETIC TAX CALCULATION
    cosmeticpriceEntry.delete(0, END)
    cosmeticpriceEntry.insert(0, f'{totalcosmeticprice}  NAIRA')
    cosmeticTax = totalcosmeticprice * 0.6
    cosmeticTaxEntry.delete(0, END)
    cosmeticTaxEntry.insert(0, str(cosmeticTax))

    # GROCERY TAX CALCULATION
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, f'{totalgroceryprice}  NAIRA')
    groceryTax = totalgroceryprice * 0.3
    groceryTaxEntry.delete(0, END)
    groceryTaxEntry.insert(0, str(groceryTax))

    # DRINK TAX CALCULATION
    drinkpriceEntry.delete(0, END)
    drinkpriceEntry.insert(0, f'{totaldrinkprice}  NAIRA')
    drinkTax = totaldrinkprice * 0.1
    drinkTaxEntry.delete(0, END)
    drinkTaxEntry.insert(0, str(drinkTax))

    #TOTAL BILL CALCULATION
    totalbill = totalcosmeticprice + totaldrinkprice + totalgroceryprice + groceryTax + cosmeticTax + drinkTax

 # BILL AREA FUNCTION DECLARATION AND DETAILS CODE
def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error!', "Customer details are required ")
    elif cosmeticpriceEntry.get() == '' and grocerypriceEntry.get() == '' and drinkpriceEntry.get() == '':
        messagebox.showerror('Error', 'No products are selected')
    elif cosmeticpriceEntry.get() == '0 NAIRA' and grocerypriceEntry.get() == '0 NAIRA' and drinkpriceEntry.get() == '0 NAIRA':
        messagebox.showerror('Error', 'No products are selected')
    else:
        # Delete previous tex
        textarea.delete(1.0, END)

        textarea.insert(END, '\t\t **Welcome Customer**\n')
        textarea.insert(END, f'\nBill Number : {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}\n')
        textarea.insert(END, '\n=======================================================')
        textarea.insert(END, f'\nPRODUCt\t\t\tQUANTITY\t\t\tPRICE\n')
        textarea.insert(END, '\n=======================================================')

        # BILL AREA FOR COSMETICS

        if bathsoapEntry.get() != 0:
            textarea.insert(END, f'BATH Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice}NAIRA')

        if HairsprayEntry.get() != 0:
            textarea.insert(END, f' Hair Spray\t\t\t{HairsprayEntry.get()}\t\t\t{Hairsprayprice}NAIRA')

        if FacecreamEntry.get() != 0:
            textarea.insert(END, f' Facecream Spray\t\t\t{FacecreamEntry.get()}\t\t\t{facecreamprice}NAIRA')

        if FacewashEntry.get() != 0:
            textarea.insert(END, f' Fase wash\t\t\t{FacewashEntry.get()}\t\t\t{facewashprice}NAIRA')

        if HairgelEntry.get() != 0:
            textarea.insert(END, f' Hair Gel\t\t\t{HairgelEntry.get()}\t\t\t{Hairgelprice}NAIRA')

        if BodylotionEntry.get() != 0:
            textarea.insert(END, f' Body Lotin\t\t\t{BodylotionEntry.get()}\t\t\t{Bodylotionprice} NAIRA')

        # BILL AREA FOR GROCERY

        if riceEntry.get() != 0:
            textarea.insert(END, f'RICE \t\t\t{riceEntry.get()}\t\t\t{riceprice}NAIRA')

        if VegoilEntry.get() != 0:
            textarea.insert(END, f' VEG OIL \t\t\t{VegoilEntry.get()}\t\t\t{vegoilprice}NAIRA')

        if PalmoilEntry.get() != 0:
            textarea.insert(END, f' PALM OIL \t\t\t{PalmoilEntry.get()}\t\t\t{palmoilprice}NAIRA')

        if WheatEntry.get() != 0:
            textarea.insert(END, f' WHEAT \t\t\t{WheatEntry.get()}\t\t\t{wheatprice}NAIRA')

        if SugarEntry.get() != 0:
            textarea.insert(END, f' SUGAR\t\t\t{SugarEntry.get()}\t\t\t{Sugarprice}NAIRA')

        if TeaEntry.get() != 0:
            textarea.insert(END, f' TEA \t\t\t{TeaEntry.get()}\t\t\t{Teaprice}NAIRA')

        # BILL AREA FOR DRINKS

        if SevenUpEntry.get() != 0:
            textarea.insert(END, f' SEVEN UP \t\t\t{SevenUpEntry.get()}\t\t\t{sevenupprice}NAIRA')

        if SpriteEntry.get() != 0:
            textarea.insert(END, f' SPRITE\t\t\t{SpriteEntry.get()}\t\t\t{spriteprice}NAIRA')

        if CocacolaEntry.get() != 0:
            textarea.insert(END, f' COCACOLA \t\t\t{CocacolaEntry.get()}\t\t\t{cocacolaprice}NAIRA')

        if FantaEntry.get() != 0:
            textarea.insert(END, f' FANTA \t\t\t{FantaEntry.get()}\t\t\t{fantaprice}NAIRA')

        if MaltEntry.get() != 0:
            textarea.insert(END, f' MALT \t\t\t{MaltEntry.get()}\t\t\t{maltprice}NAIRA')

        if PepsiEntry.get() != 0:
            textarea.insert(END, f' PEPSI \t\t\t{PepsiEntry.get()}\t\t\t{pepsiprice}NAIRA')

        # TAX ON BILL AREA
        if cosmeticTaxEntry.get() != 0.0:
            textarea.insert(END, f'\nCosmetic Tax\t\t\t{cosmeticTaxEntry.get()}')

        if groceryTaxEntry.get() != 0.0:
            textarea.insert(END, f'\nGrocery Tax\t\t\t{groceryTaxEntry.get()}')

        if drinkTaxEntry.get() != 0.0:
            textarea.insert(END, f'\nDrink Tax\t\t\t{drinkTaxEntry.get()}')

            textarea.insert(END, '\n=======================================================')
            textarea.insert(END, f'\nTotal Bill \t\t\t{totalbill}')

            textarea.insert(END, '\n=======================================================')

            save_bill()


# GUI PART
# class tKINTER SPECIFICATION
root = Tk()                  #ASSIGN OBJECT TO  TK CLASS
root.title('Supermarket payment Solution')    # passing string through Titlle method
root.geometry('1270x685')                      #pass dimention throgh geometry method
root.iconbitmap("icon.ico", )    # Getting from icon-icons.com

# HeadLine
headingLabel = Label(root, text="Supermarket payment Solution",
                     font=('times new roman', 30, "bold"), bg='gray20', bd=12, fg='gold', relief=GROOVE)
headingLabel.pack(fill=X)

# FRAME1 ;  customer details frame label
customer_details_frame = LabelFrame(root, text='Customer Details',
font=('times new roman', 15, 'bold'), bg='gray20', fg='gold', bd=8, relief=GROOVE)
customer_details_frame.pack(fill=X)

# COLUMN1 ; NAME LABEL
nameLabel = Label(customer_details_frame, text='Name',
                  font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
nameLabel.grid(row=0, column=0, padx=20)

# COLUMN2 ; NAME ENTRY
nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8),

# COLUMN3 ; PHONE LABEL
phoneLabel = Label(customer_details_frame, text='Phone Number',
                   font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

# COLUMN4; PHONE ENTRY
phoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8),

# COLUMN5 ; BILL LABEL
billnumbberLabel = Label(customer_details_frame, text='Bill Number',
                         font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
billnumbberLabel.grid(row=0, column=4, padx=20, pady=2)

# COLUMN6 ; BILL ENTRY
billnumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8),

# COLUMN7 ; SEARCH BUTTON
searchButton = Button(customer_details_frame, text='SEARCH', command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productsFrame = Frame(root)
productsFrame.pack()

# Cosmetic label Frame
cosmeticFrame = LabelFrame(productsFrame, text='cosmetics',
                           font=('times new roman', 15, 'bold'), bg='gray20', fg='gold', bd=8, relief=GROOVE)
cosmeticFrame.grid(row=0, column=0)

# bathsoapLabel & Entry
bathsoapLabel = Label(cosmeticFrame, text='Bath Soap',
                      font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
bathsoapLabel.grid(row=0, column=1, pady=6, sticky='w')

bathsoapEntry = Entry(cosmeticFrame,
                      font=('time new roman', 15, 'bold'), width=10, bd=5)
bathsoapEntry.grid(row=0, column=2, pady=6, padx=10)
bathsoapEntry.insert(0, 0)

# Facecream Label & Entry
FacecreamLabel = Label(cosmeticFrame, text='Face Cream',
                       font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
FacecreamLabel.grid(row=2, column=1, pady=6, sticky='w')

FacecreamEntry = Entry(cosmeticFrame,
                       font=('time new roman', 15, 'bold'), width=10, bd=5)
FacecreamEntry.grid(row=2, column=2, pady=6, padx=10)
FacecreamEntry.insert(0, 0)

# FaceWash Label & Entry
FacewashLabel = Label(cosmeticFrame, text='Face Wash',
                      font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
FacewashLabel.grid(row=3, column=1, pady=6, sticky='w')

FacewashEntry = Entry(cosmeticFrame,
                      font=('time new roman', 15, 'bold'), width=10, bd=5)
FacewashEntry.grid(row=3, column=2, pady=6, padx=10)
FacewashEntry.insert(0, 0)

# HairsprayLabel & Entry
HairsprayLabel = Label(cosmeticFrame, text='Hair Spray',
                       font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
HairsprayLabel.grid(row=4, column=1, pady=6, sticky='w')

HairsprayEntry = Entry(cosmeticFrame,
                       font=('time new roman', 15, 'bold'), width=10, bd=5)
HairsprayEntry.grid(row=4, column=2, pady=6, padx=10)
HairsprayEntry.insert(0, 0)

# Hair Gel Label & Entry
HairgelLabel = Label(cosmeticFrame, text='Hair Gel',
                     font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
HairgelLabel.grid(row=5, column=1, pady=6, sticky='w')

HairgelEntry = Entry(cosmeticFrame,
                     font=('time new roman', 15, 'bold'), width=10, bd=5)
HairgelEntry.grid(row=5, column=2, pady=6, padx=10, )
HairgelEntry.insert(0, 0)

# Body Lotion label & Entry
BodylotionLabel = Label(cosmeticFrame, text='Body Lotion',
                        font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
BodylotionLabel.grid(row=6, column=1, pady=6, sticky='w')

BodylotionEntry = Entry(cosmeticFrame,
                        font=('time new roman', 15, 'bold'), width=10, bd=5)
BodylotionEntry.grid(row=6, column=2, pady=6, padx=10)
BodylotionEntry.insert(0, 0)

# Grocery Frame
groceryFrame = LabelFrame(productsFrame, text='Grocery',
                          font=('times new roman', 15, 'bold'), bg='gray20', fg='gold', bd=8, relief=GROOVE)
groceryFrame.grid(row=0, column=1)

# rice Label & Entry
riceLabel = Label(groceryFrame, text='Rice',
                  font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
riceLabel.grid(row=1, column=1, pady=6, sticky='w')

riceEntry = Entry(groceryFrame,
                  font=('time new roman', 15, 'bold'), width=10, bd=5)
riceEntry.grid(row=1, column=2, pady=6)
riceEntry.insert(0, 0)

# Vegoil Label & Entry
VegoilLabel = Label(groceryFrame, text='Vegoil',
                    font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
VegoilLabel.grid(row=2, column=1, pady=6, sticky='w')

VegoilEntry = Entry(groceryFrame,
                    font=('time new roman', 15, 'bold'), width=10, bd=5)
VegoilEntry.grid(row=2, column=2, pady=6, padx=10)
VegoilEntry.insert(0, 0)

# Palmoil Label & Entry
PalmoilLabel = Label(groceryFrame, text='Palm Oil',
                     font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
PalmoilLabel.grid(row=3, column=1, pady=6, sticky='w')

PalmoilEntry = Entry(groceryFrame,
                     font=('time new roman', 15, 'bold'), width=10, bd=5)
PalmoilEntry.grid(row=3, column=2, pady=6, padx=10)
PalmoilEntry.insert(0, 0)

# Wheat & Entry
WheatLabel = Label(groceryFrame, text='Wheat',
                   font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
WheatLabel.grid(row=4, column=1, pady=6, sticky='w')

WheatEntry = Entry(groceryFrame,
                   font=('time new roman', 15, 'bold'), width=10, bd=5)
WheatEntry.grid(row=4, column=2, pady=6, padx=10)
WheatEntry.insert(0, 0)
# Sugar Label & Entry
SugarLabel = Label(groceryFrame, text='Sugar',
                   font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
SugarLabel.grid(row=5, column=1, pady=6, sticky='w')

SugarEntry = Entry(groceryFrame,
                   font=('time new roman', 15, 'bold'), width=10, bd=5)
SugarEntry.grid(row=5, column=2, pady=6, padx=10, )
SugarEntry.insert(0, 0)

# Tea label & Entry
TeaLabel = Label(groceryFrame, text='Tea',
                 font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
TeaLabel.grid(row=6, column=1, pady=6, sticky='w')

TeaEntry = Entry(groceryFrame,
                 font=('time new roman', 15, 'bold'), width=10, bd=5)
TeaEntry.grid(row=6, column=2, pady=6, padx=10)
TeaEntry.insert(0, 0)
# Cold Drink Frame
drinkFrame = LabelFrame(productsFrame, text='Drink',
                        font=('times new roman', 15, 'bold'), bg='gray20', fg='gold', bd=8, relief=GROOVE)
drinkFrame.grid(row=0, column=2)

# SevenUp Label & Entry
SevenUpLabel = Label(drinkFrame, text='Seven Up',
                     font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
SevenUpLabel.grid(row=1, column=1, pady=6, sticky='w')

SevenUpEntry = Entry(drinkFrame,
                     font=('time new roman', 15, 'bold'), width=10, bd=5)
SevenUpEntry.grid(row=1, column=2, pady=6)
SevenUpEntry.insert(0, 0)
# Sprite Label & Entry
SpriteLabel = Label(drinkFrame, text='Sprite',
                    font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
SpriteLabel.grid(row=2, column=1, pady=6, sticky='w')

SpriteEntry = Entry(drinkFrame,
                    font=('time new roman', 15, 'bold'), width=10, bd=5)
SpriteEntry.grid(row=2, column=2, pady=6, padx=10)
SpriteEntry.insert(0, 0)

# Cocacola Label & Entry
CocacolaLabel = Label(drinkFrame, text='Cocacola',
                      font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
CocacolaLabel.grid(row=3, column=1, pady=6, sticky='w')

CocacolaEntry = Entry(drinkFrame,
                      font=('time new roman', 15, 'bold'), width=10, bd=5)
CocacolaEntry.grid(row=3, column=2, pady=6, padx=10)
CocacolaEntry.insert(0, 0)

# Fanta
FantaLabel = Label(drinkFrame, text='Fanta',
                   font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
FantaLabel.grid(row=4, column=1, pady=6, sticky='w')

FantaEntry = Entry(drinkFrame,
                   font=('time new roman', 15, 'bold'), width=10, bd=5)
FantaEntry.grid(row=4, column=2, pady=6, padx=10)
FantaEntry.insert(0, 0)
# Malt Label & Entry
MaltLabel = Label(drinkFrame, text='Malt',
                  font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
MaltLabel.grid(row=5, column=1, pady=6, sticky='w')
MaltEntry = Entry(drinkFrame,
                  font=('time new roman', 15, 'bold'), width=10, bd=5)
MaltEntry.grid(row=5, column=2, pady=6, padx=10, )
MaltEntry.insert(0, 0)

# PEPSI Lotion label & Entry
PepsiLabel = Label(drinkFrame, text='Pepsi',
                   font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
PepsiLabel.grid(row=6, column=1, pady=6, sticky='w')

PepsiEntry = Entry(drinkFrame,
                   font=('time new roman', 15, 'bold'), width=10, bd=5)
PepsiEntry.grid(row=6, column=2, pady=6, padx=10, )
PepsiEntry.insert(0, 0)
# bill frame

billframe = Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

billarealabel = Label(billframe, text='Bill Area', font=('time new roman', 15, 'bold'))
billarealabel.pack(fill=X)

# Scroll bar
scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

# Bill Menu frame
billmenuFrame = LabelFrame(root, text='Bill Menu',
                           font=('times new roman', 15, 'bold'), bg='gray20', fg='gold', bd=8, relief=GROOVE)
billmenuFrame.pack()

# Cosmetic Price Label and Entry
cosmeticpriceLabel = Label(billmenuFrame, text='Cosmetic Price',
                           font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
cosmeticpriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')

cosmeticpriceEntry = Entry(billmenuFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
cosmeticpriceEntry.grid(row=0, column=1, pady=6, padx=10)

# Drink Price Label and Entry
drinkpriceLabel = Label(billmenuFrame, text='Drink Price',
                        font=('time new roman', 14, 'bold'), bg='gray20', fg='white')
drinkpriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')

drinkpriceEntry = Entry(billmenuFrame, font=('time new roman', 14, 'bold'), width=10, bd=5)
drinkpriceEntry.grid(row=2, column=1, pady=6, padx=10)

# Grocery Price Label and Entry
grocerypriceLabel = Label(billmenuFrame, text='Grocery Price',
                          font=('time new roman', 14, 'bold'), bg='gray20', fg='white')
grocerypriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')

grocerypriceEntry = Entry(billmenuFrame, font=('time new roman', 14, 'bold'), width=10, bd=5)
grocerypriceEntry.grid(row=1, column=1, pady=6, padx=10)

# Cosmetic Tax Label and Entry

cosmeticTaxLabel = Label(billmenuFrame, text='Cosmetic Tax',
                         font=('time new roman', 15, 'bold'), bg='gray20', fg='white')
cosmeticTaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky='w')

cosmeticTaxEntry = Entry(billmenuFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
cosmeticTaxEntry.grid(row=0, column=3, pady=6, padx=10)

# DrinkTaxLabel Label and Entry
drinkTaxLabel = Label(billmenuFrame, text='Drink Tax',
                      font=('time new roman', 14, 'bold'), bg='gray20', fg='white')
drinkTaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky='w')

drinkTaxEntry = Entry(billmenuFrame, font=('time new roman', 14, 'bold'), width=10, bd=5)
drinkTaxEntry.grid(row=1, column=3, pady=6, padx=10)

# Grocery Tax Label and Entry

groceryTaxLabel = Label(billmenuFrame, text='Grocery Tax',
                        font=('time new roman', 14, 'bold'), bg='gray20', fg='white')
groceryTaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky='w')

groceryTaxEntry = Entry(billmenuFrame, font=('time new roman', 14, 'bold'), width=10, bd=5)
groceryTaxEntry.grid(row=2, column=3, pady=6, padx=10)

# Button Frame
buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'),
                     bg='gray20', fg='white', bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, padx=5, pady=20, )

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'),
                    bg='gray20', fg='white', bd=5, width=8, pady=10, command=bill_area)
billButton.grid(row=0, column=1, padx=5, pady=20)

emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'),
                     bg='gray20', fg='white', bd=5, width=8, pady=10, command=send_email)
emailButton.grid(row=0, column=2, padx=5, pady=20)

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'),
                     bg='gray20', fg='white', bd=5, width=8, pady=10, command=print_bill)
printButton.grid(row=0, column=3, padx=5, pady=20)

clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'),
                     bg='gray20', fg='white', bd=5, width=8, pady=10, command=clear)
clearButton.grid(row=0, column=4, padx=5, pady=20)

root.mainloop()             # Method to help us viewing window
