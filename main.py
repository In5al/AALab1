import time
import math
import random
import matplotlib.pyplot as plt

def fib1(n):
    if n <= 1:
        return n
    return fib1(n - 1) + fib1(n - 2)

def fib2(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b


def fib3(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    M = [[1, 1],
         [1, 0]]

    # n - 1 times multiply the
    # matrix to {{1,0},{0,1}}
    for i in range(2, n + 1):
        multiply(F, M)


def fib4(n):
    phi = (1 + math.sqrt(5)) / 2

    return round(pow(phi, n) / math.sqrt(5))


MAX = 10000000

# Create an array for memoization
f = [0] * MAX


# Returns n'th fibonacci number using table f[]
def fib(n):
    # Base cases
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        f[n] = 1
        return (f[n])

    # If fib(n) is already computed
    if (f[n]):
        return f[n]

    if (n & 1):
        k = (n + 1) // 2
    else:
        k = n // 2

    # Applying above formula [Note value n&1 is 1
    # if n is odd, else 0.
    if ((n & 1)):
        f[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1))
    else:
        f[n] = (2 * fib(k - 1) + fib(k)) * fib(k)

    return f[n]

if __name__ == "__main__":
    n1 = (5, 11, 14, 17, 21, 24, 29, 33, 38, 42)
    n3 = (54021, 59098, 68502, 76021, 83055, 97010, 112010, 120409, 130337, 149099)
    n2 = [0]
    results = []
    rand = 100000
    for i in range(1,100):
        rand += random.randint(1000, 10000)
        n2.append(rand)


    for _ in n3:
        start_time = time.time()
        fib(_)
        results.append(time.time()-start_time)
        print(time.time()-start_time)
    plt.plot(n3, results)
    plt.ylabel("time(s)")
    plt.xlabel("n")
    plt.title("O(Log(n)) methode")
    plt.show()

