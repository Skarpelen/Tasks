def simple(num):
    if num == 0 or num == 1:
        print('Не простое и не составное')
        return
    ch = True
    count = 2
    for i in range(num // 2 - 1):
        if num % count == 0:
            ch = False
            break
        count += 1
    if ch:
        print('Простое')
    else:
        print('Составное')


if __name__ == '__main__':
    simple(653)
