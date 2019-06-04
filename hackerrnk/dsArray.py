'''
Task 
Given an array,N , of  integers, print N's elements in reverse order as a single line of space-separated numbers.
Input Format
The first line contains an integer,  N (the size of our array). 
The second line contains N space-separated integers describing array A's elements.
Constraints
1<=N<=1000
1<Ai<1000, where Ai is the ith integer in the array.
Sample Input
4
1 4 3 2
Sample Output
2 3 4 1
Print the elements of array  in reverse order as a single line of space-separated numbers.
'''

n= int(input())
arr = []
###Have an array typed in 1 line by following statement
arr = list(map(int, input().split()))

## Reverse the array and print it converting to Map

print(" ".join(map(str, arr[::-1])))