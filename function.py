# def power(base,exp=0):
#     print(base**exp)

# power(3,2)
# power(3)

# def divide(n1,n2):
#     print(n1/n2)

# divide(2,4)

def avg(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    print(sum/len(numbers))

avg(3,5,6,6,6,4,4,3)