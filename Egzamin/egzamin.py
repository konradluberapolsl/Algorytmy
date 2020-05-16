# Wyznaczy listę słów, które pojawiają się w tekście z jednego pliku, a nie pojawiają się w tekście z pliku drugiego przy pomocy algorytmu Boyer-Moore
def read_f1(path):
    with open(path, 'r') as file:
        text = file.read()
    text = text.lower()
    # print(text)
    file.close()
    return text


def read_f2(path):
    words = {}
    symbols = ' .,!-?()"":\n '  # warunki dla - w środku ! - strip załatwia sprwawe
    with open(path, 'r') as file:
        for line in file:
            for word in line.split():
                tmp = word.strip(symbols)
                tmp = tmp.lower()
                # TYMCZASOWE ROZWIĄZANIE!
                tmp = ' ' + tmp + ' '
                if tmp not in words and tmp != "":
                    words[tmp] = False
    print("Number of words: " + str(len(words)))

    # print(words.keys())
    file.close()
    return words


def bm(text, words):
    z=0
    n = len(text)
    for w in words:
        m = len(w)
        i = m-1
        j = m-1
        while True:
            if w[j] == text[i]:
                if j == 0:
                    words[w] = True
                    z += 1
                    print("Match no. " + str(z) + " word: '" + w + "' on position: " + str(i))
                    break
                else:
                    i -= 1
                    j -= 1
            else:
                i = i + m - min(j, 1 + w.rfind(text[i]))
                j = m-1
            if i > n-1:
                break


bm(read_f1("file1.txt"), read_f2("file2.txt"))
