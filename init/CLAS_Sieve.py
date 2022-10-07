# Python script for implementing the classic version of the Eratosthenes Sieve until 511, i.e., 8 Qubits/Bits

def multiplos(n, max_n):
    '''Method for calculating the multiples of a number n lower or equal than max_n'''
    m = set()
    for i in range(n + 1, max_n + 1):
        if i % n == 0: #is multiple
            m.add(i)

    return m

def eratosthenesSieve(max_n):
    '''Method for the implementation of the Eratosthenes Sieve'''
    s = set(range(1,max_n))

    i = 2
    while (i ** 2) <= max_n:
        if i in s:
            s -= multiplos(i, max_n)
        
        # print(f'{i} -> {s}')
        i += 1

    print(f'Max i: {i - 1}')

    return s


if __name__ == "__main__":
    print(f'Prime numbers lower than 512: {eratosthenesSieve(512)}')