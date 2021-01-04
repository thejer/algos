def frog_jump(X,Y,D):
    if X==Y:
        return 0
    return ((Y-X)//D) if (Y-X)%D == 0 else ((Y-X)//D) +1


print(frog_jump(10, 85,30))