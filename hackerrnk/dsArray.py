
'''
Print the elements of array A in reverse order as a single 
line of space-separated numbers.

'''

n= int(input())
arr = []
### Have the array typed in 1 line using space
arr = list(map(int, input().split()))

## Reverse array by converting it to MAP and printing it
print(" ".join(map(str, arr[::-1])))