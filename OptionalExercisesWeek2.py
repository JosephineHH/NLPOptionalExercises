import re

"""ELIZA like program using substitutions such as those described on page 9"""
def ELIZA(sent):
    match0 = re.search(r"\b(hello|hi|hey)\b", sent)
    match1 = re.search(r"I am (sad|depressed|unhappy)", sent)
    match2 = re.search(r"(I am|I'm) (.*)", sent)
    match3 = re.search(r".* always .*", sent)
    match4 = re.search(r".* all .*", sent)
    match5 = re.search(r"my (.*)", sent)

    if match0:
        print("Hello, how are you?")
    elif match1:
        print("I am sorry that you are", match1.group(1))
    elif match2:
        print("Why are you", match2.group(2), "?")
    elif match3:
        print("Can you think of an example?")
    elif match4:
        print("In what way?")
    elif match5:
        print("your", match5.group(1), "?")

    else:
        print("I am sorry")


ELIZA("I am really happy")




"""minimum edit distance algorithm"""
#I DON'T KNOW WHAT I AM DOING

def edit_distance(word1, word2):
    n = len(word1)
    m = len(word2)

    #create a matrix with zeroes
    editMatrix = [[]]
    accumulator = [[0 for x in range(m)] for y in range(n)]
    #for i in range(0,n-1):
    #    D[i,0] = D[i-1,0]

    return accumulator


edit_distance("to", "plante")