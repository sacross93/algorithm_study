"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

A[0] = 3
A[1] = 4
A[2] = 4
A[3] = 6
A[4] = 1
A[5] = 4
A[6] = 4
the values of the counters after each consecutive operation will be:

(0, 0, 1, 0, 0)
(0, 0, 1, 1, 0)
(0, 0, 1, 2, 0)
(2, 2, 2, 2, 2)
(3, 2, 2, 2, 2)
(3, 2, 2, 3, 2)
(3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

A[0] = 3
A[1] = 4
A[2] = 4
A[3] = 6
A[4] = 1
A[5] = 4
A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""

def solution(N, A):
    # Implement your solution here
    empty_arr = [0 for i in range(N)]
    # print(empty_arr)
    for i in A:
        if i >= 1 and i <= N:
            empty_arr[i-1] += 1
            # print(empty_arr)
        elif i == N + 1:
            for j in range(N):
                empty_arr[j] = max(empty_arr)
    
    return empty_arr

"""
▶ example
example test ✔OK
expand allCorrectness tests
▶ extreme_small
all max_counter operations ✔OK
▶ single
only one counter ✔OK
▶ small_random1
small random test, 6 max_counter operations ✔OK
▶ small_random2
small random test, 10 max_counter operations ✔OK
expand allPerformance tests
▶ medium_random1
medium random test, 50 max_counter operations ✘TIMEOUT ERROR
running time: 0.612 sec., time limit: 0.100 sec.
▶ medium_random2
medium random test, 500 max_counter operations ✘TIMEOUT ERROR
running time: 5.720 sec., time limit: 0.100 sec.
▶ large_random1
large random test, 2120 max_counter operations ✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶ large_random2
large random test, 10000 max_counter operations ✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶ extreme_large
all max_counter operations ✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
"""

# 2중 for문 사용으로 인한 timeout error 발생 추정
# 리팩토링 필요
# lazy update 적용 필요?

def solution(N, A):
    temp_arr = [0] * N
    temp_max = 0
    current_max = 0 

    for i in A:
        if 1 <= i <= N:
            if temp_arr[i - 1] < temp_max:
                temp_arr[i - 1] = temp_max
            temp_arr[i - 1] += 1
            current_max = max(current_max, temp_arr[i - 1])
        elif i == N + 1:
            temp_max = current_max

    for i in range(N):
        if temp_arr[i] < temp_max:
            temp_arr[i] = temp_max

    return temp_arr

"""
▶ example
example test ✔OK
expand allCorrectness tests
▶ extreme_small
all max_counter operations ✔OK
▶ single
only one counter ✔OK
▶ small_random1
small random test, 6 max_counter operations ✔OK
▶ small_random2
small random test, 10 max_counter operations ✔OK
expand allPerformance tests
▶ medium_random1
medium random test, 50 max_counter operations ✔OK
▶ medium_random2
medium random test, 500 max_counter operations ✔OK
▶ large_random1
large random test, 2120 max_counter operations ✔OK
▶ large_random2
large random test, 10000 max_counter operations ✔OK
▶ extreme_large
all max_counter operations ✔OK
"""