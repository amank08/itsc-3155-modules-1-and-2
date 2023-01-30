import time

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = 15 + (35 - 15) * (2**31 - 1) / (2**32 - 1) # generate random number from 15 to 35
    start_time = time.time()
    result = fibonacci(int(n))
    end_time = time.time()
    print("Fibonacci number:", result)
    print("Time taken: {:.6f} seconds".format(end_time - start_time))
