import random
import json
import math

def update(inp, word, guess, wrong, score, streak):
    correct = False
    for i in range (0, len(guess)):
        if(inp == word[i].lower()):
            guess[i] = inp
            correct = True
    if(correct):
        score += 1 + (streak/len(word))
        streak += 1
    elif(not correct):
        streak = 0
        wrong.append(inp)
    return (score, streak)

def printInfo(guess, wrong, score, streak, word, hint):
    print('Hint: ', hint)
    for i in guess:
        print(i, end = ' ')
    print('\tscore: ', end = '')
    print("%.2f" %score, end = '')
    print('\tstreak: ', str(streak), end='')
    print('\tremain wrong guess: ' + str(6 - len(wrong)))
    print(open('data/draw/' + str(len(wrong)) + '.txt', 'r').read())
    print('Wrong guessed: ', end = '')
    for i in wrong:
        print(i, end = ' ')
    print('')

def initialGuess(word):
    guess = []
    for i in word:
        if(i.isalpha()):
            guess.append('_')
        else:
            guess.append(i)
    return guess

def NotError(selectCategory, categoryList):
    if(not selectCategory.isdigit()):
        return False
    selectCategory = int(selectCategory) - 1
    if(selectCategory < 0 or selectCategory >= len(categoryList)):
        return False
    return True
    

def main(categoryList, score = 0):
    play = 'y'
    while(play == 'y'):
        score = 0
        print("Welcome to my Hangman game\nSelect Category:")
        for i in range (0, len(categoryList)):
            print(str(i+1) + '. ' + categoryList[i])
        selectCategory = input('Select(1-'+str(len(categoryList))+'): ')
        print(len(categoryList))
        if(NotError(selectCategory, categoryList)):
            selectCategory = int(selectCategory) - 1
        else:
            continue
        wordList = open('data/category/' + categoryList[selectCategory] + '.txt', 'r').read().split('\n')
        index = random.randint(0, len(wordList) - 1)  # minus 1 becuase index
        word = wordList[index]
        hint = json.loads(open('data/hint.json', 'r').read())
        hint = hint[categoryList[selectCategory]][word]
        guess = initialGuess(word)
        wrong = []
        streak = 0
        while(''.join(guess) != word and len(wrong) < 6):
            printInfo(guess, wrong, score, streak, word, hint)
            inp = input("\n> ").lower()
            if(inp == word.lower()):
                remain = guess.count('_')
                score += remain * 1.5
                guess = word;
            elif(inp not in wrong and inp not in guess):
                (score, streak) = update(inp, word, guess, wrong, score, streak)
            else:
                print("Same guess!!")
        printInfo(guess, wrong, score, streak, word, hint)
        print("\nYeahh!!!!!!!\n")
        print("Your Score:\t%.2f !!!!!!!!!!" %score)
        play = input("Want to play again?? (y/n): ")
    pass

if __name__ == '__main__':
    f = open('data/categoryList.txt' ,'r')
    categoryList = f.read().split('\n')
    main(categoryList)