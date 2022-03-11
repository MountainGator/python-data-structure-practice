def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    newb = list()
    for item in lst:
        if bool(item) == True:
            newb.append(item)
    return newb
    
print(compact([0, 1, 2, '', [], False, (), None, 'All done']))

# bool(item) == False or 