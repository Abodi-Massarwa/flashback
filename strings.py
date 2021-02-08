# TODO: string type in python accepts '' and ""


if __name__ == '__main__':
    a = "45"
    print(type(a))
    a = '45'
    print(type(a))
    print(a.__contains__("4"))
    # TODO: string indexing
    a = "abodi"
    print(a[1:2])  # grab substring from index 1 to 2-1
    print(a[::-1])  # grab a string but backwards
    print(a[:len(a) - 1])  # grab string till len(a)-2 excluding len(a)-1

    # TODO : REMEMBER STR IS IMMUTABLE (can't be changed)
    # TODO : it can be modified only by using the operator += to add a letter-string to it's end
    a += "98"
    print(a)
    print(a*3) # printing abodi98 3 times is possible with a simple operator which is (TODO: *)
    a=a.upper()
    print(a)

    a=a.lower()
    print(a)
    print(a.split("i"))
    print(type (a.split()))
    #TODO print formatting to insert additional things such as string taken from an argument of function
    b="Massarweh"
    print(f"{a[:len(a)-2].upper()} {b.upper()}")
    print("{} {}".format(b,b))
    num=5.123456789
    print(f"{num:10.6f}")
