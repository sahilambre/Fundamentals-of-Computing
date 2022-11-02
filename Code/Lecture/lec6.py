import random
def sum(tups):
    '''
        Returns the sum of all elements in a tuple
    '''
    total = 0
    for element in tups:
        total = total + element
    return total
def numPositiveNumbers(tups):
    i = 0
    for element in tups:
        if element > 0:
            i += 1
    return i
def despace(s):
    '''
        Returns the string without any spaces
        despace('Hello world!') -> 'Helloworld!'
    '''
    acc = ''
    for element in s:
        if element != ' ':
            acc += element
    return acc
def reverse(s):
    '''
        Reverse the string
    '''
    acc = ''
    for i in s:
        acc = i + acc
    return acc
def addOne(L):
    '''
        Given a list L, returns a new List which is the same as L except with every
        element added 1
        addOne([1,2,3]) -> [2,3,4]
    '''
    acc = []
    for element in L:
        element += 1
        acc.append(element)
    return acc
def addOneInPlace(L):
    '''
        Given a list L, add one to each element
    '''
    for i in range(len(L)):
        L[i] = L[i] + 1 
#l = [1,2,4,5,631,632,66320,79,9251982513]
#addOneInPlace(l)
#print(l)
def filterOutNegative(L):
    '''
        Finish the function filterOutNegative(L) that returns a copy of the given 
list
        WITHOUT negative numbers
        Implement the function specification above.
        e.x.: filterOutNegative([-1,1,-2,2,3]) -> [1,2,3]
    '''
    if L == []:
        return []
    elif L[0] < 0:
        return filterOutNegative(L[1:])
    else:
        return [L[0]] + filterOutNegative(L[1:])
    
def rollDie():
    return random.randint(1,6)
def countRolls(n):
    '''
        Roll a die n times and return how many sixes show up
        You may assume you have a function rollDie() which rolls a six sided die 
and returns the result
    '''
    count = 0
    for i in range(0,n):
        var = rollDie()
        if var == 6:
            count += 1
    return count
def countRolls():
    '''
        Roll a die until a six shows up, and count how many rolls it tooks. Return 
that number
    '''
    count = 1
    while rollDie() != 6:
        count += 1
    return count
def playerTurn():
    goAgain = 'y'
    score = 0
    while goAgain == 'y':
        roll = rollDie()
        if roll == 1:
            print('Uh oh rolled 1. Sad.')
            return 0
        score += roll
        print('You rolled {0} and your score is {1}'.format(roll, score))
        goAgain = input('Go again? (y/n)')
    return score
def computerTurn(targetScore):
    score = 0
    while score < targetScore:
        roll = rollDie()
        if roll == 1:
            return 0
        score += roll
    return score
def pig(goalScore, targetScore):
    '''
        goal score == score needed to win game of pig
        target score == score computer will "bank" at each turn
    '''
    playerScore = 0
    computerScore = 0
    while playerScore < goalScore and computerScore < goalScore:
        playerScore += playerTurn()
        if playerScore < goalScore:
            computerScore += computerTurn(targetScore)
        print('Player Score:{0}'.format(playerScore))
        print('Computer Score:{0}'.format(computerScore))
    if playerScore >= goalScore:
        print('Player wins!')
    else:
        print('Computer wins!')
pig(100, 20)