from itertools import count

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_index = numbers.index(None)
numbers_no_none = []
for num in numbers:
    if num is not None:
        numbers_no_none.append(num)
count = len(numbers)
sum_no_none = sum(numbers_no_none)
average = sum_no_none / count
numbers[none_index] = average


print("Измененный список:", numbers)
