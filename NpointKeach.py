def cal(arr, a, k):
    check = 0
    savesum = 0
    neg=[x for x in arr if x<0]
    pos=[x for x in arr if x>0]
    for i in range(len(neg)-1,-1,-k):
        savesum+=abs(neg[i])*2
    for i in range(len(pos)-1,-1,-k):
        savesum+=abs(pos[i])*2
    return savesum


a,k=map(int,input().split())
arr=[]
for _ in range(a):
    arr.append(int(input()))
output = cal(arr, a, k)
arr.sort()
print("Output:", output)

