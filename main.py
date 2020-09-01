# This is a sample Python script.
import sys


def fast_sum_v1():
    loop: int = int(input())
    sum_list: list = []
    for i in range(loop):
        initial: str = sys.stdin.readline().rstrip().split(" ")
        sum_list.append(int(initial[0])+int(initial[1]))
        print(sum_list[i])
    return


def fast_sum_v2():
    loop: int = int(input())
    sum_list: list =[]
    for i in range(loop):
        initial: str = sys.stdin.readline().rstrip().split(" ")
        sum_list.append(int(initial[0])+int(initial[1]))

    for j in range(loop):
        print(sum_list[j])
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fast_sum_v2()
