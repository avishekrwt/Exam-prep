# 1. Find the smallest number in an array


n = int(input())
arr = list(input().split(' '))

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print(smallest)