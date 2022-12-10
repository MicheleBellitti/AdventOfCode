from collections import Counter

def get_input(input):
    with open(input) as f:
        text = f.readlines()
        text_fixed = [x[0:len(x) - 1].split() for x in text]
    return text_fixed[0][0]


def search_signal(text: str, number_of_letters: int):
    for i in range(len(text)):
        c = Counter(text[i:number_of_letters + i])
        if len(c.keys()) == number_of_letters:
            return i + number_of_letters


data = get_input('input#6.txt')
print(f'part 1: {search_signal(data, 4)}\t|\tpart 2: {search_signal(data, 14)}')

