print(f'Combination with 1 and 0 avoiding two digits 1 in series'.center(90, '-'))


def f(n):
    d0 = [0] * n
    d1 = [0] * n
    d0[0] = 0
    d1[0] = 1
    for i in range(1, n):
        d0[i] = d0[i - 1] + d1[i - 1]
        d1[i] = d0[i - 1]
    return d0[n - 1] + d1[n - 1]


if __name__ == '__main__':
    print('Test 1 is', 'Ok' if f(3) == 2 else 'Fail')
    print('Test 2 is', 'Ok' if f(5) == 5 else 'Fail')
    print('Test 3 is', 'Ok' if f(6) == 8 else 'Fail')


print(f'Combination with 1 and 0 avoiding three digits 1 in series'.center(90, '-'))


def f(n):
    d0 = [0] * n
    d01 = [0] * n
    d11 = [0] * n
    d0[0] = 0
    d01[0] = 1
    for i in range(1, n):
        d0[i] = (d0[i - 1] + d01[i - 1] + d11[i - 1])
        d01[i] = d0[i - 1]
        d11[i] = d01[i - 1]
    return d0[n - 1] + d01[n - 1] + d11[n - 1]

if __name__ == '__main__':
    print('Test 1 is', 'Ok' if f(3) == 3 else 'Fail')
    print('Test 2 is', 'Ok' if f(5) == 11 else 'Fail')
    print('Test 3 is', 'Ok' if f(10) == 230 else 'Fail')

