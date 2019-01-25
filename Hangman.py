import random

def update(inp, word, guess, wrong, score, streak):
    correct = False
    for i in range (0, len(guess)):
        if(inp == word[i]):
            guess[i] = inp
            correct = True
            score += len(word) + streak[0]*1.25
            streak[0] += 1
    if(not correct):
        streak[0] = 0
        wrong.append(inp)
    return score

def printInfo(guess, wrong, score, streak, word, hint):
    print('Hint: ', hint)
    for i in guess:
        print(i, end = ' ')
    print('\tscore: ', end = '')
    print("%.2f" %score, end = '')
    print('\tstreak: ', str(streak[0]), end='')
    print('\tremain wrong guess: ' + str(len(word) + 2 - len(wrong)))
    print('\tWrong guessed: ', end = '')
    for i in wrong:
        print(i, end = ' ')

def initialGuess(word):
    guess = []
    for i in word:
        if(i.isalpha()):
            guess.append('_')
        else:
            guess.append(i)
    return guess

def main(wordList, catagorylist, Hint):
    print("Welcome to my Hangman game\nSelect Category:")
    for i in range (0, len(categoryList)):
        print(str(i+1) + '. ' + categoryList[i])
    selectCategory = int(input('Type No: ')) - 1
    index = random.randint(0, len(wordList[selectCategory]) - 1)  # minus 1 becuase index
    word = wordList[selectCategory][index]
    hint = Hint[word]
    guess = initialGuess(word)
    wrong = []
    score = 0
    streak = [0]
    while(''.join(guess) != word and len(wrong) <= len(word)+2):
        printInfo(guess, wrong, score, streak, word, hint)
        inp = input("\n> ").lower()
        if(inp == word):
            guess = word;
        elif(inp not in wrong and inp not in guess):
            score = update(inp, word, guess, wrong, score, streak)
        else:
            print("Same guess!!")
    printInfo(guess, wrong, score, streak, word, hint)
    print("\nYeahh!!!!!!!")
    pass

if __name__ == '__main__':
    wordList = [['dog', 'cat'], ['table', 'pen'], ["abc12c!!"]]
    categoryList = ['animal', 'thing', 'test']
    Hint = {'dog':'bark', 'cat':'meow'}
    main(wordList, categoryList, Hint)