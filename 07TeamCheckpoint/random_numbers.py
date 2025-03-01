import random


def append_random_numbers(numbers_list, quantity=1):
    for i in range(0, quantity):
        number = random.uniform(1, 100)
        number = round(number, 1)
        numbers_list.append(number)
    return numbers_list


def append_random_words(words, quantity=6):
    new_list = []
    for i in range(0, quantity):
        word = random.choice(words) 
        new_list.append(word)
    print(new_list)    



def main():
    numbers = [16.2, 75.1, 52.3]
    word_list = [
    "harmony", "crescent", "innovation", "serenity", "pinnacle",
    "velocity", "compassion", "euphoria", "labyrinth", "resilience" ]
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    append_random_words(word_list)

main()
