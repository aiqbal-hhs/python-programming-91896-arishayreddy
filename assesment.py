from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

#Def functions used for each variable to reset the receipt

def reset():
    textReceipt.delete(1.0,END)
    e_chicken_cranberry.set('0')
    e_chicken_supreme.set('0')
    e_seafood_deluxe.set('0')
    e_garlic_prawn.set('0')
    e_roasted_veggie.set('0')
    e_chicago_style.set('0')
    e_cheeseburger.set('0')
    e_tandoori_chicken.set('0')
    e_wedge_cheese.set('0')

    e_cheese.set('0')
    e_ham_cheese.set('0')
    e_hawaiian.set('0')
    e_pepperoni.set('0')
    e_bbq_chicken.set('0')
    e_beef_onion.set('0')
    e_veggie_trio.set('0')
    e_seven_cheese.set('0')
    e_chicken_prawn.set('0')

    e_coca_cola.set('0')
    e_water.set('0')
    e_orange_juice.set('0')
    e_fanta.set('0')
    e_sprite.set('0')
    e_garlic_bread.set('0')
    e_chips.set('0')
    e_onion_rings.set('0')
    e_chicken_wings.set('0')

    textchicken_cranberry.config(state=DISABLED)
    textseafood_deluxe.config(state=DISABLED)
    textgarlic_prawn.config(state=DISABLED)
    textwedge_cheese.config(state=DISABLED)
    textroasted_veggie.config(state=DISABLED)
    textchicago_style.config(state=DISABLED)
    textchicken_supreme.config(state=DISABLED)
    textcheeseburger.config(state=DISABLED)
    texttandoori_chicken.config(state=DISABLED)

    texthawaiian.config(state=DISABLED)
    textcheese.config(state=DISABLED)
    textbbq_chicken.config(state=DISABLED)
    textseven_cheese.config(state=DISABLED)
    textbeef_onion.config(state=DISABLED)
    textpepperoni.config(state=DISABLED)
    textchicken_prawn.config(state=DISABLED)
    textveggie_trio.config(state=DISABLED)
    textham_cheese.config(state=DISABLED)

    textwater.config(state=DISABLED)
    textorange_juice.config(state=DISABLED)
    textsprite.config(state=DISABLED)
    textfanta.config(state=DISABLED)
    textonion_rings.config(state=DISABLED)
    textgarlic_bread.config(state=DISABLED)
    textchicken_wings.config(state=DISABLED)
    textchips.config(state=DISABLED)
    textcoca_cola.config(state=DISABLED)


# Variable set at 0 at default before ordering
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')



# This is a Function for the receipt to be printed
def send():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        def send_msg():
            message=textarea.get(1.0,END)
            number=numberfield.get()
            auth='woVHAjOGldMsPhnT7gS6XRIi4cYr0ym3FZkEWfKv9Qxauq8J2DHDWus7AqZKnkeXlVzQJa3fIRrp925S'
            url='https://www.fast2sms.com/dev/bulk'

            params={
                'authorization':auth,
                'message':message,
                'numbers':number,
                'sender-id':'FSTSMS',
                'route':'p',
                'language':'english'
            }
            response=requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')
            if result==True:
                messagebox.showinfo('Send Successfully','Message sent succesfully')

            else:
                messagebox.showerror('Error','Something went wrong')

        root2=Toplevel()
        # Title that will send bill

        root2.title("Send Bill")
        root2.config(bg='red4')
        root2.geometry('485x620+50+50')

        
        # Label that ask user for Mobile number  for order
        numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='red4',fg='white')
        numberLabel.pack(pady=5)

        numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
        numberfield.pack(pady=5)

        # Label that shows bill details  that will aks for name address and phone number
        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        billLabel.pack(pady=5)

        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

        if costoffoodvar.get() != '0 NZD':
            textarea.insert(END, f'Cost Of Food\t\t\t{priceofFood}NZD\n')
        if costofdrinksvar.get() != '0 NZD':
            textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}NZD\n')
        if costofcakesvar.get() != '0 NZD':
            textarea.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}NZD\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}NZD\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}NZD\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems + 50}NZD\n')

        sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE
                          ,command=send_msg)
        sendButton.pack(pady=5)
    
        root2.mainloop()

# Def function to save the order  
def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Succesfully Saved')
# Def function to set out the bill  
def receipt():
    global billnumber,date
    if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost Of Items(NZD)\n')
        textReceipt.insert(END,'***************************************************************\n')
        # This is for if the item is clicked what it will show on the bill area
        if e_chicken_supreme.get()!='0':
            textReceipt.insert(END,f'Chicken Supreme\t\t\t{int(e_chicken_supreme.get())*13.50}\n\n')
            
        # This is for if the item is clicked what it will show on the bill area
        if e_chicago_style.get()!='0':
            textReceipt.insert(END,f'Chicago Style\t\t\t{int(e_chicago_style.get())*13.50}\n\n')
        # This is for if the item is clicked what it will show on the bill area
        if e_garlic_prawn.get()!='0':
            textReceipt.insert(END,f'Garlic Prawn\t\t\t{int(e_garlic_prawn.get())*13.50}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_seafood_deluxe.get() != '0':
            textReceipt.insert(END, f'Seafood Deluxe\t\t\t{int(e_seafood_deluxe.get()) * 13.50}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_cheeseburger.get() != '0':
            textReceipt.insert(END, f'Cheeseburger Pizza\t\t\t{int(e_cheeseburger.get()) * 13.50}\n\n')
        # This is for if the item is clicked what it will show on the bill area
        if e_tandoori_chicken.get() != '0':
            textReceipt.insert(END, f'Breakfast\t\t\t{int(e_tandoori_chicken.get()) * 13.50}\n\n')
        # This is for if the item is clicked what it will show on the bill area
        if e_roasted_veggie.get() != '0':
            textReceipt.insert(END, f'Roasted Veggie\t\t\t{int(e_roasted_veggie.get()) * 13.50}\n\n')
        # This is for if the item is clicked what it will show on the bill area
        if e_chicken_cranberry.get() != '0':
            textReceipt.insert(END, f'Chicken Cranberry \t\t\t{int(e_chicken_cranberry.get()) * 13.50}\n\n')
        # This is for if the item is clicked what it will show on the bill area
        if e_wedge_cheese.get() != '0':
            textReceipt.insert(END, f'Wedge Cheese\t\t\t{int(e_wedge_cheese.get()) * 13.50}\n\n')
        # This is for if the item is clicked what it will show on the bill area

        if e_hawaiian.get() != '0':
            textReceipt.insert(END, f'Hawiaan\t\t\t{int(e_hawaiian.get()) * 8.50}\n\n')

        # This is for if the item is clicked what it will show on the bill area

        if e_bbq_chicken.get() != '0':
            textReceipt.insert(END, f'BBQ Chicken\t\t\t{int(e_bbq_chicken.get()) * 8.50}\n\n')
        
        # This is for if the item is clicked what it will show on the bill area
        if e_beef_onion.get() != '0':
            textReceipt.insert(END, f'Beef Onion\t\t\t{int(e_beef_onion.get()) * 8.50}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_veggie_trio.get() != '0':
            textReceipt.insert(END, f'Veggie Trio\t\t\t{int(e_veggie_trio.get()) * 8.50}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_pepperoni.get() != '0':
            textReceipt.insert(END, f'Pepperoni\t\t\t{int(e_pepperoni.get()) * 8.50}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_seven_cheese.get() != '0':
            textReceipt.insert(END, f'Seven Cheese\t\t\t{int(e_seven_cheese.get()) * 8.50}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_chicken_prawn.get() != '0':
            textReceipt.insert(END, f'Chicken Prawn \t\t\t{int(e_chicken_prawn.get()) * 8.50}\n\n')


        # This is for if the item is clicked what it will show on the bill area
        if e_cheese.get() != '0':
            textReceipt.insert(END, f'Cheese\t\t\t{int(e_cheese.get()) * 8.50}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_ham_cheese.get() != '0':
            textReceipt.insert(END, f'Ham and Cheese\t\t\t{int(e_ham_cheese.get()) * 8.50}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_water.get() != '0':
            textReceipt.insert(END, f'Water\t\t\t{int(e_water.get()) * 8.50}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_orange_juice.get() != '0':
            textReceipt.insert(END, f'Orange Juice\t\t\t{int(e_orange_juice.get()) * 3.00}\n\n')


        # This is for if the item is clicked what it will show on the bill area
        if e_sprite.get() != '0':
            textReceipt.insert(END, f'Sprite \t\t\t{int(e_sprite.get()) * 3.00}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_fanta.get() != '0':
            textReceipt.insert(END, f' Fanta \t\t\t{int(e_fanta.get()) * 3.00}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_chips.get() != '0':
            textReceipt.insert(END, f' Crinkle -Cut Chips\t\t\t{int(e_chips.get()) * 3.00}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_garlic_bread.get() != '0':
            textReceipt.insert(END, f'Garlic Bread\t\t\t{int(e_garlic_bread.get()) * 3.00}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_chicken_wings.get() != '0':
            textReceipt.insert(END, f'Chicken Wings \t\t\t{int(e_chicken_wings.get()) * 3.50}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_coca_cola.get() != '0':
            textReceipt.insert(END, f'Coca Cola\t\t\t{int(e_coca_cola.get()) * 3.00}\n\n')

        # This is for if the item is clicked what it will show on the bill area
        if e_onion_rings.get() != '0':
            textReceipt.insert(END, f' Onion Rings\t\t\t{int(e_onion_rings.get()) * 3.50}\n\n')

        # This is where the cost of delivery  is coded
        textReceipt.insert(END,'***************************************************************\n')
        if costoffoodvar.get()!='0 NZD':
            textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}NZD\n\n')
        if costofdrinksvar.get() != '0 NZD':
            textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}NZD\n\n')
        if costofcakesvar.get() != '0 NZD':
            textReceipt.insert(END,f'Cost Of Cakes\t\t\t{priceofCakes}NZD\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}NZD\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}NZD\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}NZD\n\n')
        textReceipt.insert(END,'***************************************************************\n')

    # This will happen if no items enetered and pressed "receipet"
    else:
        messagebox.showerror('Error','No Item Is selected')


# This is a function which shows total cost of items if they are set at 0
def totalcost():
    global priceofFood,priceofDrinks,priceofCakes,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        # When user selects the item it will  only accept number 
        item1 = int(e_chicken_cranberry.get())
        item2 = int(e_chicago_style.get())
        item3 = int(e_garlic_prawn.get())
        item4 = int(e_roasted_veggie.get())
        item5 = int(e_cheeseburger.get())
        item6 = int(e_chicken_supreme.get())
        item7 = int(e_seafood_deluxe.get())
        item8 = int(e_tandoori_chicken.get())
        item9 = int(e_wedge_cheese.get())

        item10 = int(e_ham_cheese.get())
        item11 = int(e_cheese.get())
        item12 = int(e_seven_cheese.get())
        item13 = int(e_bbq_chicken.get())
        item14 = int(e_pepperoni.get())
        item15 = int(e_hawaiian.get())
        item16 = int(e_beef_onion.get())
        item17 = int(e_veggie_trio.get())
        item18 = int(e_chicken_prawn.get())

        item19 = int(e_water.get())
        item20 = int(e_orange_juice.get())
        item21 = int(e_sprite.get())
        item22 = int(e_fanta.get())
        item23 = int(e_onion_rings.get())
        item24 = int(e_chicken_wings.get())
        item25 = int(e_garlic_bread.get())
        item26 = int(e_chips.get())
        item27 = int(e_coca_cola.get())


      # This is the price of each item
        priceofFood=(item1*13.50)+(item2*13.50)+(item3*13.50)+(item4*13.50)+ (item5*13.50) + (item6 * 13.50) + (item7 * 13.50) \
                    + (item8 * 13.50) + (item9 * 13.50)

        priceofDrinks=(item10*8.50)+(item11*8.50)+ (item12 * 8.50) + (item13 * 8.50) + (item14 * 8.50) + (item15 * 8.50) \
                      + (item16 * 8.50) + (item17 * 8.50) + (item18 * 8.50)

        priceofCakes=(item19*3.00)+(item20*3.00)+ (item21 * 3.00) + (item22 * 3.00) + (item23 * 3.50) + (item24 * 3.50) \
                     + (item25 * 3.50) + (item26 * 3.50) + (item27 * 3.00)

        costoffoodvar.set(str(priceofFood)+ ' NZD')
        costofdrinksvar.set(str(priceofDrinks)+ ' NZD')
        costofcakesvar.set(str(priceofCakes)+ ' NZD')

        subtotalofItems=priceofFood+priceofDrinks+priceofCakes
        subtotalvar.set(str(subtotalofItems)+' NZD')

        servicetaxvar.set('50 NZD')

        tottalcost=subtotalofItems+50
        totalcostvar.set(str(tottalcost)+' NZD')

    else:
        messagebox.showerror('Error','No Item Is selected')



def chicken_cranberry():
    if var1.get()==1:
        textchicken_cranberry.config(state=NORMAL)
        textchicken_cranberry.delete(0,END)
        textchicken_cranberry.focus()
    else:
        textchicken_cranberry.config(state=DISABLED)
        e_chicken_cranberry.set('0')

def roasted_veggie():
    if var2.get()==1:
        textroasted_veggie.config(state=NORMAL)
        textroasted_veggie.delete(0,END)
        textroasted_veggie.focus()
    else:
        textroasted_veggie.config(state=DISABLED)
        e_roasted_veggie.set('0')

def chicago_style():
    if var3.get()==1:
        textchicago_style.config(state=NORMAL)
        textchicago_style.delete(0,END)
        textchicago_style.focus()

    else:
        textchicago_style.config(state=DISABLED)
        e_chicago_style.set('0')

def chicken_supreme():
    if var4.get() == 1:
        textchicken_supreme.config(state=NORMAL)
        textchicken_supreme.focus()
        textchicken_supreme.delete(0, END)
    elif var4.get() == 0:
        textchicken_supreme.config(state=DISABLED)
        e_chicken_supreme.set('0')


def tandoori_chicken():
    if var5.get() == 1:
        texttandoori_chicken.config(state=NORMAL)
        texttandoori_chicken.focus()
        texttandoori_chickken.delete(0, END)
    elif var5.get() == 0:
        texttandoori_chicken.config(state=DISABLED)
        e_tandoori_chicken.set('0')


def seafood_deluxe():
    if var6.get() == 1:
        textseafood_deluxe.config(state=NORMAL)
        textseafood_deluxe.focus()
        textseafood_deluxe.delete(0, END)
    elif var6.get() == 0:
        textseafood_deluxe.confi(state=DISABLED)
        e_seafood_deluxe.set('0')


def garlic_prawn():
    if var7.get() == 1:
        textgarlic_prawn.config(state=NORMAL)
        textgarlic_prawn.focus()
        textgarlic_prawn.delete(0, END)
    elif var7.get() == 0:
        textgarlic_prawn.config(state=DISABLED)
        e_garlic_prawn.set('0')


def cheeseburger():
    if var8.get() == 1:
        textcheeseburger.config(state=NORMAL)
        textcheeseburger.focus()
        textcheeseburger.delete(0, END)
    elif var8.get() == 0:
        textcheeseburger.config(state=DISABLED)
        e_cheeseburger.set('0')


def wedge_cheese():
    if var9.get() == 1:
        textwedge_cheese.config(state=NORMAL)
        textwedge_cheese.focus()
        textwedge_cheese.delete(0, END)
    elif var9.get() == 0:
        textwedge_cheese.config(state=DISABLED)
        e_wedge_cheese.set('0')


def bbq_chicken():
    if var10.get() == 1:
        textbbq_chicken.config(state=NORMAL)
        textbbq_chicken.focus()
        textbbq_chicken.delete(0, END)
    elif var10.get() == 0:
        textbbq_chicken.config(state=DISABLED)
        e_bbq_chicken.set('0')


def veggie_trio():
    if var11.get() == 1:
        textveggie_trio.config(state=NORMAL)
        textveggie_trio.focus()
        textveggie_trio.delete(0, END)
    elif var11.get() == 0:
        textveggie_trio.config(state=DISABLED)
        e_veggie_trio.set('0')


def chicken_prawn():
    if var12.get() == 1:
        textchicken_prawn.config(state=NORMAL)
        textchicken_prawn.focus()
        textchicken_prawn.delete(0, END)
    elif var12.get() == 0:
        textchicken_prawn.config(state=DISABLED)
        e_chicken_prawn.set('0')


def cheese():
    if var13.get() == 1:
        textcheese.config(state=NORMAL)
        textcheese.focus()
        textcheese.delete(0, END)
    elif var13.get() == 0:
        textcheese.config(state=DISABLED)
        e_cheese.set('0')


def seven_cheese():
    if var14.get() == 1:
        textseven_cheese.config(state=NORMAL)
        textseven_chesse.focus()
        textseven_cheese.delete(0, END)
    elif var14.get() == 0:
        textseven_cheese.config(state=DISABLED)
        e_seven_chees.set('0')


def pepperoni():
    if var15.get() == 1:
        textpepperoni.config(state=NORMAL)
        textpepperoni.focus()
        textpepperoni.delete(0, END)
    elif var15.get() == 0:
        textpepperoni.config(state=DISABLED)
        e_pepperoni.set('0')


def ham_cheese():
    if var16.get() == 1:
        textham_cheese.config(state=NORMAL)
        textham_cheese.focus()
        textham_cheese.delete(0, END)
    elif var16.get() == 0:
        textham_cheese.config(state=DISABLED)
        e_ham_cheese.set('0')


def beef_onion():
    if var17.get() == 1:
        textbeef_onion.config(state=NORMAL)
        textbeef_onion.focus()
        textbeef_onion.delete(0, END)
    elif var17.get() == 0:
        textbeef_onion.config(state=DISABLED)
        e_beef_onion.set('0')


def hawaiian():
    if var18.get() == 1:
        texthawaiian.config(state=NORMAL)
        texthawaiian.focus()
        texthawaiian.delete(0, END)
    elif var18.get() == 0:
        texthawaiian.config(state=DISABLED)
        e_hawaiian.set('0')


def chips():
    if var19.get() == 1:
        textchips.config(state=NORMAL)
        textchips.focus()
        textchips.delete(0, END)
    elif var19.get() == 0:
        textchips.config(state=DISABLED)
        e_chips.set('0')


def garlic_bread():
    if var20.get() == 1:
        textgarlic_bread.config(state=NORMAL)
        textgarlic_bread.focus()
        textgarlic_bread.delete(0, END)
    elif var20.get() == 0:
        textgarlic_bread.config(state=DISABLED)
        e_garlic_bread.set('0')


def onion_rings():
    if var21.get() == 1:
        textonion_rings.config(state=NORMAL)
        textonion_rings.focus()
        textonion_rings.delete(0, END)
    elif var21.get() == 0:
        textonion_rings.config(state=DISABLED)
        e_onion_rings.set('0')


def chicken_wings():
    if var22.get() == 1:
        textchicken_wings.config(state=NORMAL)
        textchicken_wings.focus()
        textchicken_wings.delete(0, END)
    elif var22.get() == 0:
        textchicken_wings.config(state=DISABLED)
        e_chicken_wings.set('0')


def fanta():
    if var23.get() == 1:
        textfanta.config(state=NORMAL)
        textfanta.focus()
        textfanta.delete(0, END)
    elif var23.get() == 0:
        textfanta.config(state=DISABLED)
        e_fanta.set('0')


def sprite():
    if var24.get() == 1:
        textsprite.config(state=NORMAL)
        textsprite.focus()
        textsprite.delete(0, END)
    elif var24.get() == 0:
        textsprite.config(state=DISABLED)
        e_sprite.set('0')


def water():
    if var25.get() == 1:
        textwater.config(state=NORMAL)
        textwater.focus()
        textwater.delete(0, END)
    elif var25.get() == 0:
        textwater.config(state=DISABLED)
        e_water.set('0')


def orange_juice():
    if var26.get() == 1:
        textorange_juice.config(state=NORMAL)
        textorange_juice.focus()
        textorange_juice.delete(0, END)
    elif var26.get() == 0:
        textorange_juice.config(state=DISABLED)
        e_orange_juice.set('0')


def coca_cola():
    if var27.get() == 1:
        textcoca_cola.config(state=NORMAL)
        textcoca_cola.focus()
        textcoca_cola.delete(0, END)
    elif var27.get() == 0:
        textcoca_cola.config(state=DISABLED)
        e_coca_cola.set('0')



root=Tk()

root.geometry('1270x690+0+0')

root.resizable(0,0)

root.title('Henderson Pizza Palace')

root.config(bg='firebrick4')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Henderson Pizza Palace',font=('arial',30,'bold'),fg='yellow',bd=9,
                 bg='red4',width=51)
labelTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Gourmet Pizzas',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Valuer Range Pizzas',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Sides and Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

#Variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_chicken_supreme = StringVar()
e_cheeseburger = StringVar()
e_roasted_veggie = StringVar()
e_garlic_prawn = StringVar()
e_tandoori_chicken = StringVar()
e_chicago_style = StringVar()
e_wedge_cheese = StringVar()
e_seafood_deluxe = StringVar()
e_chicken_cranberry = StringVar()

e_cheese = StringVar()
e_seven_cheese = StringVar()
e_pepperoni = StringVar()
e_bbq_chicken = StringVar()
e_beef_onion = StringVar()
e_veggie_trio = StringVar()
e_hawaiian = StringVar()
e_ham_cheese = StringVar()
e_chicken_prawn = StringVar()

e_water = StringVar()
e_orange_juice = StringVar()
e_fanta = StringVar()
e_sprite = StringVar()
e_coca_cola = StringVar()
e_chicken_wings = StringVar()
e_onion_rings = StringVar()
e_garlic_bread = StringVar()
e_chips = StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

e_chicken_cranberry.set('0')
e_roasted_veggie.set('0')
e_chicken_supreme.set('0')
e_seafood_deluxe.set('0')
e_garlic_prawn.set('0')
e_tandoori_chicken.set('0')
e_chicago_style.set('0')
e_cheeseburger.set('0')
e_wedge_cheese.set('0')

e_bbq_chicken.set('0')
e_cheese.set('0')
e_seven_cheese.set('0')
e_pepperoni.set('0')
e_chicken_prawn.set('0')
e_ham_cheese.set('0')
e_beef_onion.set('0')
e_veggie_trio.set('0')
e_hawaiian.set('0')

e_water.set('0')
e_orange_juice.set('0')
e_coca_cola.set('0')
e_sprite.set('0')
e_fanta.set('0')
e_onion_rings.set('0')
e_garlic_bread.set('0')
e_chips.set('0')
e_chicken_wings.set('0')

##FOOD
chicken_cranberry = Checkbutton(foodFrame,text='Chicken Cranberry',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1
                 ,command=chicken_cranberry)
chicken_cranberry.grid(row=0,column=0,sticky=W)

roasted_veggie = Checkbutton(foodFrame,text='Roasted Veggie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2
                 ,command=roasted_veggie)
roasted_veggie.grid(row=1,column=0,sticky=W)

chicago_style = Checkbutton(foodFrame,text='Chicago Style',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3
                 ,command=chicago_style)
chicago_style.grid(row=2,column=0,sticky=W)

chicken_supreme = Checkbutton(foodFrame,text='Chicken Supreme',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4
                  ,command=chicken_supreme)
chicken_supreme.grid(row=3,column=0,sticky=W)

tandoori_chicken = Checkbutton(foodFrame,text='Tandoori Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5
                  ,command=tandoori_chicken)
tandoori_chicken.grid(row=4,column=0,sticky=W)

seafood_deluxe = Checkbutton(foodFrame,text='Seafood Deluxe',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6
                   ,command=seafood_deluxe)
seafood_deluxe.grid(row=5,column=0,sticky=W)

garlic_prawn = Checkbutton(foodFrame,text='Garlic Prawn',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,
                   command=garlic_prawn)
garlic_prawn.grid(row=6,column=0,sticky=W)

cheeseburger = Checkbutton(foodFrame,text='Cheeseburger Pizza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8
                   ,command=cheeseburger)
cheeseburger.grid(row=7,column=0,sticky=W)

wedge_cheese = Checkbutton(foodFrame,text='Wedge Cheese',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9
                    ,command=wedge_cheese)
wedge_cheese.grid(row=8,column=0,sticky=W)

#Entry Fields for Food Items

textchicken_cranberry=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken_cranberry)
textchicken_cranberry.grid(row=0,column=1)

textroasted_veggie=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roasted_veggie)
textroasted_veggie.grid(row=1,column=1)

textchicago_style=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicago_style)
textchicago_style.grid(row=2,column=1)

textchicken_supreme = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken_supreme)
textchicken_supreme.grid(row=3, column=1)

texttandoori_chicken = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tandoori_chicken)
texttandoori_chicken.grid(row=4, column=1)

textseafood_deluxe = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_seafood_deluxe)
textseafood_deluxe.grid(row=5, column=1)

textgarlic_prawn = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_garlic_prawn)
textgarlic_prawn.grid(row=6, column=1)

textcheeseburger = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cheeseburger)
textcheeseburger.grid(row=7, column=1)

textwedge_cheese = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_wedge_cheese)
textwedge_cheese.grid(row=8, column=1)

#Drinks

bbq_chicken = Checkbutton(drinksFrame,text='BBQ Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10
                  ,command=bbq_chicken)
bbq_chicken.grid(row=0,column=0,sticky=W)

veggie_trio = Checkbutton(drinksFrame,text='Veggie Trio',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11
                   ,command=veggie_trio)
veggie_trio.grid(row=1,column=0,sticky=W)

chicken_prawn = Checkbutton(drinksFrame,text='Chicken Prawn',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12
                   ,command=chicken_prawn)
chicken_prawn.grid(row=2,column=0,sticky=W)

cheese = Checkbutton(drinksFrame,text='Cheese',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13
                     ,command=cheese)
cheese.grid(row=3,column=0,sticky=W)

seven_cheese = Checkbutton(drinksFrame,text='Seven Cheese',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14
                     ,command=seven_cheese)
seven_cheese.grid(row=4,column=0,sticky=W)

pepperoni = Checkbutton(drinksFrame,text='Pepperoni',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15
                     ,command=pepperoni)
pepperoni.grid(row=5,column=0,sticky=W)

ham_cheese = Checkbutton(drinksFrame,text='Ham & Cheese',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16
                      ,command=ham_cheese)
ham_cheese.grid(row=6,column=0,sticky=W)

beef_onion = Checkbutton(drinksFrame,text='Beef & Onion',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17
                      ,command=beef_onion)
beef_onion.grid(row=7,column=0,sticky=W)

hawaiian = Checkbutton(drinksFrame,text='Hawaiian',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18
                       ,command=hawaiian)
hawaiian.grid(row=8,column=0,sticky=W)

#entry fields for drink items

textbbq_chicken = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_bbq_chicken)
textbbq_chicken.grid(row=0, column=1)

textveggie_trio = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_veggie_trio)
textveggie_trio.grid(row=1, column=1)

textchicken_prawn = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken_prawn)
textchicken_prawn.grid(row=2, column=1)

textcheese = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cheese)
textcheese.grid(row=3, column=1)

textseven_cheese = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_seven_cheese)
textseven_cheese.grid(row=4, column=1)

textpepperoni = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pepperoni)
textpepperoni.grid(row=5, column=1)

textham_cheese = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_ham_cheese)
textham_cheese.grid(row=6, column=1)

textbeef_onion = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_beef_onion)
textbeef_onion.grid(row=7, column=1)

texthawaiian = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_hawaiian)
texthawaiian.grid(row=8, column=1)

#Cakes
chips = Checkbutton(cakesFrame,text='Crinkle-Cut Chips',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19
                     ,command=chips)
chips.grid(row=0,column=0,sticky=W)

garlic_bread = Checkbutton(cakesFrame,text='Garlic Bread',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20
                      ,command=garlic_bread)
garlic_bread.grid(row=1,column=0,sticky=W)

onion_rings = Checkbutton(cakesFrame,text='Onion Rings',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21
                       ,command=onion_rings)
onion_rings.grid(row=2,column=0,sticky=W)

chicken_wings = Checkbutton(cakesFrame,text='Chicken Wings',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22
                        ,command=chicken_wings)
chicken_wings.grid(row=3,column=0,sticky=W)

fanta = Checkbutton(cakesFrame,text='Fanta',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23
                       ,command=fanta)
fanta.grid(row=4,column=0,sticky=W)

sprite = Checkbutton(cakesFrame,text='Sprite',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24
                        ,command=sprite)
sprite.grid(row=5,column=0,sticky=W)

water = Checkbutton(cakesFrame,text='Water',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25
                          ,command=water)
water.grid(row=6,column=0,sticky=W)

orange_juice = Checkbutton(cakesFrame,text='Orange Juice',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26
                          ,command=orange_juice)
orange_juice.grid(row=7,column=0,sticky=W)

coca_cola = Checkbutton(cakesFrame,text='Coca Cola',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27
                            ,command=coca_cola)
coca_cola.grid(row=8,column=0,sticky=W)

#entry fields for cakes

textchips = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chips)
textchips.grid(row=0, column=1)

textgarlic_bread = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_garlic_bread)
textgarlic_bread.grid(row=1, column=1)

textonion_rings = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_onion_rings)
textonion_rings.grid(row=2, column=1)

textchicken_wings = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken_wings)
textchicken_wings.grid(row=3, column=1)

textfanta = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_fanta)
textfanta.grid(row=4, column=1)

textsprite = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sprite)
textsprite.grid(row=5, column=1)

textwater = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_water)
textwater.grid(row=6, column=1)

textorange_juice = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_orange_juice)
textorange_juice.grid(row=7, column=1)

textcoca_cola = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_coca_cola)
textcoca_cola.grid(row=8, column=1)

#costlabels & entry fields

labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5
                     ,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5
                  ,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                   command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#Calculator
operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''



calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                  ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                  ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()
