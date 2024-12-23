"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""

def solution(N):
    # Implement your solution here
    N = format(N, 'b')
    num_len = len(str(N))
    # print(num_len)
    result = 0
    temp_arr = 0
    temp = False
    for i in range(num_len):
        if int(str(N)[i]) == 1 and temp == False:
            temp = True
        elif temp == True and int(str(N)[i]) == 0:
            temp_arr += 1
        elif temp == True and int(str(N)[i]) == 1:
            if result <= temp_arr:
                result = temp_arr
            temp_arr = 0
            temp = False
        
    return result

# Result
"""
▶ extremes
n=1, n=5=101_2 and n=2147483647=2**31-1 ✔OK
▶ trailing_zeroes
n=6=110_2 and n=328=101001000_2 ✘WRONG ANSWER
got 1 expected 2
▶ power_of_2
n=5=101_2, n=16=2**4 and n=1024=2**10 ✔OK
▶ simple1
n=9=1001_2 and n=11=1011_2 ✔OK
▶ simple2
n=19=10011 and n=42=101010_2 ✔OK
▶ simple3
n=1162=10010001010_2 and n=5=101_2 ✘WRONG ANSWER
got 2 expected 3
▶ medium1
n=51712=110010100000000_2 and n=20=10100_2 ✘WRONG ANSWER
got 1 expected 2
▶ medium2
n=561892=10001001001011100100_2 and n=9=1001_2 ✔OK
▶ medium3
n=66561=10000010000000001_2 ✘WRONG ANSWER
got 5 expected 9
▶ large1
n=6291457=11000000000000000000001_2 ✘WRONG ANSWER
got 0 expected 20
▶ large2
n=74901729=100011101101110100011100001 ✔OK
▶ large3
n=805306373=110000000000000000000000000101_2 ✘WRONG ANSWER
got 1 expected 25
▶ large4
n=1376796946=1010010000100000100000100010010_2 ✔OK
▶ large5
n=1073741825=1000000000000000000000000000001_2 ✔OK
▶ large6
n=1610612737=1100000000000000000000000000001_2 ✘WRONG ANSWER
got 0 expected 28
"""

def solution(N):
    # Implement your solution here
    N = format(N, 'b')
    num_len = len(str(N))
    # print(num_len)
    result = 0
    temp_arr = 0
    for i in range(num_len):
        if int(str(N)[i]) == 1:
            if result <= temp_arr:
                result = temp_arr
            temp_arr = 0
        else:
            temp_arr += 1
        
    return result

## 리팩토링 후 결과
"""
▶ extremes
n=1, n=5=101_2 and n=2147483647=2**31-1 ✔OK
▶ trailing_zeroes
n=6=110_2 and n=328=101001000_2 ✔OK
▶ power_of_2
n=5=101_2, n=16=2**4 and n=1024=2**10 ✔OK
▶ simple1
n=9=1001_2 and n=11=1011_2 ✔OK
▶ simple2
n=19=10011 and n=42=101010_2 ✔OK
▶ simple3
n=1162=10010001010_2 and n=5=101_2 ✔OK
▶ medium1
n=51712=110010100000000_2 and n=20=10100_2 ✔OK
▶ medium2
n=561892=10001001001011100100_2 and n=9=1001_2 ✔OK
▶ medium3
n=66561=10000010000000001_2 ✔OK
▶ large1
n=6291457=11000000000000000000001_2 ✔OK
▶ large2
n=74901729=100011101101110100011100001 ✔OK
▶ large3
n=805306373=110000000000000000000000000101_2 ✔OK
▶ large4
n=1376796946=1010010000100000100000100010010_2 ✔OK
▶ large5
n=1073741825=1000000000000000000000000000001_2 ✔OK
▶ large6
n=1610612737=1100000000000000000000000000001_2 ✔OK
"""