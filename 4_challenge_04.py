# http://tinyurl.com/...

def f1(x):
    """
    Returns x 2nd.
    :input x: int.
    :return: x/2.
    """
    return int(x/2)

def f2(x):
    """
    Returns x times 4.
    :input x: int.
    :return: x*4.
    """
    return int(x*4)

result1 = f1(2)
result2 = f2(result1)

print(str(result1)+", "+str(result2))
