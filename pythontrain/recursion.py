def sum_array(array):

    '''Return sum of all items in array

    Input variable: Lists consisting of numerical values.

    Return variable: Summed value of the list of numerical values

       '''
    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):

    '''Return nth term in fibonacci sequence

    Input variable: the nth instance of fibonacci sequence being queried

    Output variable: The value of the nth instance of the fibonacci sequence

    '''

    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):
    '''Return factorial of a number

    input variable: Numerical value which factorial needs to be calculated

    Return variable: The factorial of the input variable

    '''

    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):

    '''Return word in reverse

    Input variable: String

    Output variableL the reversed order of input string

    '''

    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
