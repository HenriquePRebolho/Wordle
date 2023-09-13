# Tentative of reconstructing the game wordle
import random
import dicionario
import colorama
from colorama import Fore
colorama.init(autoreset=True)

word = random.sample(dicionario.valid_words, 1)[0]

print(word)
print("Try guessing the word:")

ok = True

while ok:
    chute = input()
    if len(chute) != 5:
        print("Seu chute necessita ter cinco letras.")
        print("Tente novamente:")
        ok = True
    else:
        if chute == word:
            print("Boa!")
            ok = False
        elif chute != word:
            result = []
            for i in range(5):
                j = chute[i]
                if chute[i] in word:
                    if chute[i] == word[i]:
                        result.append(Fore.GREEN + j)
                        i += 1
    # problem with adapt and adept. The second 'a' is not in the word, but the program understand otherwise
                    elif chute[i] != word[i]:
                        result.append(Fore.YELLOW + j)
                        i += 1

                else:
                    result.append(Fore.RED + j)
                    i += 1

            print("Your result:")
            print("".join(result))
            print('Try again:')
            ok = True
