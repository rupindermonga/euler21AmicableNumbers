#A proper divisor of a positive integer $n$ is any divisor of $n$ other than $n$ itself. Thus, prime numbers have exactly one proper divisor, 1, and every other number has at least two proper divisors.
#Amicable numbers: If d(a) = b and d(b) = a, where a ≠ b

def SumProperDivisor(n):
    sum = 0
    for i in range(1, int(n // 2) +1):
        if n % i == 0:
            sum += i
    return sum
            
def IsAmicable(n):
    number1 = SumProperDivisor(n)
    return n == SumProperDivisor(number1) and n != number1


def SumAmicableNumbers(n):
    sum = 0
    for number in range(n):
        if IsAmicable(number):
           sum += number
    return sum


final = SumAmicableNumbers(10000)
print(final)