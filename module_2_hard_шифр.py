c = 1
c_ = 1
sum = 0
count = 0

while c <= 10:
    print(f'1 число {c}')
    c = c + 1
    count = c + 1

    while c_ <= 10:
        print(f'2 число {c_}')
        sum = c + c_
        print(sum)
        c_ = c_ + 1
        if sum > n:
            n % sum
        if sum == n and n % sum == 0 and n % sum == 0:
            rez = f'{[c-1]}{[c_]}'

        print(f'{[c-1]}{[c_]}')