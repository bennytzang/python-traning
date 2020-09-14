# n = input("輸入一個正整數: ")
# n = int(n)
# for i in range(n):
#     if i*i == n:
#         print("整數平方根",i)
#         break
# else:
#     print("沒有整數平方根")
def calculate(n):
    sum = 0
    for n in range(1,n):
        sum = sum + n
    print(sum)

calculate(5)
calculate(10)