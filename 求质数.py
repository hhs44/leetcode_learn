from math import sqrt


def func(n=100, m=200):
    res = []
    if n == 1:
        res = [2] + [num for num in range(2, m) if
                     num % 2 != 0 and 0 not in [num % i for i in range(2, int(sqrt(num)) + 1)]]
    if n >= 2:
        res = [num for num in range(n, m) if num % 2 != 0 and 0 not in [num % i for i in range(2, int(sqrt(num)) + 1)]]
    print(res)


if __name__ == '__main__':
    func()
