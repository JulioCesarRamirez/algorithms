def add_one(given):
    strings = [str(integer) for integer in given]
    a_string = "".join(strings)
    an_integer = int(a_string) + 1
    res = [int(x) for x in str(an_integer)]
    return res


giv = [1, 2, 9, 9]
print(add_one(giv))
