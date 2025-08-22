def genarate_odd(n):
    result=[]
    for i in range(1,2*n,2):
        result.append(i)
    return result
n=int(input("Enter a number: "))
print(genarate_odd(n))
        