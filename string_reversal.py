def reverse_string(s):
    return s[::-1]
def check(s,r):
    min_strings=[]
    for i in range(len(s)):
        if r[i]=='1':
            min_strings.append(reverse_string(s[i]))
        else:
            min_strings.append(s[i])
    for i in range(len(min_strings)-1):
        if min_strings[i]>min_strings[i+1]:
            return False
    return True
def find_reversal_string(s):
    n=len(s)
    min_reversal ='1' * n
    for i in range(2**n):
        r=bin(i)[2:].zfill(n)
        if check(s,r)and r<min_reversal:
            min_reversal=r
    return min_reversal

T = int(input())
KQ =[]
for _ in range(T):
    N=int(input())
    s=[]
    for _ in range(N):
        s.append(input().strip())
    KQ.append(find_reversal_string(s))
for kq in KQ:
    print(kq)
