def find_smallest(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num 
    return smallest
score_list = [12, 45, 2, 9, 18]
print(find_smallest(score_list)) 