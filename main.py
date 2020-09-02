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
    ##EOFError를 이용하라고 했지만, 방법이 뭔지 모르겠다.


def sum_cycle():
    number_i: int = int(input())
    number_mid = int(number_i)
    counter: int = 0
    number: int = 0
    while True:
        number = (number_mid%10)*10 + (number_mid//10+number_mid%10)%10
        number_mid = number
        counter += 1

        if number == number_i:
            print(counter)
            break

    return


def cheap_burger():
    burger_n: int = 3
    soda_n: int = 2
    burger_p: list = []
    soda_p: list = []

    for i in range(burger_n):
        burger = int(input())
        burger_p.append(burger)
    burger_p.sort()

    for j in range(soda_n):
        soda = int(input())
        soda_p.append(soda)

    soda_p.sort()

    print(burger_p[0]+soda_p[0]-50)


def average_score():
    student = 5
    score: int = 0
    scores: list = []

    for i in range(student):
        score = int(input())
        if score<40:
            score = 40
        scores.append(score)

    print(int(sum(scores)/student))
    return


def pick_second():
    numbers: list = sys.stdin.readline().rstrip().split(" ")
    numbers_int: list = []
    for i in range(len(numbers)):
        integers = int(numbers[i])
        numbers_int.append(integers)

    numbers_int.sort(reverse = True)
    print(int(numbers_int[1]))
    return


def pick_second_if():
    numbers: list = sys.stdin.readline().rstrip().split(" ")
    numbers_int: list = []
    for i in range(len(numbers)):
        integers = int(numbers[i])
        numbers_int.append(integers)
    if numbers_int[1] <= numbers_int[0] <= numbers_int[2] or numbers_int[2] <= numbers_int[0] <= numbers_int[1]:
        print(numbers_int[0])
    elif numbers_int[0] <= numbers_int[1] <= numbers_int[2] or numbers_int[2] <= numbers_int[1] <= numbers_int[0]:
        print(numbers_int[1])
    elif numbers_int[0] <= numbers_int[2] <= numbers_int[1] or numbers_int[1] <= numbers_int[2] <= numbers_int[0]:
        print(numbers_int[2])


def put_stars():
    count: int = int(input())
    for i in range(count*2-1):
        if i < count:
            print("*"*(i+1), sep="", end="\n")
        elif i >= count:
            print("*"*(count-(i-count+1)), sep="", end="\n")
    return


def put_stars_v2():
    number: int = int(input())
    for i in range(2*number-1):
        if i < number:
            print(" "*i+(2*number-2*i-1)*"*")
        if i >= number:
            print(" "*(2*number-i-2)+(2*(i-number)+3)*"*")


def put_stars_v3():
    number: int = int(input())
    for j in range(2*number):
        if j % 2 == 0:
            for i in range(number):
                if i % 2 == 0:
                    print("*", end="")
                elif i % 2 !=0:
                    print(" ", end="")
        elif j % 2 != 0:
            for k in range(number):
                if k % 2 == 0:
                    print(" ",end="")
                elif k % 2 != 0:
                    print("*",end="")
        print("")

    return



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    put_stars_v3()
