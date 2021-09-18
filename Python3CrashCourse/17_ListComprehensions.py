# performing opperations on elements in a list: 

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# times each number in list by 10:
times_ten = [num*10 for num in myList]

print(times_ten)

# time only if even:
times_ten_if_even = [num*10 for num in myList if num % 2 == 0]

print(times_ten_if_even)