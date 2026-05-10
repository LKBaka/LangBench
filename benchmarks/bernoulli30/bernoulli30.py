def bernoulli(n):
    # 硬编码波努利数的值
    if n == 0:
        return 1
    elif n == 1:
        return -0.5
    elif n == 2:
        return 1/6
    elif n == 4:
        return -1/30
    elif n == 6:
        return 1/42
    elif n == 8:
        return -1/30
    elif n == 10:
        return 5/66
    elif n == 12:
        return -691/2730
    elif n == 14:
        return 7/6
    elif n == 16:
        return -3617/510
    elif n == 18:
        return 43867/798
    elif n == 20:
        return -174611/330
    elif n == 22:
        return 854513/138
    elif n == 24:
        return -236364091/2730
    elif n == 26:
        return 8553103/6
    elif n == 28:
        return -23749461029/870
    elif n == 30:
        return 8615841276005/14322
    else:
        return 0

print(bernoulli(30))