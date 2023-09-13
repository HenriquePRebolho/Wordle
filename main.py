# Tentative of reconstructing the game wordle
import random
import dicionario
import colorama
from colorama import Fore
colorama.init(autoreset=True)

word = random.sample(dicionario.valid_words, 1)[0]

print("Tente acertar a palavra sorteada:")

ok = True

while ok:
    chute = input()
    if len(chute) != 5:
        print("Seu chute necessita ter cinco letras.")
        print("Tente novamente:")
        ok = True
    elif chute not in dicionario.valid_words:
        print("Seu chute não consta no dicionário")
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

            print("Seu resultado:")
            print("".join(result))
            print('Tente novamente:')
            ok = True
