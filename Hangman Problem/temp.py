function_call = 0
def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    global function_call 
    function_call += 1 
    print(x, a, function_call)
    
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
        
        
rem(7, 5)        