from math import sqrt
import re


def is_antipalindrome(n):
    # checks if a number is antipalindrome
    # n: int
    # return: bool
    return not any(i == str(n)[-index - 1] for index, i in enumerate(str(n)))


def test_is_antipalindrome():
    # test function for antipalindrome
    assert(is_antipalindrome(2783) == True)
    assert(is_antipalindrome(2773) == False)
    assert(is_antipalindrome(2782) == False)


def get_perfect_squares(start, end):
    # returns a list of perfect squares between given range
    # start, end: int
    # return: list
    return list(filter(lambda x: int(sqrt(x)) == sqrt(x), range(start, end + 1)))


def test_get_perfect_squares():
    # test function for get perfect squares
    assert(get_perfect_squares(1, 10) == [1, 4, 9])
    assert(get_perfect_squares(10, 100) == [i * i for i in range(4, 11)])


def menu():
    # prints out the menu
    # returns: int, representing the menu item given by user
    print('1. enter a number to check if it\'s antipalindrome')
    print('2. get perfect squares between [start, end]')
    print('3. get largest prime number below n')
    print('4. exit')
    return int(input('your option: '))


def prim(n):
    # n: int
    # return: bool
    # checks if a number is prime or not
    return not re.match(r'^1?$|^(11+?)\1+$', '1' * n)


def get_largest_prime_below(n):
    # n: int
    # returns the largest prime number below given n
    while not prim(n):
        n -= 1
    return n


def main():
    # console
    test_is_antipalindrome()
    test_get_perfect_squares()
    while (option := menu()) != 4:
        if option == 1:
            n = int(input('n: '))
            print(f'your number is {"antipalindrome" if is_antipalindrome(n) else "not antipalindrome"}')
        if option == 2:
            start = int(input('start: '))
            end = int(input('end: '))
            print(f'list of squares in range: {get_perfect_squares(start, end)}')
        if option == 3:
            n = int(input('n: '))
            print(get_largest_prime_below(n))


if __name__ == '__main__':
    main()
