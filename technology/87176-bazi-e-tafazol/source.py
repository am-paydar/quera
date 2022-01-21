def game(number):
    b = number // 10
    a = number % 10
    return max(b, a) - min(b, a)
