#Michael Sands
#Time spent: 2 hours
#December 10, 2017


#I used Python 3 for this program
#I believe python 2.7 has a different tkinter import (although im not sure), just so i dont loose points!
import tkinter as tk
from tkinter import Button, StringVar, Label, Entry, Canvas, Text, END, messagebox
import random

#The correct word is printed to the screen for testing purposes when you grade,
#but the user interaction with in the program all takes place inside of the tkinter GUI

#BONUS POINTS
#The correct word is displayed in a dialog box once the game ends
#All incorrect guessess are displayed in their own section of the GUI
#If a non alphabetical or multiple characters are entered an error dialog box appears
#I attempted to utilize some objected oriented principles all though i know i should have set up the class utilization differently

class stickman():
	def head(self, canvas):
		canvas.create_oval(100,50,150,100)
	def body(self, canvas):
		stick = canvas.create_line(125, 100, 125, 175)
	def leftarm(self, canvas):
		stick_leg1 = canvas.create_line(125, 175, 100, 225)
	def rightarm(self, canvas):
		stick_leg2 = canvas.create_line(125, 175, 150, 225)
	def leftleg(self, canvas):
		stick_arm1 = canvas.create_line(125, 175, 95, 150)
	def rightleg(self, canvas):
		stick_leg2 = canvas.create_line(125, 175, 155, 150)  



def chooseword(wordlist):
	print('2. Computer is choosing a word')
	r = random.randint(0,len(wordlist) -1)
	choice = wordlist[r]
	return choice
	

def init():
	print('1. Hangman')
	#TKINTER
	root = tk.Tk()
	g = Label(root, text="Please Enter a Letter as a Guess Here - - - - - - > > > ")
	g.grid(row=0, column = 0)
	e1 = Entry(root, width = 2)
	e1.grid(row=0, column=1)

	canvas = Canvas(root, width=250, height=300, bg = 'blue')
	canvas.grid(row=3, column=0)


	t = Text(root, width =30, height = 2)
	t.grid(row=4, column = 1)
	l = Label(root, text = 'Already Guessed')
	l.grid(row=4, column = 0)
	

	t2 = Text(root, width =30, height = 20)
	t2.grid(row=3, column = 1)
	l2 = Label(root, text = 'Correct Guesses')
	l2.grid(row=3, column = 2)

	stick = stickman()

	#COMPUTER GENERATED WORD
	wordlist = ['Hangman', 'Python', 'American', 'Machine', 'Engineer', 'Politics', 'Science', 'Linux', 'Macintosh', 'Internet', 'Washington', 'Country', 'amazing']
	computers_word = chooseword(wordlist).lower()
	print(computers_word)


	userselections = []
	global wrongguess
	wrongguess = 0



	word_guessed = ['_'] * len(computers_word)
	def get_user_input():


		def compareguess(letter, word):
			if str(letter) in word:
				return True
			else:
				return False

		t.delete(1.0, "end")
		guess =  e1.get().lower()
		if len(guess) == 1 and guess.isalpha() == True:
			userselections.append(guess)
			wg = word_guessed
			if (len(userselections) > 0):
				current_letter = userselections[-1]
				result = compareguess(current_letter, computers_word)
				if result == True:
					for i, letter in enumerate(computers_word):
						if guess == letter:
							wg[i] = letter
					if '_' not in word_guessed:
						messagebox.showinfo("Winner!", "YOU WIN! You guessed the correct word which was: " + computers_word)
					t2.insert("end", word_guessed)
					t2.insert("end", '\n')

				else:
					global wrongguess
					wrongguess += 1
					if wrongguess == 1:
						stick.head(canvas)
					elif wrongguess == 2:
						stick.body(canvas)
					elif wrongguess == 3:
						stick.leftarm(canvas)
					elif wrongguess == 4:
						stick.rightarm(canvas)
					elif wrongguess == 5:
						stick.leftleg(canvas)
					elif wrongguess == 6:
						stick.rightleg(canvas)
						#Tkinter Dialog Box to display game over
						messagebox.showinfo("Game Over", "Game Over you are out of Guesses! The correct word was: " + computers_word)
			
				t.insert("end", userselections)
				e1.delete(0, "end")

		else:
			msg = 'Error please only type one letter at a time & ensure your entry contains only alphabetical characters'
			messagebox.showinfo("Error", msg)
			
			t.insert("end", userselections)
			e1.delete(0, "end")

	letter_guess = Button(root, text='Submit', command=get_user_input)
	letter_guess.grid(row=0, column=2)


	root.mainloop()


init()