# 6. Rearrange array in increasing-decreasing order

n = int(input())
arr = list(map(int,input().split(" ")))

# 0,1,2,3,4,5
for i in range(n-1):
    minindex = i

    for j in range(i+1,n):
        if arr[j]<arr[minindex]:
            minindex = j
    
    arr[i],arr[minindex] = arr[minindex],arr[i]

left = int(n/2)
right = int(n-1)

while(left<right):
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1

print(arr)