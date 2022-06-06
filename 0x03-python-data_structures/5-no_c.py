#!/usr/bin/env python3
def no_c(my_string):
    my_string = "Best School Chicago C is fun!"
    
    new_string = my_string.translate({ord('c'): None, ord('C'): None})
    return new_string
