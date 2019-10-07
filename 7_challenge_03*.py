# http://tinyurl.com/z2m2115

numbers = [2,5,8]

while True:
    n = input("Input number:")
    if n == "q":
        break

    try:
        # input returns str type
        n = int(n)
    except ValueError:
        print("input number or q to quit.")

    if n in numbers:
        print("correct!")
        break
    else:
        print("incorrect...")
