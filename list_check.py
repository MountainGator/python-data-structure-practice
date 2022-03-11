def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    def is_list(item):
        if type(item) == list:
            return True
        else:
            return False

    newb = list()

    for item in lst:
        newb.append(is_list(item))

    return all(newb)

print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))