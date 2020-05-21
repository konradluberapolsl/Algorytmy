# -*- coding: utf-8 -*-
# Wyznaczy listę słów, które pojawiają się w tekście z jednego pliku, a nie pojawiają się w tekście z pliku drugiego przy pomocy algorytmu Boyer-Moore
import os


def read_to_string(path):
    with open(path, 'r', encoding="utf-8") as file:
        text = file.read()
    text = text.lower()
    text += " " # dodatkowe zabezpieczenie
    #print(text)
    file.close()
    return text


def read_to_dict(path):
    words = {}
    symbols = ' .,!-?()"":\n '  # warunki dla - w środku ! - strip załatwia sprwawe
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                tmp = word.strip(symbols)
                tmp = tmp.lower()
                # TYMCZASOWE ROZWIĄZANIE!
                #t = ' ' + tmp + ' '
                if tmp not in words and tmp != "":
                    words[tmp] = False
    # print("Ilość słów bez powtórzeń: " + str(len(words)))
    #print(words.keys())
    file.close()
    return words


def bm(text, words):
    n = len(text)
    symbols = [' ', '.', ',', '!', '?', '-', '(', ')', '#', '*', '']
    for w in words:
        m = len(w)
        i = m - 1
        j = m - 1
        while True:
            if w[j] == text[i]:
                if j == 0:
                    if i == 0 or text[i-1] in symbols and text[i+len(w)] in symbols:
                        words[w] = True
                        # print("Matched word: '" + w + "' on position: " + str(i))
                        # if i == 0:  print("Before: None")
                        # else: print("Before: " + text[i-1])
                        # print("After: " + text[i + len(w)])
                        break
                    else:
                        i = i + m - min(j, 1 + w.rfind(text[i]))
                        #i = i + m - min(j, 1 + w.rfind(text[i+len(w)]))
                        j = m - 1
                else:
                    i -= 1
                    j -= 1
            else:
                i = i + m - min(j, 1 + w.rfind(text[i]))
                j = m - 1
            if i > n - 1:
                break
    return words


def count_words(path):
    words = []
    symbols = ' .,!-?()"":\n '
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                tmp = word.strip(symbols)
                tmp = tmp.lower()
                if tmp not in words and tmp != "":
                    words.append(tmp)
    file.close()
    print(words)
    return len(words)


def results(words_1, num_of_word_2):
    i = 0
    j = 0
    for w in words_1:
        if words_1[w]:
            j += 1
        elif not words_1[w]:
            # print(w)
            i += 1
    c = int(num_of_word_2) - j

    print("Ilość słów w pliku 1. (bez powtórzeń): " + str(len(words_1)))
    print("Ilość słów w pliku 2. (bez powtórzeń): " + str(num_of_word_2))
    print("Ilość słów unikalne dla pliku 1: " + str(i))
    print("Ilość słów unikalne dla pliku 2: " + str(c))
    print("Ilość słów z pliku 1 znalezionych w pliku 2: " + str(j))

    save_results(words_1, num_of_word_2, i, c, j)


def save_results(words, n2, unique_1, unique_2, matches):
    file = open("results.txt", "w")

    file.write("Egzamin Praktyczny AiSD Konrad Lubera \n")
    file.write("Temat: Wyznaczy listę słów, które pojawiają się w tekście z jednego pliku, a nie pojawiają się w tekście z pliku drugiego przy pomocy algorytmu Boyer-Moore\n")
    file.write("---------------------------------------\n")

    file.write("Wyniki: \n")
    file.write("--------\n")
    file.write("Ilość słów w pliku 1. (bez powtórzeń): " + str(len(words)) + "\n")
    file.write("Ilość słów w pliku 2. (bez powtórzeń): " + str(n2) + "\n")
    file.write("---------\n")
    file.write("Słowa unikalne dla pliku 1: " + str(unique_1) + "\n")
    file.write("Słowa unikalne dla pliku 2: " + str(unique_2) + "\n")
    file.write("---------\n")
    file.write("Ilość słów z pliku 1 znalezionych w pliku 2: " + str(matches) + "\n")
    file.write("---------------------------------------\n")

    file.write(
        "Słowa które pojawiają się w tekście z jednego pliku, a nie pojawiają się w tekście z pliku drugiego: \n")
    i = 1
    for w in words:
        if not words[w]:
            file.write(str(i) + ". " + str(w.strip().capitalize()) + "\n")
            i += 1

    file.close()


results(bm(read_to_string("file1.txt"), read_to_dict("file2.txt")), count_words("file1.txt"))
os.system('start notepad results.txt')
