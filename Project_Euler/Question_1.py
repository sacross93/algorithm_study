# 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면?

## 10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.
## 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?

object_num= 1000
target_num= [3, 5]
sum= 0

for i in range(0, object_num):
    if i % target_num[0] == 0 or i % target_num[1] == 0:
        sum += i

print(sum)