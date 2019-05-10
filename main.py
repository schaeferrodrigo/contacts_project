# -*- coding: utf-8 -*-
#===============================================================================
from create_table import *
from add_contacts import *


first_step = 0


while first_step != 'exit':
    first_step = raw_input('Hello, what do you want to do?\n a. CREATE table \n b. INSERT entry \n c. UPDATE entry \n d. SEARCH an entry \n e. CONFIG\n Digit exit to close\n\n')
    if first_step == 'a':
        conf = raw_input('Are you sure?(y/n)\n\n')
        if conf == 'y':
            table_contacts = create_table()
        elif conf =='n':
            pass
    elif first_step == 'b':
        insert_data()
    elif first_step == 'c':
        pass
    elif first_step == 'd':
        pass
    elif first_step == 'exit':
        exit()
    else:
        pass
