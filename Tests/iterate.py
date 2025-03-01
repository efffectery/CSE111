lol = [ "hi", "there" ]

def count_sumthing(lol):

    for first_char, *_ in lol:
        print(first_char)

count_sumthing(lol)