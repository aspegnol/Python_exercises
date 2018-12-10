if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
arr.sort()
x=arr.count(arr[n-1])
print(arr[n-1-x])
