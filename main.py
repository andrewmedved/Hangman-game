import sys
import graphics
import textwrap
import time
import os
from random import randrange


def get_word_from_base(position):

	"""Выбрать и считать слово из базы слов"""

	try:
		with open('base_of_words.txt') as file:
			return file.readlines()[position]

	except FileNotFoundError:
		return None

	except IndexError:
		return -1


def ciphered_word(word):
	word = word.strip()
	return ['_' for _ in range(len(word))]


def test():

	MAGIC_WORD = 'lighter'.upper()

	letter = 'g'.upper()

	print(MAGIC_WORD.index('G'))


def main():

	word = get_word_from_base(randrange(0, 213)).upper()

	if word == -1:
		print("OUT OF RANGE")

	if word != None:
		print(word)
	else:
		print("Occured error!")

	print(sys.argv[1])


def game_circle():


	start_game_choice = input("Would you like to start a game? yes/no ")

	while start_game_choice != 'no':

		hp = 6

		chosen_letters = []

		WORD = get_word_from_base(randrange(0, 213)).upper()

		print(WORD)
		secret_word = ciphered_word(WORD)

		while True:

			if hp == 0:
				print("=====GAME_OVER=====")
				break

			if '_' not in secret_word:
				print("OOH YEAHH! YOU WON!")
				break

			print(graphics.pictures[hp])


			print(secret_word)

			print(f"Chosen letters: {chosen_letters}")

			choice_letter = input("Enter guessing letter  ").upper()

			if (choice_letter in chosen_letters) or (choice_letter == ''): 
				print("Please print unique letter.")
				time.sleep(1)
				continue

			if choice_letter in WORD:
				print("RIGHT!")
				for i in range(len(WORD)):
					letter = WORD[i]
					if letter == choice_letter:
						secret_word[i] = letter
			else: 
				print("WRONG!")
				time.sleep(1)
				hp -= 1

			chosen_letters.append(choice_letter)
			os.system('clear')


		start_game_choice = input("Do we play another game? yes/no ")
	


#test()
game_circle()