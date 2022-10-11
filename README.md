# qPND
### _Hybrid Algorithm for detecting prime numbers_
 
Project developed as end-of-course project in _Quantum Software Development Course_ from _Escuela Superior de Informatica - UCLM_.

The main idea is to develop, by means of one (or more) quantum algorithm -and classic software if needed- a Prime Number Detector (PND).

## Algorithm Concept
The purpose is to achieve an easy-to-understand algorithm for finding prime numbers, without needing to go deep in complex Number Theory of Mathematics. For this, I took advantage of basic mathematical properties (multiples and cartesian combinations).

Basically, we get a set of all those odd numbers lower than $a$ -the potential prime number we are examining- encoded in a set $B$en, we apply the cartesian product with itself and we will obtain another set -let's call it $C$. At this point, we just simply have to check whether if $a \in C$. In other words, if $a$ can be defined as a product of two lower numbers. In that case, we can state that $a$ is **not** a prime number, otherwise, we found a prime number!

For a more visual point of view, the process is explained in the figure below.

![Flow_diagram](https://user-images.githubusercontent.com/72602176/195032699-9fe59128-f015-4fba-8fcb-ec79cbb97670.png)

## Evolution
The evolution of the project and the main idea of the hybrid algorithm changed along time, starting from "quatumizing" classical primality tests -such as Miller-Rabin test of even the Fermat's Small Theorem- and use it as a Search Oracle in a Grover Search Algorithm. Due to the high complexity of this tasks and the time budget available, I had to discard the idea.

I also found a parallel alternative, again a "quantumization" of a classical algorithm for finding prime numbers, in this case, the _Sieve of Erastosthenes_. But, due to similar reasons as the previous approach, the idea was discarded.

Finally, we reached this idea aiming to simplify the algorithm, and the previously explained version of the algorithm was developed.

## Implementation
The quantum part of the algorithm was developed in Q# language. And, taking advantage of the Q# language ability to be wrapped within classic code in two conventional languages, Python was chosen.

#### Dependences
Regarding the Q# execution, you will need the .NET SDK and QDK. For installing it, in this [link](https://learn.microsoft.com/en-us/azure/quantum/install-command-line-qdk) you might find several options as well as the steps to install it. 

Then, for the integration with Python, a virtual environment is available in the repository, but the libraries are:
- [microsoft](https://pypi.org/project/microsoft/)
- [qsharp](https://pypi.org/project/qsharp/)
- [matplolib](https://pypi.org/project/matplotlib/)
- [notebook](https://pypi.org/project/notebook/)

For the case you might want to execuite it without the given virtual environment

## Execution
For executing the program, once you have installed all the requirements, open the repository and type the following commands
```
cd ./PND/PND/
python -W ignore qPND.py [--plot/-p] <number>
```
The `-W ignore` is due to the qsharp library, which includes inside it some minor warnings.

The `--plot` or `-p` option can be used in case you want to check the results after launching several times the Quantum Algorithm in a histogram. Also it's important for you to know that `<number>` **must** be an odd number, otherwise, the obvious result will be printed: _\<number\> is not a prime number_. Since it is divisible by $2$.

## References
The whole pdf for the references can be found in the `bib` folder.
#### Final Version
- [Solving mathematical problems with quantum search algorithm](https://arxiv.org/abs/quant-ph/0605003)
- [Quantum random access memory](https://arxiv.org/abs/0708.1879)
- [Quantum Bit String Comparator: Circuits and applications](https://www.researchgate.net/publication/228574906_Quantum_bit_string_comparator_Circuits_and_applications)

#### Initial approaches
- [A quantum primality test with order finding](https://arxiv.org/abs/1711.02616)
- [Primality Testing in Quantum Domain](https://arxiv.org/abs/1711.02616)
- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
