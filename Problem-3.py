def generate_odd_conditional(n):
    result=[]
    for i in range(1,2*n,2):
        result.append(i)
    if n % 2 ==0:
        result.pop()
    return result
n=int(input("Enter a number: "))
print(generate_odd_conditional(n))