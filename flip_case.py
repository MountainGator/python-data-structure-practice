def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    for char in phrase:
        if char == to_swap:
            if char.isupper():
                char = char.lower()
            elif char.islower():
                char = char.upper()
        if char == to_swap.upper():
            if char.isupper():
                char = char.lower()
            elif char.islower():
                char = char.upper()

    

print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))