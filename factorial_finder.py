'''
Factorial Finder** - The Factorial of a positive integer, n, is defined as the product of the
sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this
using both loops and recursion.
'''

def factorial(num):
    '''
    take a number and factor it in the product of sum as n, n-2..
    '''

    ans = 1

    while num >= 1:
        ans = ans * (num)
        num = num - 1

    return ans

def test_factorial():
    '''
    test case to match number and it's factor
    '''
    num = 5
    ans = 120
    assert factorial(num) == ans
    assert factorial(0) == 1


if __name__ == "__main__":
    test_factorial()