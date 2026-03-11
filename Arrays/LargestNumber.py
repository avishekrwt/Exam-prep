# 2. Find the largest number in an array

n = int(input())
arr = list(input().split(' '))

lar = arr[0]
for item in arr:
    if lar < item:
        lar = item

print(lar)