def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    def find_length (word):
        return len(word)
    
    lst = list()

    if type(d.keys()[0]) == int:
        lst.append(d.keys().sort())
    if type(d.keys()[0]) == str:
        lst.append(d.keys().sort(key=find_length))

    return tuple(lst[0], lst[-1])

print(min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))
print(min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"}))
