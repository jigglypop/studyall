def isPalindrome(arr):
    N = len(arr)
    cnt = N // 2

    i = 0
    while i < cnt:
        if arr[i] != arr[N - 1 - i]:
            return False
        i += 1
    return True

arr1 = 'abacxcaba'
arr2 = 'bbbbabbb'

print(isPalindrome(arr1))
print(isPalindrome(arr2))


# arr = 'algorithm'
# arr = list(arr)
# print(arr)
# N = len(arr)
# for i in range(len(arr)//2):
#     # arr[i] <--> arr[N-1-i]
#     arr[i],arr[N-1-i] = arr[N-1-i], arr[i]
# print(arr)

# val = ''
# while val:
#     print(val % 10)
#     val = val // 10