# This is a sample Python script.
import sys


def fast_sum_v1():
    loop: int = int(input())
    sum_list: list = []
    for i in range(loop):
        initial: list = sys.stdin.readline().rstrip().split(" ")
        sum_list.append(int(initial[0]) + int(initial[1]))
        print(sum_list[i])
    return


def fast_sum_v2():
    loop: int = int(input())
    sum_list: list = []
    for i in range(loop):
        initial: list = sys.stdin.readline().rstrip().split(" ")
        sum_list.append(int(initial[0]) + int(initial[1]))

    for j in range(loop):
        print(sum_list[j])
    return


def n_pick():
    number: int = int(input())
    for i in range(number):
        print(i + 1, end="\n")


def n_pick_reverse():
    number: int = int(input())
    storage: list = []
    for i in range(number):
        storage.append(i + 1)
    for j in reversed(storage):
        print(j)


def organized_sum_v1():
    loop: int = int(input())
    storage: list = []

    for i in range(loop):
        initial: list = sys.stdin.readline().rstrip().split(" ")
        storage.append(int(initial[0]) + int(initial[1]))
        print(f'Case #{i + 1}: {storage[i]}')

    return


def organized_sum_v2():
    loop: int = int(input())
    storage: list = []

    for i in range(loop):
        initial: list = sys.stdin.readline().rstrip().split(" ")
        storage.append(int(initial[0]) + int(initial[1]))
        print(f'Case #{i + 1}: {initial[0]} + {initial[1]} = {storage[i]}')

    return


def pick_star_v1():
    loop: int = int(input())
    for i in range(loop):
        print("*" * (i + 1), sep="", end="\n")
    return


def pick_star_v2():
    loop: int = int(input())
    for i in range(loop):
        print(" " * (loop - (i + 1)), "*" * (i + 1), sep="", end="\n")
    return


def less_number():
    n, x = map(int, input().split(" "))  #스페이스바로 구분된 두개의 정수를 받아 n과 x에 저장한다
    storage: list = sys.stdin.readline().rstrip().split(" ")
    output: list = []

    for i in range(n):
        if int(storage[i]) < x:
            output.append(int(storage[i]))
        else:
            continue

    for j in range(len(output)):
        print(output[j], end=" ")
    return


def while_sum_v1():
    storage: list = []
    counter: int = 0
    a, b = map(int, input().split(" "))
    while a != 0 or b != 0:
        storage.append(a + b)
        print(storage[counter], end="\n")
        a, b = map(int, input().split(" "))
        counter += 1
    return


def while_sum_v2():
    storage: list = []
    counter: int = 0
    input_list: list = sys.stdin.readline().rstrip().split(" ")

    while len(input_list) != 1:
        a = int(input_list[0])
        b = int(input_list[1])

        storage.append(a+b)
        print(storage[counter])
        counter += 1

        input_list = sys.stdin.readline().rstrip().split(" ")

    return


def while_sum_v2_2():
    storage: list = []
    counter: int = 0

    while True:
        input_list = sys.stdin.readline().rstrip().split(" ")
        try:
            a = int(input_list[0])
            b = int(input_list[1])
        except EOFError:
            break
        storage.append(a + b)
        print(storage[counter])
        counter += 1


    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while_sum_v2_2()
