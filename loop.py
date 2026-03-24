# for loop
programming_languages = ['Rust', 'Python', 'Golang', 'Javascript', 'C++', 'Java']

for language in programming_languages:
    print(language)

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Tomato', 'Potato', 'Banana', 'Carrot']

for category in categories:
    for food in foods:
        print(f'{food} is a {category}')

developer_names = ['John', 'Jane', 'Bob', 'Alice', 'Mike']

for developer in developer_names:
    if developer == 'Jane':
        continue
    print(developer)    

# while loop
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the secret number (1-5): '))
    if guess == secret_number:
        print('You guessed it!')
    else:
        print('Try again')

# combination loop
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'{word} contains the vowel {letter}')
            break
        else:
            print(f'{word} has no vowels')