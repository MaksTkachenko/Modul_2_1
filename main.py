
# Зареєструватись на github, та створити окремий репозиторій для цього завдання

# 1. Програма буде брати зі списку слів одне рандомне слово. +
# 2. Програма буде отримувати від користувача число - кількість спроб вгадати +
# 3. Далі програма буде чекати від користувача або букву, або ціле слово.
# 4. Якщо користувач пише слово, програма повинна перевіряти чи це не те саме слово,
#    якщо так то говорити що користувач вгадав слово, або писати що слово не правильне.
# 5. Якщо користувач ввів літеру, програма повинна перевірити чи є ця літера у нашому слові,
#    та якщо є, виводити наше слово, де зірочками будуть закриті всі літери,
#    які користувач ще не вгадав, або "Такої літери немає"
# 6. Якщо кількість спроб закінчиться, потрібно сказати користувачю, що він програв та закінчити роботу програми.

import random


def input_attempts():
    while True:
        user_number_input = input("Введіть кількість спроб: ")
        if not user_number_input.isdigit():
            print("Ви ввели недійсний символ! Спробуйте знову.")
        else:
            break
    return int(user_number_input)


def input_letter():
    while True:
        user_letter_input = input("Введіть слова або літеру: ").lower()

        if not user_letter_input.isalpha():
            print("Ви ввели недійсний символ! Спробуйте знову.")
        else:
            break
    return user_letter_input


def play_fun():
    play_num = input_attempts()
    list_guesses = []  # Список для зберігання вгаданих літер
    count_play = 0

    while count_play < play_num:

        letter = input_letter()

        if len(letter) > 1:
            if letter == random_word:
                print("Вітаю ви вгадали слово!!!")
                break
            else:
                # letter not in random_word:
                count_play += 1
                print("Невірне слово!!!")

        elif letter in list_guesses:
            print("Ви вже вгадали цю літеру")

        elif letter in random_word:
            list_guesses.append(letter)
            masked_word = ""
            for char in random_word:
                if char in list_guesses:
                    masked_word += char
                else:
                    masked_word += "*"
            print(masked_word)
            if '*' not in masked_word:
                print("Вітаємо! Ви вгадали слово!!!")
                break
        else:
            count_play += 1
            print("Такої літери немає")

        if count_play == play_num:
            print("На жаль, ви не вгадали, пощастити інший раз.")
            break

        attempts = play_num - count_play
        print(f"Залишилось {attempts} спроб")


if __name__ == "__main__":

    list_words = ["apple", "orange", "strawberry", "raspberry", "peach", "cherry"]
    random_word = random.choice(list_words)

    play_fun()
