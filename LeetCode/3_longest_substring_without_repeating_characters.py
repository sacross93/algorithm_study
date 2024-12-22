"""
Given a string s, find the length of the longest 
substring
without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

test_input1 = "abcabcbb"
test_input2 = "bbbbb"
test_input3 = "pwwkew"
test_input = [test_input1, test_input2, test_input3]

for input in test_input:
    print(input)

temp = ""
result_str = []

for i in test_input1:
    if i not in temp:
        temp += i
    else:
        result_str.append(temp)
        temp = ""

len_result_str = []
for i in result_str:
    len_result_str.append(len(i))

print(max(len_result_str))