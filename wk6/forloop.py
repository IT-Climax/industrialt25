data = [1.6, 3.4, 5.5, 9.4]
N = len(data)
print(N)
print(f'')
print(data[2])
data [2] = 7.3

for x in data:
    print(x)
data.append(11.4)
print(f"[{', '.join(str(x) for x in data)}]")

# index = 2
# x = data[index]
# print(x)


# carlist = ["Peugeot", "Toyota", "Honda", "Benz"]
# for auto in carlist:
#     print(auto)
# print(f"[{', '.join(str(auto) for auto in carlist)}]")


# # Range function
# start = 1
# stop = 4
# nums = []

# for x in range(start, stop):
#     print(x)
#     nums.append(x)

# print(f"[{', '.join(str(n) for n in nums)}]")

# # Range function with step
# start = 1
# stop = 10
# step = 2

# nums = []

# for x in range(start, stop, step):
#     print(x)
#     nums.append(x)

# print(f"[{', '.join(str(n) for n in nums)}]")


# # For using to implement summation of numbers
# sum = 0
# for x in data:
#     sum = sum+x
# print(sum)

# # implement sequence of number 0, 1, 1, 2, 3, 5,8,13,21,34, 55, 89, 144 (Fibonacci)
# N = 10
# fib1 = 0
# fib2 = 1
# print(fib1)
# print(fib2)

# for k in range(N-2):
#     fib_next = fib2 + fib1
#     fib1 = fib2
#     fib2 = fib_next
#     print(fib_next) # internal popping


# fib = [0,1]
# for k in range(N-2):
#     fib_next = fib[k+1] + fib[k]
#     fib.append(fib_next)
# print(f"Fibonacci List with Append: {list(fib)}")

# # Nested For Loops
# pairs = []
# for i in range(1, 5):
#     for k in range(1,5):
#         print(i, k)

#         #implementing pairs
#         pairs.append((i, k))
# print(pairs)

# pairs = [(i, k) for i in range(1, 5) for k in range(1, 5)]
# print(pairs)

# for i in range(1, 5):
#     row = [(i, k) for k in range(1, 5)]
#     print(row)


# """
# Class work
# 1. Implement the firt 25 prime numbers

# 2. Implement the prime number between 50 and 100
# """