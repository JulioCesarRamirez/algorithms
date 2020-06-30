def num_ways(nStairs):
    if nStairs == 0 or nStairs == 1:
        return 1
    else:
        return num_ways(nStairs-1) + num_ways(nStairs-2)


n = 4
result = num_ways(n)
print(f"{n} is num of stairs \nThe number of ways are {result}")
