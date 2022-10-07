# qPND
### Hybrid Algorithm for detecting prime numbers.
 
Project developed as end-of-course project in _Quantum Software Development Course_ from _Escuela Superior de Informatica - UCLM_.

The main idea is to develop, by means of one (or more) quantum algorithm -and classic software if needed- a Prime Number Detector (PND).

## Algorithm Concept
The purpose is to achieve an easy-to-understand algorithm for finding prime numbers, without needing to go deep in complex Number Theory of Mathematics. For this, I took advantage of basic mathematical properties (multiples and cartesian combinations).

Basically, we get a set of all those odd numbers lower than $a$ -the potential prime number we are examining- encoded in a set $B$en, we apply the cartesian product with itself and we will obtain another set -let's call it $C$. At this point, we just simply have to check whether if $a \in C$. In other words, if $a$ can be defined as a product of two lower numbers. In that case, we can state that $a$ is **not** a prime number, otherwise, we found a prime number!

For a more visual point of view, the process is explained in the figure below.

![Final Version Diagram](https://github.com/SergioJF10/qPND/blob/main/doc/img/Final_Version.png?raw=true)

## Evolution
The evolution of the project and the main idea of the hybrid algorithm changed along time, starting from "quatumizing" classical primality tests -such as Miller-Rabin test of even the Fermat's Small Theorem- and use it as a Search Oracle in a Grover Search Algorithm. Due to the high complexity of this tasks and the time budget available, I had to discard the idea.

I also found a parallel alternative, again a "quantumization" of a classical algorithm for finding prime numbers, in this case, the _Sieve of Erastosthenes_. But, due to similar reasons as the previous approach, the idea was discarded.

Finally, we reached this 

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
