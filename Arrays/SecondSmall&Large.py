# 3. Second Smallest and Second Largest element in an array

n = int(input())
arr = list(map(int, input().split()))

smallest = secondSmallest = float('inf')
largest = secondLargest = float('-inf')

for x in arr:

    if x < smallest:
        secondSmallest, smallest = smallest, x
    elif smallest < x < secondSmallest:
        secondSmallest = x

    if x > largest:
        secondLargest, largest = largest, x
    elif secondLargest < x < largest:
        secondLargest = x

print(secondSmallest)
print(secondLargest)