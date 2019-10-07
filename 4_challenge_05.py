# http://tinyurl.com/hkzgqrv

def f(x):
    """
    Returns return float from str
    :param x: str
    return float x
    """
    try:
        return float(x)
    except ValueError:
        print("Invalit Input x!")

x = "abcd"
result = f(x)
print(result)
