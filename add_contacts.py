# -*- coding: utf-8 -*-
#===============================================================================
import pandas as pd

# File to add contacts in the table


def add_contact(name,surname , email,phone, inst, city,country,field , position ,info , ORCID):
    table = pd.read_csv('Contacts Agenda.csv')
    table = table.append(pd.Series({'Name' : name , 'Surname': surname, 'email' : email, 'Phone': phone, 'Institution' : inst, 'City' : city,'Country' : country,'Field_Research': field,'Position': position, '+info' : info , 'ORCID number': ORCID}), ignore_index = True)
    table.to_csv('Contacts Agenda.csv') #listar agendas criadas
    print 'The data was inserted.\n'

def insert_data():
    data_to_insert = []
    name = raw_input('What is his/her name?\n')
    surname =  raw_input('What is his/her surname?\n')
    email = raw_input('What is his/her email?\n')
    phone = raw_input('What is his/her phone?\n')
    inst = raw_input('What is his/her Institution?\n')
    city = raw_input('What is his/her City?\n')
    country = raw_input('What is his/her Country?\n')
    field = raw_input('What is his/her field?\n')
    position = raw_input('What is his/her position?\n')
    info = raw_input('Some additional info?\n')
    ORCID = raw_input('What is his/her ORCID?\n')
    add_contact(name,surname , email,phone, inst, city,country,field , position ,info, ORCID)




#add_contact('Amadeu' , 'Delshams', 'amadeu.delshams@upc.edu','Universitat Politecnica de Catalunya', 'Barcelona', 'Catalonia','dynamical systems','Dean',' ')
