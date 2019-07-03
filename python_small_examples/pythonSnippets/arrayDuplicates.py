'''
program to find the list of duplicated in an array

'''

def repeated(arr):
    ln = len(arr)
    #arr.sort()
    rep1 = []
    for i in range(ln):
        k = i + 1
        for j in range(k, ln):
            if arr[i] == arr[j] and arr[i] not in rep1:
                rep1.append(arr[i])
    return rep1

        
#ar = [1,3,4,5,6,5,4,3,7,9,99,9,8,6,6,2,1]
ar = [4,5,6,4,5,6,1]
print('\nOriginal Array : ' , ar)

print('\nRepeated elements in an array:',repeated(ar))