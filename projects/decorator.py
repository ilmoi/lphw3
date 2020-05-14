"""playing with simple decorators"""

def decorator(func):
    def wrapper(): #note how you DONT pass func() into the wrapper here
        print('predecorating...')
        func()
        print('postdecorating')

    return wrapper #note how this has to be returned as an object, not called

# =========== OPTION 1 ===========
# def sunshine():
#     print('todays sunny!')
#
# sunshine = decorator(sunshine)
# sunshine()

# =========== OPTION 2 ===========
@decorator
def sunshine():
    print('todays sunny!')

sunshine()

# takes in any number of params, and stores them as TUPLE
def self_expo(*args):
    for a in args:
        print(a**a)

self_expo(1)
self_expo(2)
self_expo(3)
self_expo(1,2,3)

#takes in any number of params in the format: param_name=param, and stores them as DICT
def self_expoz(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])

self_expoz(a=1)
self_expoz(b=2)
self_expoz(c=3)
self_expoz(a=1,b=2,c=3)

#good boilerplate

import functools

def decorator(func):

    @functools.wraps(func) #this is to ensure help works correcly

    def wrapper_decorator(*args, **kwargs): #note arguments
        # Do something before the func runs
        value = func(*args, **kwargs)
        # Do something after the func runs
        return value

    return wrapper_decorator #note just object
