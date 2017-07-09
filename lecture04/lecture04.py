def solve(numLegs, numHeads):
    for numChicks in range(0, numHeads + 1):
        numPigs = numHeads - numChicks
        totLegs = 4 * numPigs + 2 * numChicks
        if totLegs == numLegs:
            return (numPigs, numChicks)
    return (None, None)


def barnYard():
    heads = int(input('Enter number of heads: '))
    legs = int(input('Enter number of legs: '))
    pigs, chickens = solve(legs, heads)
    if pigs == None:
        print('There is no solution')
    else:
        print("Number of pigs: ", pigs)
        print("Number of chickens: ", chickens)


def solve1(numLegs, numHeads):
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs - numHeads - numChicks - numSpiders
            totLegs = 4 * numPigs + 2 * numChicks + 8 * numSpiders
            if totLegs == numLegs:
                return (numPigs, numChicks, numSpiders)
    return (None, None, None)



def solve2(numLegs, numHeads):
    solutionFound = False
    for numSpiders in range(0, numHeads +1):


def isPalidrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    if leng(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalidrome(s[1:-1])


def isPalindrome1(s, indent):
    """Returns True if s is a palindrome and False otherwise"""
    print(indent, 'isPalidrome1 called with', s)
    if len(s) <= 1:
        print(indent, 'About to return True from base case')
        return True
    else:
        ans = s(0) == s(-1) and isPalidrome1(s[1:-1], indent + indent)
        print(indent, 'About to return', ans)
        return ans


def fib(x):
    """Return fibonacci of x, where x is a non-negative int"""
    if x == 0 or x == 1: return 1
    else: return fib(x-1) + fib(x-2)
































