l=[int(item) for item in input().split(",")]
n=int(input())
count=0
for i in l:
    if i==n:
     count+=1
     print(count)