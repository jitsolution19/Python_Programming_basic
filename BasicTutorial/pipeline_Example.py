from toolz import pipe
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
average = pipe(numbers, 
               filter(lambda n: n % 2 == 0), 
               map(lambda n: n * 10), 
               map(lambda n: n + 5), 
               lambda x: sum(x) / len(x))
print(average)