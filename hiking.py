MOD=10**9+7
def count_routes(n,m,x,C,D,A,B):
    dp={}
    def solve(length,mountain,bridge_count,used_east,used_west):
        if length > D:
            return 0
        state=(length,mountain,bridge_count,used_east,used_west)
        if state in dp:
            return dp[state]
        if C <= length <= D:
            result=1
        else:
            result=0
        
        if mountain == 0:  
            for i in range(n):
                if not (used_east & (1<<i)):
                    new_length=length+A[i]
                    new_used=used_east | (1<<i)
                    result=(result+solve(new_length,0,bridge_count,new_used,used_west)) % MOD
                                    
                    if bridge_count < 18:
                        new_length=length+A[i]+x
                        result=(result+solve(new_length,1,bridge_count+1,new_used,used_west)) % MOD
        else:  
            for i in range(m):
                if not (used_west & (1<<i)): 
                    new_length=length+B[i]
                    new_used=used_west | (1<<i)
                    result=(result+solve(new_length,1,bridge_count,used_east,new_used)) % MOD
                    if bridge_count < 18:
                        new_length=length+B[i]+x
                        result=(result+solve(new_length,0,bridge_count+1,used_east,new_used)) % MOD
        dp[state]=result
        return result
    total=0
    for i in range(n):
        total=(total+solve(A[i],0,0,1<<i,0)) % MOD
    for i in range(m):
        total=(total+solve(B[i],1,0,0,1<<i)) % MOD
    return total

T=int(input())
kq=[]
for _ in range(T):
    n,m,x,C,D=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    kq.append(count_routes(n,m,x,C,D,A,B))
for result in kq:
    print(result)
