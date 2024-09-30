import string

path = "./Macbeth.txt"


with open(path, "r") as f:
    counts = {}
    plaintext = f.read()
    plaintext = plaintext.lower()
    nopunc = plaintext.translate(str.maketrans('', '', string.punctuation))
    nopunc = nopunc.replace("\n", " ")
    list = nopunc.split(" ")

    for i in list:
        counts[i] = counts.get(i, 0) + 1


def Main():
    inn = int(input("Would you like to count a certain word (1) or show all words that only appear once? (2) "))

    if inn == 1:
        try:
            print(counts[input("Enter the word you wish to count: ")])
        except:
            Main()

    elif inn == 2:
        temp = []
        for i in counts:
            if counts[i] == 1:
                temp.append(i)
        print(temp)

Main()
