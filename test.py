import random
import json
import math

def update(inp, word, guess, wrong, score, streak):
    correct = False
    for i in range (0, len(guess)):
        if(inp == word[i]):
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
    print('\tremain wrong guess: ' + str(len(word) - len(wrong)))
    print('\t\tWrong guessed: ', end = '')
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

def main(catagoryList, score):
    play = 'y'
    while(play == 'y'):
        print("Welcome to my Hangman game\nSelect Category:")
        for i in range (0, len(categoryList)):
            print(str(i+1) + '. ' + categoryList[i])
        selectCategory = int(input('Type No: ')) - 1
        wordList = open('data/category/' + catagoryList[selectCategory] + '.txt', 'r').read().split('\n')
        index = random.randint(0, len(wordList) - 1)  # minus 1 becuase index
        word = wordList[index]
        hint = json.loads(open('data/hint.txt', 'r').read())
        hint = hint[categoryList[selectCategory]][word]
        guess = initialGuess(word)
        wrong = []
        streak = 0
        while(''.join(guess) != word and len(wrong) <= len(word)):
            printInfo(guess, wrong, score, streak, word, hint)
            inp = input("\n> ").lower()
            if(inp == word):
                remain = guess.count('_')
                score += remain * 1.5
                guess = word;
            elif(inp not in wrong and inp not in guess):
                (score, streak) = update(inp, word, guess, wrong, score, streak)
            else:
                print("Same guess!!")
        printInfo(guess, wrong, score, streak, word, hint)
        play = input("Want to play again?? (y/n): ")
        print("\nYeahh!!!!!!!")
    pass

if __name__ == '__main__':
    f = open('data/categoryList.txt' ,'r')
    categoryList = f.read().split('\n')
    main(categoryList, 0)