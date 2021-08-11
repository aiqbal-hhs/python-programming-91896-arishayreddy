from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

#Functions

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
    textseafod_deluxe.config(state=DISABLED)
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

        root2.title("Send Bill")
        root2.config(bg='red4')
        root2.geometry('485x620+50+50')

        logoImage=PhotoImage(file='sender.png')
        label=Label(root2,image=logoImage,bg='red4')
        label.pack(pady=5)

        numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='red4',fg='white')
        numberLabel.pack(pady=5)

        numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
        numberfield.pack(pady=5)

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
        if e_chicken_supreme.get()!='0':
            textReceipt.insert(END,f'Chicken Supreme\t\t\t{int(e_chicken_supreme.get())*10}\n\n')

        if e_chicago_style.get()!='0':
            textReceipt.insert(END,f'Chicago Style\t\t\t{int(e_chicago_style.get())*60}\n\n')

        if e_garlic_prawn.get()!='0':
            textReceipt.insert(END,f'Garlic Prawn\t\t\t{int(e_garlic_prawn.get())*100}\n\n')

        if e_seafood_deluxe.get() != '0':
            textReceipt.insert(END, f'Seafood Deluxe\t\t\t{int(e_seafood_deluxe.get()) * 30}\n\n')

        if e_cheeseburger.get() != '0':
            textReceipt.insert(END, f'Cheeseburger Pizza\t\t\t{int(e_cheeseburger.get()) * 50}\n\n')

        if e_tandoori_chicken.get() != '0':
            textReceipt.insert(END, f'Breakfast\t\t\t{int(e_tandoori_chicken.get()) * 100}\n\n')

        if e_roasted_veggie.get() != '0':
            textReceipt.insert(END, f'Roasted Veggie\t\t\t{int(e_roasted_veggie.get()) * 40}\n\n')

        if e_chicken_cranberry.get() != '0':
            textReceipt.insert(END, f'Chicken Cranberry \t\t\t{int(e_chicken_cranberry.get()) * 120}\n\n')

        if e_wedge_cheese.get() != '0':
            textReceipt.insert(END, f'Wedge Cheese\t\t\t{int(e_wedge_cheese.get()) * 120}\n\n')

        if e_hawaiian.get() != '0':
            textReceipt.insert(END, f'Hawiaan\t\t\t{int(e_hawaiian.get()) * 50}\n\n')

        if e_bbq_chicken.get() != '0':
            textReceipt.insert(END, f'BBQ Chicekn\t\t\t{int(e_bbq_chicken.get()) * 40}\n\n')

        if e_beef_onion.get() != '0':
            textReceipt.insert(END, f'Beef Onion\t\t\t{int(e_beef_onion.get()) * 80}\n\n')

        if e_veggie_trio.get() != '0':
            textReceipt.insert(END, f'Veggie Trio\t\t\t{int(e_veggie_trio.get()) * 30}\n\n')

        if e_pepperoni.get() != '0':
            textReceipt.insert(END, f'Pepperoni\t\t\t{int(e_pepperoni.get()) * 40}\n\n')

        if e_seven_cheese.get() != '0':
            textReceipt.insert(END, f'Seven Cheese\t\t\t{int(e_seven_cheese.get()) * 60}\n\n')

        if e_chicken_prawn.get() != '0':
            textReceipt.insert(END, f'Chicken Prawn \t\t\t{int(e_chicken_prawn.get()) * 20}\n\n')

        if e_cheese.get() != '0':
            textReceipt.insert(END, f'Cheese\t\t\t{int(e_cheese.get()) * 50}\n\n')

        if e_ham_cheese.get() != '0':
            textReceipt.insert(END, f'Ham and Cheese\t\t\t{int(e_ham_cheese.get()) * 80}\n\n')

        if e_water.get() != '0':
            textReceipt.insert(END, f'Water\t\t\t{int(e_water.get()) * 400}\n\n')

        if e_orange_juice.get() != '0':
            textReceipt.insert(END, f'Orange Juice\t\t\t{int(e_orange_juice.get()) * 300}\n\n')

        if e_sprite.get() != '0':
            textReceipt.insert(END, f'Sprite \t\t\t{int(e_sprite.get()) * 500}\n\n')

        if e_fanta.get() != '0':
            textReceipt.insert(END, f' Fanta \t\t\t{int(e_fanta.get()) * 450}\n\n')

        if e_chips.get() != '0':
            textReceipt.insert(END, f' Crinkle -Cut Chips\t\t\t{int(e_chips.get()) * 800}\n\n')

        if e_garlic_bread.get() != '0':
            textReceipt.insert(END, f'Garlic Bread\t\t\t{int(e_garlic_bread.get()) * 620}\n\n')

        if e_chicken_wings.get() != '0':
            textReceipt.insert(END, f'Chicken Wings \t\t\t{int(e_chicken_wings.get()) * 700}\n\n')

        if e_coca_cola.get() != '0':
            textReceipt.insert(END, f'Coca Cola\t\t\t{int(e_coca_cola.get()) * 550}\n\n')

        if e_onion_rings.get() != '0':
            textReceipt.insert(END, f' Onion Rings\t\t\t{int(e_onion_rings.get()) * 550}\n\n')

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

    else:
        messagebox.showerror('Error','No Item Is selected')



def totalcost():
    global priceofFood,priceofDrinks,priceofCakes,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_chicken_cranberry.get())
        item2=int(e_chicago_style.get())
        item3=int(e_garlic_prawn.get())
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

        priceofFood=(item1*10)+(item2*60)+(item3*100)+(item4*50)+ (item5*40) + (item6 * 30) + (item7 * 120) \
                    + (item8 * 100) + (item9 * 120)

        priceofDrinks=(item10*50)+(item11*40)+ (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 60) \
                      + (item16 * 20) + (item17 * 50) + (item18 * 80)

        priceofCakes=(item19*400)+(item20*300)+ (item21 * 500) + (item22 * 550) + (item23 * 450) + (item24 * 800) \
                     + (item25 * 620) + (item26 * 700) + (item27 * 550)

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

def e_chicago_style():
    if var2.get()==1:
        textchicago_style.config(state=NORMAL)
        textchicago_style.delete(0,END)
        textchicago_style.focus()

    else:
        textchicago_style.config(state=DISABLED)
        e_chicago.set('0')

def garlic_prawn():
    if var3.get()==1:
        textgarlic_prawn.config(state=NORMAL)
        textgarlic_prawn.delete(0,END)
        textgarlic_prawn.focus()

    else:
        textgarlic_prawn.config(state=DISABLED)
        e_fish.set('0')

def e_roasted_veggie():
    if var4.get() == 1:
        textroasted_veggie.config(state=NORMAL)
        textroasted_veggie.focus()
        textroasted_veggie.delete(0, END)
    elif var4.get() == 0:
        textroasted_veggie.config(state=DISABLED)
        e_roasted_veggie.set('0')


def cheeseburger():
    if var5.get() == 1:
        textcheeseburger.config(state=NORMAL)
        textcheeseburger.focus()
        textcheeseburger.delete(0, END)
    elif var5.get() == 0:
        textcheeseburger.config(state=DISABLED)
        e_cheeseburger.set('0')


def chicken_supreme():
    if var6.get() == 1:
        textchicken_supreme.config(state=NORMAL)
        textchicken_supreme.focus()
        textchicken_supreme.delete(0, END)
    elif var6.get() == 0:
        textchicken_supreme.config(state=DISABLED)
        e_chicken_supreme.set('0')


def seafood_deluxe():
    if var7.get() == 1:
        textseafod_deluxe.config(state=NORMAL)
        textseafod_deluxe.focus()
        textseafod_deluxe.delete(0, END)
    elif var7.get() == 0:
        textseafod_deluxe.config(state=DISABLED)
        e_seafood_deluxe.set('0')


def tandoori_chicken():
    if var8.get() == 1:
        texttandoori_chicken.config(state=NORMAL)
        texttandoori_chicken.focus()
        texttandoori_chicken.delete(0, END)
    elif var8.get() == 0:
        texttandoori_chicken.config(state=DISABLED)
        e_tandoori_chicken.set('0')


def wedge_cheese():
    if var9.get() == 1:
        textwedge_cheese.config(state=NORMAL)
        textwedge_cheese.focus()
        textwedge_cheese.delete(0, END)
    elif var9.get() == 0:
        textwedge_cheese.config(state=DISABLED)
        e_wedge_cheese.set('0')


def hawaiian():
    if var10.get() == 1:
        texthawaiian.config(state=NORMAL)
        texthawaiian.focus()
        texthawaiian.delete(0, END)
    elif var10.get() == 0:
        texthawaiian.config(state=DISABLED)
        e_hawaiian.set('0')


def cheese ():
    if var11.get() == 1:
        textcheese.config(state=NORMAL)
        textcheese.focus()
        textcheese.delete(0, END)
    elif var11.get() == 0:
        textcheese.config(state=DISABLED)
        e_cheese.set('0')


def ham_cheese():
    if var12.get() == 1:
        textham_cheese.config(state=NORMAL)
        textham_cheese.focus()
        textham_cheese.delete(0, END)
    elif var12.get() == 0:
        textham_cheese.config(state=DISABLED)
        e_ham_cheese.set('0')


def e_pepperoni():
    if var13.get() == 1:
        textpepperoni.config(state=NORMAL)
        textpepperoni.focus()
        textpepperoni.delete(0, END)
    elif var13.get() == 0:
        textpepperoni.config(state=DISABLED)
        e_pepperoni.set('0')


def e_bbq_chicken():
    if var14.get() == 1:
        textbbq_chicken.config(state=NORMAL)
        textbbq_chicken.focus()
        textbbq_chicken.delete(0, END)
    elif var14.get() == 0:
        textbbq_chicken.config(state=DISABLED)
        e_bbq_chicken.set('0')


def beef_onion():
    if var15.get() == 1:
        textbeef_onion.config(state=NORMAL)
        textbeef_onion.focus()
        textbeef_onion.delete(0, END)
    elif var15.get() == 0:
        textbeef_onion.config(state=DISABLED)
        e_beef_onion.set('0')


def veggie_trio():
    if var16.get() == 1:
        textveggie_trio.config(state=NORMAL)
        textveggie_trio.focus()
        textveggie_trio.delete(0, END)
    elif var16.get() == 0:
        textveggie_trio.config(state=DISABLED)
        e_veggie_trio.set('0')


def seven_cheese():
    if var17.get() == 1:
        textseven_cheese.config(state=NORMAL)
        textseven_cheese.focus()
        textseven_cheese.delete(0, END)
    elif var17.get() == 0:
        textseven_cheese.config(state=DISABLED)
        e_seven_cheese.set('0')


def chicken_prawn():
    if var18.get() == 1:
        textchicken_prawn.config(state=NORMAL)
        textchicken_prawn.focus()
        textchicken_prawn.delete(0, END)
    elif var18.get() == 0:
        textchicken_prawn.config(state=DISABLED)
        e_chicken_prawn.set('0')


def coca_cola():
    if var19.get() == 1:
        textcoca_cola.config(state=NORMAL)
        textcoca_cola.focus()
        textcoca_cola.delete(0, END)
    elif var19.get() == 0:
        textcoca_cola.config(state=DISABLED)
        e_coca_cola.set('0')


def water():
    if var20.get() == 1:
        textwater.config(state=NORMAL)
        textwater.focus()
        textwater.delete(0, END)
    elif var20.get() == 0:
        textwater.config(state=DISABLED)
        e_water.set('0')


def fanta():
    if var21.get() == 1:
        textfanta.config(state=NORMAL)
        textfanta.focus()
        textfanta.delete(0, END)
    elif var21.get() == 0:
        textfanta.config(state=DISABLED)
        e_fanta.set('0')


def sprite():
    if var22.get() == 1:
        textsprite.config(state=NORMAL)
        textsprite.focus()
        textsprite.delete(0, END)
    elif var22.get() == 0:
        textsprite.config(state=DISABLED)
        e_sprite.set('0')


def water():
    if var23.get() == 1:
        textwater.config(state=NORMAL)
        textwater.focus()
        textwater.delete(0, END)
    elif var23.get() == 0:
        textwater.config(state=DISABLED)
        e_water.set('0')


def chips():
    if var24.get() == 1:
        textchips.config(state=NORMAL)
        textchips.focus()
        textchips.delete(0, END)
    elif var24.get() == 0:
        textchips.config(state=DISABLED)
        e_chips.set('0')


def garlic_bread():
    if var25.get() == 1:
        textgarlic_bread.config(state=NORMAL)
        textgarlic_bread.focus()
        textgarlic_bread.delete(0, END)
    elif var25.get() == 0:
        textgarlic_bread.config(state=DISABLED)
        e_garlic_bread.set('0')


def onion_rings():
    if var26.get() == 1:
        textonion_rings.config(state=NORMAL)
        textonion_rings.focus()
        textonion_rings.delete(0, END)
    elif var26.get() == 0:
        textonion_rings.config(state=DISABLED)
        e_onion_rings.set('0')


def chicken_wings():
    if var27.get() == 1:
        textchicken_wings.config(state=NORMAL)
        textchicken_wings.focus()
        textchicken_wings.delete(0, END)
    elif var27.get() == 0:
        textchicken_wings.config(state=DISABLED)
        e_chicken_wings.set('0')



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

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
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
e_roasted_veggie = StringVar()
e_seafood_deluxe = StringVar()
e_paneer = StringVar()

e_cheese=StringVar()
e_seven_cheese = StringVar()
e_pepperoni = StringVar()
e_bbq_chicken = StringVar()
e_ = StringVar()
e_veggie_trio = StringVar()
e_hawaiian = StringVar()
e_ = StringVar()
e_coldrinks = StringVar()

e_water = StringVar()
e_orange_juice = StringVar()
e_fanta = StringVar()
e_sprite = StringVar()
e_coca_cola = StringVar()
e_chicken_wings = StringVar()
e_onion_rings = StringVar()
e_garlic_bread = StringVar()
e_chips = StringVar()

