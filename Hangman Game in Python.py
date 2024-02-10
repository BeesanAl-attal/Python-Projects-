
import random 
from collections import Counter 

# note : using a triple quotation mark to create a multi line string 
list_of_secret_words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 
                        'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 'cherry', 
                        'papaya', 'berry', 'peach', 'lychee', 'muskmelon'
                        ]

# randomly choose a secret word from our secret words list 
word = random.choice(list_of_secret_words)
# after my first attempt i will add  buttons and more advanced setting 

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for letter in word:
        # to print the empty spaces for the letters in the word
        print('_', end= ' ')
    print()

playing = True 
#list for storing the letters guessed by the player 
letterGuessed = ''
chances = len(word) + 2
correct = 0
flag = 0

try: 
    while (chances != 0) and flag == 0: # flag is updated when the world is correctly guessed 
        print()
        chances -= 1

        try:
            guess = str(input('Enter a letter to guess: '))
        except:
            print('Enter Only a letter')
            continue # so we can let the user reenter until the input is valid a 'letter'


        # validation for the guess 
        if not guess.isalpha():
            print("enter only a letter")
            continue 
        elif len(guess) > 1 :
            print("enter only one letter")
            continue # you always wondered how to allow the user to reenter the value and this how simply use continue 
        elif guess in letterGuessed:
            print('You already guessed that letter')
            continue 

        # if the letter is guessed correctly
        if guess in word:
            # k stores the number of times the guessed letter occurs in word
            k =  word.count(guess)
            for _ in range(k):
                letterGuessed += guess # the guessed letter is added as many times it occurs 

        #print the word 
        #here lets explain the use of Counter which was imported from collections 
        # the counter function returns the list as a dictionary where 
        # the key of the elements in the dictionary is the element of the list 
        # Counter is a subclass of dictionary that counts the occurrences of elements in an iterable.
        # for exp lst = ['a', 'b'] --> Counter(lst) --> {'a': no. of occurrence of 'a'}
        # and from this simple explanation you can conclude why we used Counter 
        # a question when two dictionaries are equal? -->  when they have the same key-value pairs     
        
        for char in word:
            if char in letterGuessed and (Counter(letterGuessed)) != Counter(word):
                print(char, end = ' ')
                correct += 1 
            #if the user Guessed all the letters
            # Once the correct word is guessed fully, 
            elif (Counter(letterGuessed)) ==  Counter(word):
            # the game ends even if chances remain 
                print()
                print(f'The word is {word}')
                flag = 1
                print('Congratulations, YOU WON!, good job at guessing')
                break # to break out of the for loop 
                break # to break out of the while loop 
            else: 
              print('_', end = ' ')
    #if the user has used all of his chances 
    if chances == 0 and (Counter(letterGuessed) != Counter(word)):
        print()
        print('You lost :(, Try again ')
        print(f'the word was {word}')
except KeyboardInterrupt:
    print()
    print('Bye! Try again.')
    exit() # used to terminate the execution of the program, when its called it immediately stops the program and exits



