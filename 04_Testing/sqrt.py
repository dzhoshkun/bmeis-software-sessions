def sqrt(a):
    if a<0:
        raise ValueError('Negative value for `a`')
    if isinstance(a,complex):
        raise ValueError('Complex value for `a`')
    return a**0.5
