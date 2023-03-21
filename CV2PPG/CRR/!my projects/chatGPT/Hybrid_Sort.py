def hybrid_sort(numbers):
    if len(numbers) <= 10:
        return insertion_sort(numbers)
    else:
        pivot = numbers[len(numbers)//2]
        less = [x for x in numbers if x < pivot]
        equal = [x for x in numbers if x == pivot]
        greater = [x for x in numbers if x > pivot]
        return hybrid_sort(less) + equal + hybrid_sort(greater)

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key_item = numbers[i]
        j = i-1
        while j >=0 and numbers[j] > key_item:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key_item
    return numbers

numbers = [11, 4, 5, 6, 7, 8, 9, 10, 3, 2, 1, 0]
print(hybrid_sort(numbers))