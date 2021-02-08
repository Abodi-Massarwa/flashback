# unlike strings lists are mutable
# order matters
class node :
    """
    sample node class
    """
    pass
if __name__ == '__main__':
    st = 'Print only the words that start with s in this sentence'
    s_list= [x for x in st.split(" ") if x.__contains__("s")]
    print(s_list)
    print([x for x in range(0,11,2)])

    print([x for x in range(1, 51) if x%3==0 or x%5==0])
    print([x for x in 'Print every word in this sentence that has an even number of letters'.split(" ") if len(x)%2==0])

    st = 'Create a list of the first letters of every word in this string'
    print([x[0] for x in st.split(" ")])
    x= node()
    print(help(x))