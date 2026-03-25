def number_pattern(n):

    # n value validation
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'

    # pattern number
    pattern = ''
    for i in range(1, n + 1):
       if i == n:
            pattern += str(i)
       else:
            pattern += str(i) + ' '
    return pattern

print(number_pattern(4))
print(number_pattern(12))