
length = 10007

def factory_deck():
    return list(range(0, length))

def deal_into_new_stack(deck):
    return deck[::-1]

def cut_n_cards(deck, n):
    start = deck[:n]
    end = deck[n:]
    return end + start

def deal_with_increment(deck, n):
    new_deck = [None] * length
    for i in range(0, length):
        new_deck[i * n % length] = deck[i]
    return new_deck

deck = factory_deck()

file = open("input.txt", "r")
lines = file.readlines()

for line in lines:
    if line.startswith("deal into new stack"):
        deck = deal_into_new_stack(deck)
    elif line.startswith("cut"):
        n = int(line.split()[-1])
        deck = cut_n_cards(deck, n)
    elif line.startswith("deal with increment"):
        n = int(line.split()[-1])
        deck = deal_with_increment(deck, n)
    else:
        print("error: " + line)
        exit(1)

result = deck.index(2019)
print(result)