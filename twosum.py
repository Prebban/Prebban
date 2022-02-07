A = [-2, 1, 2, -5, -1, 4, 7, 10, 11]
target = 9




def twosum(A, target):
    i = 0
    j = len(A) - 1
    A.sort()
    print(sorted(A))

    while i <= j:
        if A[i] + A[j] == target: 
            print(i, j)
            i += 1
            continue
            return True
        elif A[i] + A[j] < target:
            i += 1 
        else: # A[i] + A[j] > target
            j -= 1
    return False

print(twosum(A, target))