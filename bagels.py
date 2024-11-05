import random

num_elements = 3
max_attempts = 11

def main():
    attempt = 1
    secret_word = []
    word_array = []

    for i in range(num_elements):
        secret_word.append(str(random.randint(0, 9)))

    print(f'Secret {secret_word}')

    for i in range(max_attempts):
        word_array.append(str(random.randint(100, 999)))

    while attempt < max_attempts:
        word = word_array[attempt]
        print(word)

        if word == ''.join(secret_word):
            print('You got them right')
            break

        fermi = False
        pico = False

        for i in range(len(secret_word)):
            if word[i] == secret_word[i]:
                fermi = True
            elif word[i] in secret_word:
                pico = True

        if fermi:
            print('Fermi')
        elif pico:
            print('Pico')
        else:
            print('Bagels')

        attempt += 1

    if attempt == max_attempts:
        print('Game over')

main()
