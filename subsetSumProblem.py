def count_sets(arr, total):
    mem = {}
    return rec(arr, total, len(arr) - 1, mem)


def rec(arr, total, i, mem):
    key = str(total) + ":" + str(i)
    if key in mem:
        return mem[key]
    elif total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        to_return = rec(arr, total, i-1, mem)
    else:
        to_return = (
            rec(arr, total - arr[i], i-1, mem) + rec(arr, total, i-1, mem))
    mem[key] = to_return
    return to_return


myArr = [2, 4, 6, 10]
myTotal = 16

print("Array: ", *myArr)
print(f"Total: {myTotal}")
print("Result = ", count_sets(myArr, myTotal))
