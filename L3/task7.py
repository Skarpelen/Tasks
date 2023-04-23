def fib(n):
    if n == 1 or n == 2:
        return 1

    first_num = 1
    sec_num = 1
    sum_fib = 0
    for i in range(n - 1):
        num_fib = first_num + sec_num
        first_num = sec_num
        sec_num = num_fib
        sum_fib += num_fib
    return first_num


if __name__ == '__main__':
    print(fib(764))