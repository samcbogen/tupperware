def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:
    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    HINT:
    If you can figure out
    how to use the built-in range function (without modifying the test cases!),
    then feel free to do so.
    That's fairly difficult to do,
    however, and it's much easier
    to just implement this function normally using the yield syntax.
    '''
    if b is None:
        index0 = 0
        index1 = a
        while index0 < index1:
            index0 += 1
            yield index0 - 1
    elif b is not None and c is None:
        index0 = a
        index1 = b
        while index0 < index1:
            index0 += 1
            yield index0 - 1
    elif b is not None and c is not None:
        index0 = a
        index1 = b
        if index0 > index1:
            if c > 0:
                return []
            elif c < 0:
                while index0 > index1:
                    index0 += c
                    yield index0 - c
        elif index1 > index0:
            while index0 < index1:
                if c < 0:
                    return []
                elif c > 0:
                    index0 += c
                    yield index0 - c
