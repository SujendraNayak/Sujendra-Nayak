def count_multiples(numbers):
    result = {}
    
    for i in range(1, 10):   
        count = 0
        
        for j in numbers:
            if j % i == 0:   # if divisible
                count += 1
        result[i] = count
    return result



numbers = list(map(int, input("Enter numbers separated by space: ").split()))
#he map() function in Python applies a function to each element of something (like a list).
print(count_multiples(numbers))
