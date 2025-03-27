from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox 
import pymongo 
from pip import *
fenetre1 = Tk ()
fenetre1. geometry('1300x600')
fenetre1. title ('Gestion des locations des bus ')
fenetre1. resizable (height=True, width=True)



def interface2() :
    fenetre = Tk ()
    fenetre. geometry('1000x300')
    fenetre. title ('Gestion des bus ')
    fenetre. resizable (height=True, width=True)
    
    def ajout():
       conx = pymongo.MongoClient(host="localhost" ,port=27017)
       Imm=E7.get()
       Da=E2.get()
       Ca=E3.get()
       db=conx.BUS1
       L=[]
       nb=0
       if (Imm!="" and Da!="" and Ca!=""):
           bus= {'Immatriculation':Imm,
                  'Date dacquisition':Da,
                    'Capacite':Ca}
           for i in db.gestion.find():
               L.append(i["Immatriculation"])
           if ((Imm in L)):
               messagebox.showinfo("Attention!","Ce matricule existe déja dans la base")
               for i in db.gestion.find():
                   if (Imm==i["Immatriculation"]):
                       E2.delete(0,END)
                       E3.delete(0,END)
                       E2.insert(0,i["Date dacquisition"])
                       E3.insert(0,i["Capacite"])
                       for i in db.g_loc.find():
                            if(Imm==i["Matricule"]):
                                label = Label(fenetre, text= i["Montant"])
                                label. place(x='550', y= '80')
                       for i in db.g_loc.find():
                            if (Imm==i['Matricule']):
                                nb+=1
                       label = Label(fenetre, text= nb)
                       label. place(x='550', y= '50')
                       
           else:
               db.gestion.insert_one(bus)
               messagebox.showinfo("Action","Ajout avec succés")
               E7.delete(0,END)
               E2.delete(0,END)
               E3.delete(0,END)
       else:
           messagebox.showinfo("Attention!","Remplir tous champs")
           E7.delete(0,END)
           E2.delete(0,END)
           E3.delete(0,END)
       
       
               
        
    def supp():
       conx = pymongo.MongoClient(host="localhost" ,port=27017)
       Imm=E7.get()
       Da=E2.get()
       Ca=E3.get()
       db=conx.BUS1
       L=[]
       if (Imm!=""):
           bus= {"Immatriculation": Imm}
           bus1= {"Date dacquisition": Da}
           bus2= {"Capacite": Ca}
           for i in db.gestion.find():
               L.append(i["Immatriculation"])
           if (Imm in L):
                db.gestion.delete_one(bus)
                db.gestion.delete_one(bus1)
                db.gestion.delete_one(bus2)
                messagebox.showinfo("Action","Suppression avec succés")
           else:
               messagebox.showinfo("Attention!","Cette élement n'existe pas dans la base!")
               E7.delete(0,END)
               E2.delete(0,END)
               E3.delete(0,END)
       else:
            messagebox.showinfo("Attention!","Le champ Immatriculation est obligatoire!!")
       
       E7.delete(0,END)
       E2.delete(0,END)
       E3.delete(0,END)

    def annuler():
       E7.delete(0,END)
       E2.delete(0,END)
       E3.delete(0,END)
       
       
    def search():
        conx = pymongo.MongoClient(host="localhost" ,port=27017)
        Imm=E7.get()
        Da=E2.get()
        Ca=E3.get()
        db=conx.BUS1
        nb=0
        if (Imm!="" or Da!="" or Ca!=""):
            for i in db.gestion.find():
                if (Imm==i["Immatriculation"]):
                    E2.insert(0,i["Date dacquisition"])
                    E3.insert(0,i["Capacite"])
            
            for i in db.g_loc.find():
                if(Imm==i["Matricule"]):
                    label = Label(fenetre, text= i["Montant"])
                    label. place(x='550', y= '80')
            for i in db.g_loc.find():
                if (Imm==i['Matricule']):
                    nb+=1
            label = Label(fenetre, text= nb)
            label. place(x='550', y= '50')
        else:
            messagebox.showinfo("Attention!","Remplir au moins une champ")
                


    def interface31():
        fenetre = Tk ()
        fenetre. geometry('1000x500')
        fenetre. title ('Gestion des locations ')
        fenetre. resizable (height=True, width=True)
        conx = pymongo.MongoClient(host="localhost" ,port=27017)
        db=conx.BUS1
        Imm=E7.get()
        L=[]
        tree = ttk.Treeview(fenetre , columns =(1,2,3) , heigh = 5 , show = 'headings' )
        tree.place(x = '150' , y = '250' , width = '650' , height = '175')
        tree.heading(1 , text = "Date")
        tree.heading(2 , text = "Type")
        tree.heading(3 , text = "Montant")
        for i in tree.get_children():
            tree.delete(i)
        for i in db.g_loc.find():
            if (Imm==i["Matricule"]):
                tree.insert("","end",values=(i["Date location"],i["Type"],i["Montant"]))
            
       
            
        def ajout():
           conx = pymongo.MongoClient(host="localhost" ,port=27017)
           Dl=E5.get()
           Nj=E1.get()
           Ty=E2.get()
           Mo=E3.get()
           E=E4.get()
           M=listcombo.get()
           db=conx.BUS1
           L=[]
           
           if (Dl!="" and Nj!="" and Ty!="" and Mo!="" and E!=""and M!=""):
               for i in db.g_loc.find():
                   if (Dl==i["Date location"] and M==i["Matricule"]):
                       L.append(Dl)
                       L.append(M)
               if ((Dl in L) and (M in L)):
                   messagebox.showinfo("Attention!","Ce bus est déja louer a cette date")
               else:
                   bus= {'Matricule':M,
                         'Date location':Dl,
                          'Nombre de jours':Nj,
                            'Type':Ty,
                              'Montant':Mo,
                                'E-mail':E}
                   db.g_loc.insert_one(bus)
                   tree.insert('',END,values=(Dl,Ty,Mo))
                   messagebox.showinfo("Action","Ajout avec succés")
           else:
               messagebox.showinfo("Attention!","Remplir tous champs")

           E5.delete(0,END)
           E1.delete(0,END)
           E2.delete(0,END)
           E3.delete(0,END)
           E4.delete(0,END)
           listcombo.delete(0,END)

        def supp():
           conx = pymongo.MongoClient(host="localhost" ,port=27017)
           Dl=E5.get()
           Nj=E1.get()
           Ty=E2.get()
           Mo=E3.get()
           E=E4.get()
           M=listcombo.get()
           db=conx.BUS1
           L=[]
           if (Dl!="" and  M!=""):
               bus= {'Date location':Dl}
               bus1= {'Nombre de jours':Nj}
               bus2= {'Type':Ty}
               bus3= {'Montant':Mo}
               bus4= {'E-mail':E}
               bus5= {'Matricule':M}
               for i in db.g_loc.find():
                   if (Dl==i["Date location"] and M==i["Matricule"]):
                       L.append(Dl)
                       L.append(M)
               
               if ((Dl in L)and(M in L)):
                    db.g_loc.delete_one(bus)
                    db.g_loc.delete_one(bus1)
                    db.g_loc.delete_one(bus2)
                    db.g_loc.delete_one(bus3)
                    db.g_loc.delete_one(bus4)
                    db.g_loc.delete_one(bus5)
                    for i in tree.get_children():
                        tree.delete(i)
                    for i in db.g_loc.find():
                        tree.insert("","end",values=(i["Date location"],i["Type"],i["Montant"]))
                    messagebox.showinfo("Action","Suppression avec succés")
               else:
                   messagebox.showinfo("Attention!","Cette élement n'existe pas dans la base")
                   E5.delete(0,END)
                   E1.delete(0,END)
                   E2.delete(0,END)
                   E3.delete(0,END)
                   E4.delete(0,END)
                   listcombo.delete(0,END)
            
           else:
                messagebox.showinfo("Attention!","les champs Matricule et Date location sont obligatoire!")
                
           E5.delete(0,END)
           E1.delete(0,END)
           E2.delete(0,END)
           E3.delete(0,END)
           E4.delete(0,END)
           listcombo.delete(0,END)
           
        def search():
            conx = pymongo.MongoClient(host="localhost" ,port=27017)
            M=listcombo.get()
            Dl=E5.get()
            Nj=E1.get()
            Ty=E2.get()
            Mo=E3.get()
            E=E4.get()
            L=[]
            if (Dl!="" or Nj!="" or Ty!=""or Mo!=""or E!=""or M!=""):
                for i in db.g_loc.find():
                    if (M==i["Matricule"]):
                        L.append(i["Matricule"])
                if (M in L):
                    E1.insert(0,i["Nombre de jours"])
                    E2.insert(0,i["Type"])
                    E3.insert(0,i["Montant"])
                    E4.insert(0,i["E-mail"])
                    E5.insert(0,i["Date location"])
                else:
                    messagebox.showinfo("Attention!","Ce matricule n'existe pas")
                    E5.delete(0,END)
                    E1.delete(0,END)
                    E2.delete(0,END)
                    E3.delete(0,END)
                    E4.delete(0,END)
                    listcombo.delete(0,END)
            else:
                messagebox.showinfo("Attention!","Remplir au moins une champ")
            
            
        def annuler():
            E5.delete(0,END)
            E1.delete(0,END)
            E2.delete(0,END)
            E3.delete(0,END)
            E4.delete(0,END)
            listcombo.delete(0,END)


        def action(event):
            select = listcombo.get()


        L=[]
        for i in db.gestion.find():
                L.append(i["Immatriculation"])
        listcombo=ttk.Combobox(fenetre,values=L)
        
        listcombo.bind("<<ComboboxSelected>>",action)
        listcombo.place (x='450', y= '50')
            
        label = Label(fenetre, text= "Locations", font=("Verdana", 10))
        label. place(x='5', y= '5')
        label = Label(fenetre, text= "Matricule :")
        label. place(x='57', y= '50')
        label = Label(fenetre, text= "Date locations :")
        label. place(x='50', y= '80')
        label = Label(fenetre, text= "Nombre de jours :")
        label. place(x='45', y= '110')
        label = Label(fenetre, text= "Type :")
        label. place(x='68', y= '140')
        label = Label(fenetre, text= "Montant :")
        label. place(x='58', y= '170')
        label = Label(fenetre, text= "E-mail :")
        label. place(x='63', y= '200')
        E5= Entry(fenetre)
        E5.place(x='450', y= '80')
        E1 = Entry(fenetre)
        E1.place(x='450', y= '110')
        E2 = Entry(fenetre)
        E2.place(x='450', y= '140')
        E3 = Entry(fenetre)
        E3.place(x='450', y= '170')
        E4 = Entry(fenetre)
        E4.place(x='450', y= '200')
        B = Button(fenetre, text="Ajouter" , font=("Verdana", 10), command=ajout)
        B.place(x='759', y= '50')
        B1 = Button(fenetre, text="Supprimer" , font=("Verdana", 10),command=supp)
        B1.place(x='750', y= '80')
        B2= Button(fenetre, text="Annuler" , font=("Verdana", 10), command=annuler)
        B2.place(x='757', y= '110')
        B3= Button(fenetre, text="Imprimer" , font=("Verdana", 10))
        B3.place(x='850', y= '400')
        B4 = Button(fenetre, text="Search" , font=("Verdana", 10),command=search)
        B4.place(x='760', y= '140')

    
    label = Label(fenetre, text= "Bus", font=("Verdana", 10))
    label. place(x='5', y= '5')
    label = Label(fenetre, text= "Immatriculation :")
    label. place(x='53', y= '50')
    label = Label(fenetre, text= "Date d'acquisition :")
    label. place(x='50', y= '80')
    label = Label(fenetre, text= "Capacité :")
    label. place(x='70', y= '110')
    label = Label(fenetre, text= "Nombre de locations :")
    label. place(x='403', y= '50')
    label = Label(fenetre, text= "Montant des locations :")
    label. place(x='400', y= '80')
    B = Button(fenetre, text="Ajouter" , font=("Verdana", 10), command=ajout)
    B.place(x='759', y= '50')
    B1 = Button(fenetre, text="Supprimer" , font=("Verdana", 10), command=supp)
    B1.place(x='750', y= '80')
    B2 = Button(fenetre, text="Annuler" , font=("Verdana", 10), command=annuler)
    B2.place(x='757', y= '110')
    B3 = Button(fenetre, text="Locations" , font=("Verdana", 10),command=interface31)
    B3.place(x='750', y= '140')
    B4 = Button(fenetre, text="Search" , font=("Verdana", 10),command=search)
    B4.place(x='755', y= '170')
    E7 = Entry(fenetre)
    E7.place(x='220', y= '50')
    global x
    x= StringVar()
    E2 = Entry(fenetre, textvariable =x)
    E2.place(x='220', y= '80')
    global y
    y= StringVar()
    E3 = Entry(fenetre, textvariable=y)
    E3.place(x='220', y= '110')




def interface3():
    fenetre = Tk ()
    fenetre. geometry('1000x500')
    fenetre. title ('Gestion des locations ')
    fenetre. resizable (height=True, width=True)
    conx = pymongo.MongoClient(host="localhost" ,port=27017)
    db=conx.BUS1
    
    tree = ttk.Treeview(fenetre , columns =(1,2,3) , heigh = 5 , show = 'headings' )
    tree.place(x = '150' , y = '250' , width = '650' , height = '175')
    tree.heading(1 , text = "Date")
    tree.heading(2 , text = "Type")
    tree.heading(3 , text = "Montant")
    for i in db.g_loc.find():
            tree.insert("","end",values=(i["Date location"],i["Type"],i["Montant"]))
        
    def ajout():
       conx = pymongo.MongoClient(host="localhost" ,port=27017)
       Dl=E5.get()
       Nj=E1.get()
       Ty=E2.get()
       Mo=E3.get()
       E=E4.get()
       M=listcombo.get()
       db=conx.BUS1
       L=[]
       
       if (Dl!="" and Nj!="" and Ty!="" and Mo!="" and E!=""and M!=""):
           for i in db.g_loc.find():
               if (Dl==i["Date location"] and M==i["Matricule"]):
                   L.append(Dl)
                   L.append(M)
           if ((Dl in L) and (M in L)):
               messagebox.showinfo("Attention!","Ce bus est déja louer a cette date")
           else:
               bus= {'Matricule':M,
                     'Date location':Dl,
                      'Nombre de jours':Nj,
                        'Type':Ty,
                          'Montant':Mo,
                            'E-mail':E}
               db.g_loc.insert_one(bus)
               tree.insert('',END,values=(Dl,Ty,Mo))
               messagebox.showinfo("Action","Ajout avec succés")
       else:
           messagebox.showinfo("Attention!","Remplir tous champs")

       E5.delete(0,END)
       E1.delete(0,END)
       E2.delete(0,END)
       E3.delete(0,END)
       E4.delete(0,END)
       listcombo.delete(0,END)

    def supp():
       conx = pymongo.MongoClient(host="localhost" ,port=27017)
       Dl=E5.get()
       Nj=E1.get()
       Ty=E2.get()
       Mo=E3.get()
       E=E4.get()
       M=listcombo.get()
       db=conx.BUS1
       L=[]
       if (Dl!="" and  M!=""):
           bus= {'Date location':Dl}
           bus1= {'Nombre de jours':Nj}
           bus2= {'Type':Ty}
           bus3= {'Montant':Mo}
           bus4= {'E-mail':E}
           bus5= {'Matricule':M}
           for i in db.g_loc.find():
               if (Dl==i["Date location"] and M==i["Matricule"]):
                   L.append(Dl)
                   L.append(M)
           
           if ((Dl in L)and(M in L)):
                db.g_loc.delete_one(bus)
                db.g_loc.delete_one(bus1)
                db.g_loc.delete_one(bus2)
                db.g_loc.delete_one(bus3)
                db.g_loc.delete_one(bus4)
                db.g_loc.delete_one(bus5)
                for i in tree.get_children():
                    tree.delete(i)
                for i in db.g_loc.find():
                    tree.insert("","end",values=(i["Date location"],i["Type"],i["Montant"]))
                messagebox.showinfo("Action","Suppression avec succés")
           else:
               messagebox.showinfo("Attention!","Cette élement n'existe pas dans la base")
               E5.delete(0,END)
               E1.delete(0,END)
               E2.delete(0,END)
               E3.delete(0,END)
               E4.delete(0,END)
               listcombo.delete(0,END)
        
       else:
            messagebox.showinfo("Attention!","les champs Matricule et Date location sont obligatoire!")
            
       E5.delete(0,END)
       E1.delete(0,END)
       E2.delete(0,END)
       E3.delete(0,END)
       E4.delete(0,END)
       listcombo.delete(0,END)
       
    def search():
        conx = pymongo.MongoClient(host="localhost" ,port=27017)
        M=listcombo.get()
        Dl=E5.get()
        Nj=E1.get()
        Ty=E2.get()
        Mo=E3.get()
        E=E4.get()
        L=[]
        if (Dl!="" or Nj!="" or Ty!=""or Mo!=""or E!=""or M!=""):
            for i in db.g_loc.find():
                if (M==i["Matricule"]):
                    L.append(i["Matricule"])
            if (M in L):
                E1.insert(0,i["Nombre de jours"])
                E2.insert(0,i["Type"])
                E3.insert(0,i["Montant"])
                E4.insert(0,i["E-mail"])
                E5.insert(0,i["Date location"])
            else:
                messagebox.showinfo("Attention!","Ce matricule n'existe pas")
                E5.delete(0,END)
                E1.delete(0,END)
                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)
                listcombo.delete(0,END)
        else:
            messagebox.showinfo("Attention!","Remplir au moins une champ")
        
        
    def annuler():
        E5.delete(0,END)
        E1.delete(0,END)
        E2.delete(0,END)
        E3.delete(0,END)
        E4.delete(0,END)
        listcombo.delete(0,END)


    def action(event):
        select = listcombo.get()


    L=[]
    for i in db.gestion.find():
            L.append(i["Immatriculation"])
    listcombo=ttk.Combobox(fenetre,values=L)
    listcombo.current(0)
    listcombo.bind("<<ComboboxSelected>>",action)
    listcombo.place (x='450', y= '50')
        
    label = Label(fenetre, text= "Locations", font=("Verdana", 10))
    label. place(x='5', y= '5')
    label = Label(fenetre, text= "Matricule :")
    label. place(x='57', y= '50')
    label = Label(fenetre, text= "Date locations :")
    label. place(x='50', y= '80')
    label = Label(fenetre, text= "Nombre de jours :")
    label. place(x='45', y= '110')
    label = Label(fenetre, text= "Type :")
    label. place(x='68', y= '140')
    label = Label(fenetre, text= "Montant :")
    label. place(x='58', y= '170')
    label = Label(fenetre, text= "E-mail :")
    label. place(x='63', y= '200') 
    E5= Entry(fenetre)
    E5.place(x='450', y= '80')
    E1 = Entry(fenetre)
    E1.place(x='450', y= '110')
    E2 = Entry(fenetre)
    E2.place(x='450', y= '140')
    E3 = Entry(fenetre)
    E3.place(x='450', y= '170')
    E4 = Entry(fenetre)
    E4.place(x='450', y= '200')
    B = Button(fenetre, text="Ajouter" , font=("Verdana", 10), command=ajout)
    B.place(x='759', y= '50')
    B1 = Button(fenetre, text="Supprimer" , font=("Verdana", 10),command=supp)
    B1.place(x='750', y= '80')
    B2= Button(fenetre, text="Annuler" , font=("Verdana", 10), command=annuler)
    B2.place(x='757', y= '110')
    B3= Button(fenetre, text="Imprimer" , font=("Verdana", 10))
    B3.place(x='850', y= '400')
    B4 = Button(fenetre, text="Search" , font=("Verdana", 10),command=search)
    B4.place(x='760', y= '140')

    


def exit():
    fenetre1.destroy()

frame = LabelFrame(fenetre1, padx='10', pady='10')
frame.place(x='150',y='100')
photo = PhotoImage(file='bus.png')
label = Label(frame, image=photo)
label.pack()

frame = LabelFrame(fenetre1, padx='10', pady='10')
frame.place( x='700',y='100')
photoo = PhotoImage(file='clo.png')
label = Label(frame, image=photoo)
label. pack()


bouton = Button(fenetre1,text="Gestion des bus", font=("Verdana", 10),command=interface2)
bouton.place(x='280', y= '60')

bouton = Button(fenetre1,text="Gestion des locations", font=("Verdana", 10),command=interface3)
bouton.place(x='280', y= '500')

bouton1 = Button(fenetre1,text="Exit", font=("Verdana", 10),command=exit)
bouton1.place(x='900', y= '500')
fenetre1. mainloop()
