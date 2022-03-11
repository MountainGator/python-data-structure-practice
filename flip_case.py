def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newb = str('')
    for char in phrase:
        if char == to_swap.lower():
            if char.isupper():
                newb += char.lower()
            elif char.islower():
                newb += char.upper()
        if char == to_swap.upper():
            if char.isupper():
                newb += char.lower()
            elif char.islower():
                newb += char.upper()
        if char != to_swap.lower() and char != to_swap.upper():
            newb += char
    return newb

    

print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))