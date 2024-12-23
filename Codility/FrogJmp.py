"""
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

X = 10
Y = 85
D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
"""

def solution(X, Y, D):
    result = X
    numtry = 0
    while True:
        if result >= Y:
            break
        else:
            result += D
            numtry += 1
    return numtry

"""
▶ example
example test ✔OK
expand allCorrectness tests
▶ simple1
simple test ✔OK
▶ simple2 ✔OK
▶ extreme_position
no jump needed ✔OK
▶ small_extreme_jump
one big jump ✔OK
expand allPerformance tests
▶ many_jump1
many jumps, D = 2 ✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶ many_jump2
many jumps, D = 99 ✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶ many_jump3
many jumps, D = 1283 ✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶ big_extreme_jump
maximal number of jumps ✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶ small_jumps
many small jumps ✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
"""

# 반복문이 동작하지 않아야 하는 것으로 보임
# 리팩토링 필요
# 3, 999111321, 7 를 기준으로 다시 작성해보자
# no jump 일때도 판단해야함
        
def solution(X, Y, D):
    if X >= Y:
        return 0
    distance = Y - X
    return (distance + D - 1) // D