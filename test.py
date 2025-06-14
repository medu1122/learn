def thoigian(s,v):
    return s/v
def dkienwin(n,x,y,v,z):
    timeMax=v[-1]
    timeMin=min(thoigian(x,tocdo) for tocdo in v[:-1])
    if z == 0:
        timeDone=thoigian(x,timeMax)
    else:
        Scuoicung=x-z
        timeDone=1+(thoigian(Scuoicung,timeMax) if Scuoicung > 0 else 0)
    return timeDone < timeMin
def tim_z_min(n,x,y,v):
    if dkienwin(n,x,y,v,0):
        return 0

    for z in range(1,y+1):
        if dkienwin(n,x,y,v,z):
            return z
    return -1
T=int(input())
for _ in range(T):
    n,x,y=map(int,input().split())
    v=list(map(int,input().split()))
    print(tim_z_min(n,x,y,v))
