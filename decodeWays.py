def helper(data, k, memo):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == '0':
        return 0
    if memo[s] != None:
        return memo[k]
    result = helper(data, k - 1, memo)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += helper(data, k - 2, memo)
    memo[k] = result
    return result


def num_ways(data):
    memo = [None] * (len(data) + 1)  # initalie to null's
    return helper(data, len(data), memo)


print(num_ways("12"))
