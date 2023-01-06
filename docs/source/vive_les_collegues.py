import tkinter as tk    #import tkinter
from tkinter import ttk, messagebox,ttk
from csv import DictWriter
from tkcalendar import *

import os 

#Create button code action function
def action():
    """
    this function is used to :

    Get the 4 infos : name, last name, date, poste
    
    write it to the csv files

    
    
    
    """
    usernom = nom_var.get()
    userprenom = prenom_var.get()
    userdate_arrivee = date_arrivee_var.get()
    userposte = poste_var.get()
    #change value 0,1 to Yes or No

    #write to csv file code here
    with open('liste_employe.csv', 'a', newline = '') as f:
        dict_writer = DictWriter(f, fieldnames=['Nom', 'Prenom', 'Date','Poste'])
        if os.stat('liste_employe.csv').st_size == 0:        #if file is not empty than header write else not
            dict_writer.writeheader()
       
        dict_writer.writerow({
            'Nom' : usernom,
            'Prenom' : userprenom,
            'Date' : userdate_arrivee,
            'Poste' : userposte,
        })
    #Change color after submit button
    nom_entrybox.delete(0, tk.END)
    prenom_entrybox.delete(0, tk.END)
    date_arrivee_entrybox.delete(0, tk.END)
    nom_label.configure(foreground = 'Blue')
    prenom_label.configure(foreground = 'Blue')
    date_arrivee_label.configure(foreground = 'Blue')
    poste_label.configure(foreground = 'Blue')

if __name__ == "__main__":
    
    win = tk.Tk()
    win.title('Information Store')    #give a title name

    #create labels
    #name label
    nom_label = ttk.Label(win,text = "Nom : ")
    nom_label.grid(row=0, column=0, sticky = tk.W)

    #prenom label
    ''' 
    This is use to create a box to entry the name of your collegue

    '''
    prenom_label = ttk.Label(win,text = "Prenom: ")
    prenom_label.grid(row=1, column = 0, sticky = tk.W)

    #date d'arrivé number label
    date_arrivee_label = ttk.Label(win, text = "Date d'arrivée : ")
    date_arrivee_label.grid(row=2, column = 0, sticky =tk.W)

    #poste label
    poste_label = ttk.Label(win,text = "Selectionnez le poste : ")
    poste_label.grid(row=4, column = 0, sticky = tk.W)

    #Create entry box
    #nom entry box
    nom_var = tk.StringVar()
    nom_entrybox = ttk.Entry(win, width = 16, textvariable = nom_var)
    nom_entrybox.grid(row=0 , column = 1)
    nom_entrybox.focus()

    #prenom entry box
    prenom_var = tk.StringVar()
    prenom_entrybox = ttk.Entry(win, width = 16, textvariable = prenom_var)
    prenom_entrybox.grid(row = 1, column = 1)

    #date entry box
    date_arrivee_var = tk.StringVar()
    date_arrivee_entrybox = DateEntry(win,width = 16, textvariable= date_arrivee_var)
    date_arrivee_entrybox.grid(row=2, column =1)


    #poste entry box
    #create combobox
    poste_var = tk.StringVar()
    poste_combobox = ttk.Combobox(win,width = 13, textvariable = poste_var, state="readonly")
    poste_combobox['values'] = open("liste_postes.txt", "r").read()
    poste_combobox.current(0)
    poste_combobox.grid(row = 4, column=1)



    #submit button
    submit_button = ttk.Button(win, text = "Submit", command = action)  
    submit_button.grid(row=7, column=0)
    win.mainloop()   