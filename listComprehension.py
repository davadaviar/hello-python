# example 1
even_numbers = [ number for number in range(1, 11) if number % 2 == 0]
print(even_numbers)

# example 2
numbers = [1, 2, 3, 4, 5]
result = [(number, 'Even') if number % 2 == 0 else (number, 'Odd') for number in numbers]
print(result)

# example 3
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words)

# example 4
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)