inWord = input("digite uma paravra, e eu verei se e palindrome")

droWni = inWord[: :1]

if droWni == inWord :
    print("is Palindrome")
else :
    print("isnt palindrome")

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

# another way to do the same, the above one is the best

def reverse(word1) :
    x = ''
    for i in word1 :
        x = i + x
    return x


word = input('give me a word:\n')
x = reverse(word)
print(x, word)
if x == word :
    print('This is a Palindrome')
else :
    print('This is NOT a Palindrome')
