from random import *

""" 
Loads words from a text file and compares to inputted chars to play Hangman.
"""

def load_words():
	words = []
	filename = "HangmanWords.txt"
	with open(filename) as file:
		for line in file:
			line = line.strip()
			words.append(line)
	file.close()
	return words
# Randomly chooses a word from the loaded words
def get_word(words):
	rand = randint(0, len(words))
	word = words[rand]
	return word
		
# Defines what to do at each turn
def turn(loss, word, word_as_list):
	j = 0
	char = input("Please enter a letter you think is in the word!\n")
	for i in range(len(word)):
		if(char == word[i]):
			print("Your letter was in the word!")
			word_as_list[i] = char
			print(word_as_list)
			j-=1
		j+=1
		if (j == len(word)):
			print("Your letter wasn't in the word!")
			return False

	
	return word_as_list

# Draws the hangman to identify progress made in each game. 
def status(loss):
	print("-----")
	print("|   |")
	if(loss < 6):
		print("|   ", end="")
	else:
		print("|   ")
	if(loss <= 5):
		print("O")
	if(loss != 6 and loss != 5):
		print("|  ", end="")
	elif(loss == 6):
		print("|  ")
	if(loss <= 2):
		print("/|\ ")
	elif(loss == 3):
		print("/|")
	elif(loss == 4):
		print(" |")
	if(loss <= 6 and loss != 5):
		print("|  ", end="")
	elif(loss == 5):
		print("|  ")
	if(loss == 0):
		print("/\ ")
	if(loss == 1):
		print("/")
	if(loss == 5):
		print("|")
	elif(loss >= 2):
		print("")
	print("_______\n")
		

def main():
	words = load_words()
	status(0)
	word = get_word(words)
	word_as_list = []
	win = 0
	loss = 0
	for i in range(len(word)):
		word_as_list.append("_")
		print(word_as_list[i], end=" ")
	while(win < len(word) and loss < 7):
		if(turn(loss, word, word_as_list) == False):
			loss+=1
			status(loss)
		if(loss == 6):
			print("You lose!")
			print("The word was...", word)
			break
		for i in range(len(word)):
			if ("_" != word_as_list[i]):
				win+=1
		if(win == len(word)):
				print("You win!")
				print("The word was...", word)
				break
		win = 0
			
if __name__ == "__main__":
	main()