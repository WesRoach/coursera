# Number Theory and Cryptography

We all learn numbers from childhood. Some of us like to count, others hate it, but any person uses numbers everyday to buy things, pay for services, estimated time and necessary resources. People have been wondering about numbers’ properties for thousands of years. And for thousands of years it was more or less just a game that was only interesting for pure mathematicians. Famous 20th century mathematician G.H. Hardy once said “The Theory of Numbers has always been regarded as one of the most obviously useless branches of Pure Mathematics”. Just 30 years after his death, an algorithm for encryption of secret messages was developed using achievements of number theory. It was called RSA after the names of its authors, and its implementation is probably the most frequently used computer program in the word nowadays. Without it, nobody would be able to make secure payments over the internet, or even log in securely to e-mail and other personal services. In this short course, we will make the whole journey from the foundation to RSA in 4 weeks. By the end, you will be able to apply the basics of the number theory to encrypt and decrypt messages, and to break the code if one applies RSA carelessly. You will even pass a cryptographic quest!

As prerequisites we assume only basic math (e.g., we expect you to know what is a square or how to add fractions), basic programming in python (functions, loops, recursion), common sense and curiosity. Our intended audience are all people that work or plan to work in IT, starting from motivated high school students.

Do you have technical problems? Write to us: coursera@hse.ru

## Week 1 - Modular Arithmetic

In this week we will discuss integer numbers and standard operations on them: addition, subtraction, multiplication and division. The latter operation is the most interesting one and creates a complicated structure on integer numbers. We will discuss division with a remainder and introduce an arithmetic on the remainders. This mathematical set-up will allow us to created non-trivial computational and cryptographic constructions in further weeks.

### Learning Objectives

- Apply the notion of divisibility in problems in number theory
- Calculate remainder of a number after division
- Solve problems in number theory using the notion of division
- Apply divisibility test to check divisibility of numbers
- Apply modular arithmetic to problems in number theory
- Use binary system to represent numbers

## Week 2 - Euclid's Algorithm

This week we'll study Euclid's algorithm and its applications. This fundamental algorithm is the main stepping-stone for understanding much of modern cryptography! Not only does this algorithm find the greatest common divisor of two numbers (which is an incredibly important problem by itself), but its extended version also gives an efficient way to solve Diophantine equations and compute modular inverses.

### Learning Objectives

- Compute the greatest common divisor
- Compute the least common multiple
- Solve linear Diophantine equations
- Compute inverses in modular arithmetic

## Week 3 - Building Blocks for Cryptography

Cryptography studies ways to share secrets securely, so that even eavesdroppers can't extract any information from what they hear or network traffic they intercept. One of the most popular cryptographic algorithms called RSA is based on unique integer factorization, Chinese Remainder Theorem and fast modular exponentiation. In this module, we are going to study these properties and algorithms which are the building blocks for RSA. In the next module we will use these building blocks to implement RSA and also to implement some clever attacks against RSA and decypher some secret codes.

### Learning Objectives

- Develop an algorithm to compute fast modular exponentiation
- Develop an algorithm to compute a number with given remainders modulo two coprime numbers
- Describe the dependencies between remainders of the same integer modulo different integers
- Compute least common multiple using greatest common divisor
- Prove properties of numbers based on their prime factorizations
- Compute Euler's totient function
- Compute modular exponents using Fermat's Little Theorem and Euler's Theorem

## Week 4 - Cryptography

Modern cryptography has developed the most during the World War I and World War II, because everybody was spying on everybody. You will hear this story and see why simple cyphers didn't work anymore. You will learn that shared secret key must be changed for every communication if one wants it to be secure. This is problematic when the demand for secure communication is skyrocketing, and the communicating parties can be on different continents. You will then study the RSA cryptosystem which allows parties to exchange secret keys such that no eavesdropper is able to decipher these secret keys in any reasonable time. After that, you will study and later implement a few attacks against incorrectly implemented RSA, and thus decipher a few secret codes and even pass a small cryptographic quest!

### Learning Objectives

- Develop an algorithm for RSA encryption
- Develop an algorithm for RSA decryption
- Develop an algorithm to break RSA when one of the prime factors of the key is small
- Develop an algorithm to break RSA when there are only a few potential plaintext messages
- Develop an algorithm to break RSA when the difference between prime factors of the key is small
- Develop an algorithm to break RSA when there is insufficient randomness in the generation of prime factors
- Develop an algorithm to break RSA when the same message is broadcasted with different public keys
