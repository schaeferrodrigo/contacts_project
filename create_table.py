# -*- coding: utf-8 -*-
#===============================================================================
import pandas as pd

# This file creates a table of contacts

def create_table():
    table = pd.DataFrame(columns = ['Name','Surname','email','Phone', 'Institution', 'City','Country','Field_Research','Position', '+info', 'ORCID number'])
    #name_of_file = input('What is the name of the new table?\n')
    name_of_file = 'Contacts_Agenda'
    table.to_csv('tables_folder/'+name_of_file +'.csv')
    print( 'The table was created\n')
