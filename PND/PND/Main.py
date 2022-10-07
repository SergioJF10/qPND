import matplotlib.pyplot as plt
import qsharp
from PND import Stage1

CANDIDATE = 11

def array_to_number(array):
    '''Converts an array with bits intepreted as boolean values into integers'''
    exponent = 0
    int_res = 0
    for bit in array[::-1]:
        int_res += ((2 ** exponent) * bit)
        exponent += 1

    return int_res

def stage_1():
    '''First Stage (initialization): Call to Quantum qRAM algorithm for initialization'''
    b_set = set()
    bin_results = Stage1(shots=5000)
    int_results = []
    for result in bin_results:
        int_results.append(array_to_number(result))
        b_set.add(int_results[-1])

    print(f'[STAGE 1] Odd numbers lower than {CANDIDATE}: {b_set}')
    plt.hist(int_results)
    plt.show()
    return b_set

def stage_2(b_set):
    '''Second Stage (cartesian product): Classic cartesian product method'''
    c_set = set()

    for b1 in b_set:
        for b2 in b_set:
            c_set.add(b1 * b2)

    return c_set


if __name__ == '__main__':
    b_set = stage_1()
    c_set = stage_2(b_set)
    print(c_set)