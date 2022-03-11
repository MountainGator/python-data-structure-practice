def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    vowel_list = list()
    count = 0
    noob = str()
    for char in s:
        if vowels.count(char) != 0:
            vowel_list.append(char)

    vowel_list.reverse()

    for letter in s:
        if vowels.count(letter) == 0:
            noob += letter
        if vowels.count(letter) != 0:
            noob += vowel_list[count]
            count += 1
    return noob

print(reverse_vowels("Hello!"))

print(reverse_vowels("Reverse Vowels In A String"))