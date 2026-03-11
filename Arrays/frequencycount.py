n = int(input())
arr = list(map(int,input().split(" ")))
freq_arr = dict()

for item in arr:
    count = freq_arr.get(item,0)
    freq_arr[item] = count+1

print(freq_arr)