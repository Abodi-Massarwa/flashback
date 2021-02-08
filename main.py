
if __name__ == '__main__':
    #  print_hi('PyCharm')
    # TODO: due to python's enormous power of Dynamic Typing with each advantage comes a disadvantage
    # TODO: since we can freely assign any desired value of any desired type to the same variable as much as we wish to
    # TODO: such power makes us fall easily for it , but it could lead to obscure results
    a = 5
    a = (1, 2)
    a += a
    a = [1, 2, 3, 4, 5]
    a = {1: 1.2, 2: 2.3}

    # TODO: an easy tool provided by python could help us determine the type of each variable whenever & however we
    #  want to
    a = 5
    print(type(a))
    a = (1, 2)
    print(type(a))
    a = {1: {2: 3}}
    print(type(a))
