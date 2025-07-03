def get_factorial(num):
    
    if num != 0:
        num_list = []
        for i in range(num):
            num_list.append(i +1)

        x = len(num_list) -1
        last_result = num_list[x]
        while x > 0:
            last_result = last_result * num_list[x -1]
            x -= 1
    else:
        return 1

    return last_result

print(get_factorial(0))
print(get_factorial(1))
print(get_factorial(5))
