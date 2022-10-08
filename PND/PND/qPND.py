import matplotlib.pyplot as plt
import qsharp
import sys
import warnings
from PND import Stage1

CANDIDATE = 11
GRAPHIC = False
QUBITS = 4

def array_to_number(array):
    '''Converts an array with bits intepreted as boolean values into integers'''
    exponent = 0
    int_res = 0
    for bit in array[::-1]:
        int_res += ((2 ** exponent) * bit)
        exponent += 1

    return int_res

def stage_0():
    '''Preprocessing stage filtering for discarding obvius not primes'''
    if CANDIDATE == 2:
        return True
    elif CANDIDATE % 2 == 0:
        print(f'[PREPROCESS] {CANDIDATE} is NOT a prime number')
        return False
    elif CANDIDATE > (2 ** QUBITS) - 1:
        print(f'[PREPROCESS] Number {CANDIDATE} cannot be processed with 4 Qubits')
        return False
    else:
        return True

def stage_1():
    '''First Stage (initialization): Call to Quantum qRAM algorithm for initialization'''
    b_set = set()
    bin_results = Stage1(shots=5000)
    int_results = []
    for result in bin_results:
        int_results.append(array_to_number(result))
        b_set.add(int_results[-1])

    print(f'[STAGE 1] Odd numbers encoded with {QUBITS} qubits {CANDIDATE}: \n\t{b_set}')
    if GRAPHIC:
        plt.hist(int_results)
        plt.show()

    return b_set

def stage_2(b_set):
    '''Second Stage (cartesian product): Classic cartesian product method'''
    c_set = set()

    for b1 in b_set:
        for b2 in b_set:
            if b1 != 1 and b2 != 1:
                c_set.add(b1 * b2)

    print(f'[STAGE 2] Cartesian product of the B set: \n\t{c_set}')
    return c_set

def stage_3(c_set):
    '''Third Stage (prime finding): Classic search in a set'''
    return (CANDIDATE in c_set)

def main():
    '''Entry point for the program'''
    print(f'[STARTING] Potential prime number a: {CANDIDATE}')
    if not stage_0():
        return
    b_set = stage_1()
    c_set = stage_2(b_set)
    if stage_3(c_set):
        print(f'[STAGE 3] {CANDIDATE} is NOT a prime number')
    else:
        print(f'[STAGE 3] {CANDIDATE} IS a prime number')


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print('CmdLineError: Potential number not specified')
        sys.exit(1)

    if (sys.argv[1] == '--plot' or sys.argv[1] == '-p') and len(sys.argv) == 3:
        GRAPHIC = True

        if sys.argv[2].isdigit():
            CANDIDATE = int(sys.argv[2])
            main()
        else:
            print('CmdLineError: Potential number not specified')

    elif sys.argv[1].isdigit() and len(sys.argv) == 2:
        CANDIDATE = int(sys.argv[1])
        main()
    else:
        print('CmdLineError: Potential number not specified')
