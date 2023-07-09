
# simple GUI based-calculator using Tkinter module

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
# expression is stored as a string
expression = ""


# Function to update expression in text entry box as and when new button is pressed
def pressButton(num):
	# point out the global expression variable because it will be used in this function
	global expression

	# concatenation/append of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)


# Function to evaluate the final expression when "=" button pressed
def equalpress():
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)

		# initialize the expression variable
		# by empty string
		expression = ""

	# if error is generated then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents when "clear" pressed
# of text entry box
def clear():
	global expression
	# setting it to null string
	expression = ""
	# updating expression
	equation.set("")


# Driver code/ main function
if __name__ == "__main__":
	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background="#94AF9F")

	# set the title of GUI window
	gui.title("U-Calculate")

	# set the configuration/resolution of GUI window
	gui.geometry("315x350")

	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()

	# create the text entry box widget for using Entry method
	# displaying the expression.
	expression_field = Entry(gui, textvariable=equation)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	expression_field.grid(columnspan=4, rowspan=2, ipadx=95, pady=20)

	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	button1 = Button(gui, text=' 1 ', fg='black', bg='#AEC2B6', command=lambda: pressButton(1), height=2, width=7)
	button1.grid(row=2, column=0, padx=7, pady=7)

	button2 = Button(gui, text=' 2 ', fg='black', bg='#AEC2B6', command=lambda: pressButton(2), height=2, width=7)
	button2.grid(row=2, column=1, padx=7, pady=7)

	button3 = Button(gui, text=' 3 ', fg='black', bg='#AEC2B6', command=lambda: pressButton(3), height=2, width=7)
	button3.grid(row=2, column=2, padx=7, pady=7)

	button4 = Button(gui, text=' 4 ', fg='black', bg='#AEC2B6', command=lambda: pressButton(4), height=2, width=7)
	button4.grid(row=3, column=0, padx=7, pady=7)

	button5 = Button(gui, text=' 5 ', fg='black', bg='#AEC2B6', command=lambda: pressButton(5), height=2, width=7)
	button5.grid(row=3, column=1, padx=7, pady=7)

	button6 = Button(gui, text=' 6 ', fg='black', bg='#AEC2B6', command=lambda: pressButton(6), height=2, width=7)
	button6.grid(row=3, column=2, padx=7, pady=7)

	button7 = Button(gui, text=' 7 ', fg='black', bg='#AEC2B6', command=lambda: pressButton(7), height=2, width=7)
	button7.grid(row=4, column=0, padx=7, pady=7)

	button8 = Button(gui, text=' 8 ', fg='black', bg='#AEC2B6', command=lambda: pressButton(8), height=2, width=7)
	button8.grid(row=4, column=1, padx=7, pady=7)

	button9 = Button(gui, text=' 9 ', fg='black', bg='#AEC2B6', command=lambda: pressButton(9), height=2, width=7)
	button9.grid(row=4, column=2, padx=7, pady=7)

	button0 = Button(gui, text=' 0 ', fg='black', bg='#AEC2B6', command=lambda: pressButton(0), height=2, width=7)
	button0.grid(row=5, column=0, padx=7, pady=7)

	plus = Button(gui, text=' + ', fg='black', bg='#5C8984', command=lambda: pressButton("+"), height=2, width=7)
	plus.grid(row=2, column=3, padx=7, pady=7)

	minus = Button(gui, text=' - ', fg='black', bg='#5C8984', command=lambda: pressButton("-"), height=2, width=7)
	minus.grid(row=3, column=3, padx=7, pady=7)

	multiply = Button(gui, text=' * ', fg='black', bg='#5C8984', command=lambda: pressButton("*"), height=2, width=7)
	multiply.grid(row=4, column=3, padx=7, pady=7)

	divide = Button(gui, text=' / ', fg='black', bg='#5C8984', command=lambda: pressButton("/"), height=2, width=7)
	divide.grid(row=5, column=3, padx=7, pady=7)

	equal = Button(gui, text=' = ', fg='black', bg='#5C8984', command=equalpress, height=2, width=7)
	equal.grid(row=5, column=2, padx=7, pady=7)

	clear = Button(gui, text='Clear', fg='black', bg='#9BABB8', command=clear, height=2, width=7)
	clear.grid(row=5, column='1', padx=7, pady=7)

	Decimal= Button(gui, text='.', fg='black', bg='#5C8984', command=lambda: pressButton('.'), height=2, width=7)
	Decimal.grid(row=6, column=0, padx=7, pady=7)
	
	# start the GUI
	gui.mainloop()
