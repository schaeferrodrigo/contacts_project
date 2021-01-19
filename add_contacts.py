# -*- coding: utf-8 -*-
#===============================================================================
import pandas as pd

# File to add contacts in the table


def add_contact(name,surname , email,phone, inst, city,country,field , position ,info , ORCID):
    table = pd.read_csv('tables_folder/Contacts_Agenda.csv')
    table = table.append(pd.Series({'Name' : name , 'Surname': surname, 'email' : email, 'Phone': phone, 'Institution' : inst, 'City' : city,'Country' : country,'Research_Field': field,'Position': position, '+info' : info , 'ORCID number': ORCID}), ignore_index = True)
    table.to_csv('tables_folder/Contacts_Agenda.csv') #listar agendas criadas
    print('The data was inserted.\n')

def insert_data():
    data_to_insert = []
    name = input('What is his/her name?\n')
    surname =  input('What is his/her surname?\n')
    email = input('What is his/her email?\n')
    phone = input('What is his/her phone?\n')
    inst = input('What is his/her Institution?\n')
    city = input('What is his/her City?\n')
    country = input('What is his/her Country?\n')
    field = input('What is his/her field?\n')
    position = input('What is his/her position?\n')
    info = input('Some additional info?\n')
    ORCID = input('What is his/her ORCID?\n')
    add_contact(name,surname , email,phone, inst, city,country,field , position ,info, ORCID)




#add_contact('Amadeu' , 'Delshams', 'amadeu.delshams@upc.edu','Universitat Politecnica de Catalunya', 'Barcelona', 'Catalonia','dynamical systems','Dean',' ')
