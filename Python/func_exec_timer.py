# calculate the time a function takes to run using decorator

import time

def funcTimer(func):


    def exec_func(*args):

        start = time.time()

        func(*args)

        finish = time.time()
        duration = finish - start

        # give it 5 digits precision
        format_duration = "{:.5f}".format(duration)
        print(f'function {func.__name__} take {format_duration} to run')

    return exec_func 



@funcTimer
def fib(num):

    # not the most efficient fibonacci. but it's my own code
    arr = [0, 1]

    while len(arr) < num:
        left_index = len(arr) - 2
        arr.append(arr[left_index] + arr[left_index + 1])

    print(arr[num - 1])
    return arr[num -1]

fib(7000)

