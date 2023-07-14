T=int(input())
for test in range(T):
    size=int(input())
    blocks=list(map(int,input().split()))
    len_blocks=len(blocks)
    if blocks[0]>=blocks[-1]:
        new=[blocks.pop(0)]
    else:
        new=[blocks.pop(-1)]
    while len(blocks)>0:
        if new[-1]>=blocks[0] and blocks[0]>blocks[-1]:
            new.append(blocks.pop(0))
        elif new[-1]>=blocks[-1]:
            new.append(blocks.pop(-1))
        else:
            break
    if len(new)==len_blocks:
        print("Yes")
    else:
        print("No")
