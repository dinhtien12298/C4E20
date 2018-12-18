def get_even_list(l):
    for index, item in enumerate(l):
        if item % 2 != 0:
            del l[index]
    print(l)
    
    return l


