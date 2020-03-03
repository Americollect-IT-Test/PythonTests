import numpy as np
def find_all_letter(string_val):
    ''' prints all characters one by one'''

    for i in string_val:
        print (i)


def random_generator(shuff_list=['AMERICOL','AMERIEBO']):

    return  np.random.choice(shuff_list)

    
find_all_letter(random_generator())



