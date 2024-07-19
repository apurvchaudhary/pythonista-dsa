# factorial using recursion
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


# two Rupees daily
def two_daily(n):
    if n == 1:
        return 2
    else:
        return 2**n + two_daily(n - 1)


# sum of +ve integer number
def sum_pos(n):
    if n == 1:
        return 1
    return n + sum_pos(n - 1)


def sum_all_digit(n):
    if n < 10:
        return n
    return n % 10 + sum_all_digit(n // 10)


def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / a * pow(a, n + 1)
    return a * power(a, n - 1)


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def decimal_to_binary(n):
    if n == 0:
        return 0
    return n % 2 + 10 * decimal_to_binary(n // 2)


def nestedEvenSum(obj, sum=0):
    for key, value in obj.items():
        if isinstance(value, dict):
            sum = nestedEvenSum(value, sum)
        elif isinstance(value, int) and value % 2 == 0:
            sum += value
    return sum


def stringifyNumbers(obj):
    for key, value in obj.items():
        if isinstance(value, bool):
            continue
        if isinstance(value, int):
            obj[key] = str(value)
        elif isinstance(value, dict):
            obj[key] = stringifyNumbers(value)
    return obj


obj = {"num": 1, "test": [], "data": {"val": 4, "info": {"isRight": True, "random": 66}}}

print(stringifyNumbers(obj))
