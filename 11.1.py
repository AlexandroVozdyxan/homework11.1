def checking_a_prime_number(number):
    if number <= 1:
        return False
    if number == 1 or number == 2 or number == 3 or number == 5:
        return False
    if number % 2 or number % 3 or number % 5:
        return False
    return True
def prime_generator(end):
    for q in range(2, end + 1):
        if checking_a_prime_number(q):
            yield q

prime_generator(10)
prime_generator(100)