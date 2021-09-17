def top_n (items, n):
    """Return the not n items in an arraay in desc order.

    Args:
        items (array): list or array-like object
        n (int): num of items to return


    Return:
        array: top n items in desc order


    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8, 7, 4]



    """


    return sorted(items, reverse = True)[0 : n]

t = top_n([8,3,2,7,4], 4)

print(t)
