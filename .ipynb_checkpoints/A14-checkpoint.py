#########2.1
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

#example
n1 = 53872
print(f"The number is: {n1}\nThe sum of digits is: {sum_of_digits(n1)}")

###########2.2
def sum_n(n):
    if n < 2:
        return n
    else:
        return n + sum_n(n - 1)
#example
n2 = 5
print(f"The number is: {n2}\nThe sum of all numbers from 0 up to and including {n2}: {sum_n(n2)}")

############2.3
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
#example
n3 = 8
print(f"The number is: {n3}\nFibonacci value for {n3} is: {fib(n3)}")