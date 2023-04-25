def add(*args):
    result = 0
    for _ in args:
        result += _
    return result
print(add(2, 4, 9))
