#import random as r

#print("H A N G M A N")

#total = ["poop", "steph", "loser", "hello"]
#word = r.choice(total)

#new_word = "-" * (len(word))
#print(new_word)
#answer = input(f"Guess a letter: ")
#guesses = 8
#if answer not in word:
   # guesses -= 1
   # print(f"You have {guesses} guesses remaining")
#elif answer in word:
   # print(new_word.replace(new_word, answer))
#elif guesses > 8:
    #exit()


#else:
    #print(f"No such letter in the word")

import random as r
print("H A N G M A N")
print()
guesses = 8
total = ['python', 'java', 'kotlin', 'javascript']
word = r.choice(total)
new_word = "-" * (len(word))
temp = list(new_word)
while guesses > 0:
    i = 0
    print(new_word)
    answer = input(f"Input a single letter: ")
    if answer not in word:
        guesses -= 1
        print(f"{answer} is not in the word. You have {guesses} guesses left")

    else:
        for letters in word:
            if answer == letters:
                temp[i] = answer
            i = i + 1
        new_word = "".join(temp)
        print()

print("Thanks for playing!")




