import random
from replit import clear
from ascii import stages
from ascii import logo
from words import word_list

user_letters = {}

def get_random_word(words):
	random_num = random.randint(0, len(words)-1)
	random_word = words[random_num].lower()
	return random_word

def display_blanks(word):
	blanks = []
	for char in word:
		if char in user_letters:
			blanks.append(char)
		else:
			blanks.append("_")
	print(' '.join(blanks))

def get_user_guess(random_word):
	user_guess = input("Guess a letter: ").lower()
	print("\n")
	if not user_guess in user_letters:
		user_letters[user_guess] = 1
	else:
		user_letters[user_guess] += 1
	return user_guess

def should_game_end(random_word, lives_left):
	print(stages[lives_left])
	if lives_left < 1:
		print("You lose! :(")
		print(f"The word was {random_word}")
		return True
	else:
		for letter in random_word:	
			if not letter in user_letters:
				return False
	print("You win! :)")
	return True

def start_game():	
	lives_left = 6
	print(logo)
	random_word = get_random_word(word_list)
	# print(f"The word is: {random_word}")

	while not should_game_end(random_word, lives_left):
		user_guess = get_user_guess(random_word)
		clear()
		display_blanks(random_word)
		print("\n\n")
		if not user_guess in random_word:
			if user_letters[user_guess] >= 2:
				print("\nAlready tried this letter. It's not in the answer.")
			elif len(user_guess) >= 2:
				print("Please enter single letters")
			else:
				lives_left -= 1

start_game()
