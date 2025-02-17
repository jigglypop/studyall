# def exp(x, n):
#     if n <= 1:
#         return x ** n

#     if n & 1:   # 홀수
#         ret = exp(x, (n - 1) // 2)
#         return ret * ret * x
#     else:
#         ret = exp(x, n // 2)
#         return ret * ret

# print(exp(10, 0))
# print(exp(10, 1))
# print(exp(10, 10))

def exp(x, n):
    if n <= 1:
        return x ** n
    if n & 1:   # 홀수
        return x * exp(x, (n - 1) // 2) **2
    else:
        return exp(x, n // 2) ** 2
        
print(exp(10, 0))
print(exp(10, 1))
print(exp(10, 10))
print(exp(10,9))