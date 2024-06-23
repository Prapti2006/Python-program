def minion_game(string):
    VOWELS = ["A","E","I","O","U"]
    index_consonants = []
    index_vowels = []
    STUART = 0
    KEVIN = 0
    string_len = len(list(string))
    for i in range(string_len):
        if string[i] not in VOWELS:
            index_consonants.append(i)
        else:
            index_vowels.append(i)
    for i in index_consonants:
        STUART+= string_len-i
    for i in index_vowels:
        KEVIN += string_len-i
    if STUART > KEVIN:
        print(f"Stuart {STUART}")
    elif STUART < KEVIN:
        print(f"Kevin {KEVIN}")
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)