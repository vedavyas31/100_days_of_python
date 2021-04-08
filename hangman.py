import random
import hangman_art
import hangman_words

#print the logo of this game
from hangman_art import logo, stages
print(logo)

#STEP 1
# create a word list
# word_list = hangman_words.word_list
# choose a random work from the word list
from hangman_words import word_list
chosen_word = random.choice(word_list)

# print(f'chosen_word is {chosen_word}')

#STEP 2
# create an empty list the is of same length as the chosen_word
display = []
for letter in chosen_word:
	display.append('_')

print(display)

#set lives equal 6
lives = 6
correct_guess = False
guess_list = []
while '_' in display and lives>0:
	# let the user guess a letter. Create a list of all the guesses
	guess = input('Guess a letter: ').lower()
	

	# check if the guessed letter is in the chosen_word
	if guess in chosen_word:
		if guess in display:
			print(f'You have already guessed the letter {guess}.')
			print(stages[lives])
		else:
			correct_guess = True
			# if user guesses a letter that is present in the chosen word then 
			# reveal only that letters in the word
			for num in range(len(chosen_word)):
				if chosen_word[num] == guess:
					display[num] = guess
			print(f'Letter a is in the word. {lives} lives left.\n{stages[lives]}')
	else:
		if guess in guess_list:
			print(f'You have already guessed {guess}. {lives} left.')
			print(stages[lives])
		else:
			guess_list.append(guess)
			correct_guess = False
			lives -= 1
			print(f'Letter {guess} is not in the word. You are left with {lives} lives.\n{stages[lives]}')

	print(display)
	# print(guess_list)

	#if no _ are present in the display and the user has guessed 
	#all the letters then print You win
	if '_' not in display and lives>0:
		print('You win')
	
	# if lives are equal to 0 then print sorry you loose
	if lives == 0 and '_' in display:
		print(f'{stages[0]} \n Sorry You Loose. The word was {chosen_word}')
