from functools import reduce

def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    newb = list()

    for num in nums:
        if num % 2 == 0:
            newb.append(num)
    if len(newb) == 0:
        return 1

    return reduce(lambda x, y: x*y, newb)

print(multiply_even_numbers([2, 3, 4, 5, 6]))
print(multiply_even_numbers([3, 4, 5]))
print(multiply_even_numbers([1, 3, 5]))    
