# http://tinyurl.com/...

def f(a,b,c,d=1,e=2):
    """
    Returns caluculation of a-e
    :input a: int.
    :input b: int.
    :input c: int.
    :input d: int, optional.
    :input e: int, optional.
    :return: (a+b+c)*d*e
    """
    return (a+b+c)*d*e

result = f(1,1,1,3)
print(result)
