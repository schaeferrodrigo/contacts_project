# -*- coding: utf-8 -*-
#===============================================================================
import pandas as pd

# This file creates a table of contacts

def create_table():
    table = pd.DataFrame(columns = ['Name','Surname','email','Phone', 'Institution', 'City','Country','Field_Research','Position', '+info', 'ORCID number'])
    name_of_file = raw_input('What is the name of the new table?\n')
    name_of_file = 'Contacs Agenda'
    table.to_csv(name_of_file +'.csv')
    print 'The table was created\n'
