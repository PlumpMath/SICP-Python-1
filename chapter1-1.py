Q1
from operator import add, sub
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs."""
    if b < 0:
        op = sub
    else:
        op = add
    return op(a, b)

#################    


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition == 1:
        return true_result
    else:
        return  false_result

import random
def c():
	return random.randint(1,100)

def t():
	return 1

def f():
	return 'more than 1'	
	


