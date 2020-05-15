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
    symbols = '.,!-?()"" \n'  # warunki dla - w środku ! - strip załatwia sprwawe
    with open(path, 'r') as file:
        for line in file:
            for word in line.split():
                tmp = word.strip(symbols)
                tmp = tmp.lower()
                if tmp not in words:
                    words[tmp] = False
    print("Ilość słów bez powtórzeń: " + str(len(words)))
    # print(words.keys())
    file.close()
    return words


def bm(text, words):
    for w in words:
        print(w)


bm(read_f1("file1.txt"), read_f2("file2.txt"))
