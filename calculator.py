# OG21050003522
# Level 1 task 27

#========================= Compulsory Task 1 ==============================#
# Calculator app using exception handling-----------------------------------

# -----------Importing modules-----------
import sys
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6 import QtGui

# Class declaration of the main app.
class Calculator(QWidget):
	def __init__(self):
		'''
		The constructor will load the ui form for use by the app as the GUI.
		The constructor will also call the event triggers method.
		'''
		super(Calculator, self).__init__()
		loadUi('Calculator.ui', self)
		self.event_triggers()
		#-----------class attributes-----------------------------------
		self.current_display = ''	# used to update the gui screen
		self.num1 = 0 				# used to hold the first number
		self.num2 = 0 				# used to hold the second number
		self.current_operation = '' # user to hold the currect operation + - x /

	def event_triggers(self):
		'''
		Function will used to listen for button clicks and trigger events
		'''
		#-------------numbers------------------------
		self.btn_0.clicked.connect(self.btn_0_clicked)
		self.btn_1.clicked.connect(self.btn_1_clicked)
		self.btn_2.clicked.connect(self.btn_2_clicked)
		self.btn_3.clicked.connect(self.btn_3_clicked)
		self.btn_4.clicked.connect(self.btn_4_clicked)
		self.btn_5.clicked.connect(self.btn_5_clicked)
		self.btn_6.clicked.connect(self.btn_6_clicked)
		self.btn_7.clicked.connect(self.btn_7_clicked)
		self.btn_8.clicked.connect(self.btn_8_clicked)
		self.btn_9.clicked.connect(self.btn_9_clicked)
		#------------opertaions-----------------------
		self.add_btn.clicked.connect(self.add)
		self.subtract_btn.clicked.connect(self.subtract)
		self.multiplication_btn.clicked.connect(self.multiply)
		self.division_btn.clicked.connect(self.divide)
		self.equals_btn.clicked.connect(self.get_answer)
		#-------------extras-----------------------------
		self.log_btn.clicked.connect(self.open_log)
		self.float_btn.clicked.connect(self.float_point)
		self.back_btn.clicked.connect(self.back_space)
		self.clear_btn.clicked.connect(self.clear_screen)
	
	#----------events---------------
	'''
	When the numbers or the point are clicked, they will trigger the events
	below. Each function will call the update display function and pass a specify value
	as argument to the update display function.
	'''
	def btn_0_clicked(self):
		self.update_display(0)
	def btn_1_clicked(self):
		self.update_display(1)
	def btn_2_clicked(self):
		self.update_display(2)
	def btn_3_clicked(self):
		self.update_display(3)
	def btn_4_clicked(self):
		self.update_display(4)
	def btn_5_clicked(self):
		self.update_display(5)
	def btn_6_clicked(self):
		self.update_display(6)
	def btn_7_clicked(self):
		self.update_display(7)
	def btn_8_clicked(self):
		self.update_display(8)
	def btn_9_clicked(self):
		self.update_display(9)
	def float_point(self):
		self.update_display('.')
	#--------------------------------

	def update_display(self,value):
		'''
		Function will only continue to update display if the display has not reached limit.
		Function will update display with value of button clicked.
		the current display string is used to store what the user has entered before and update accordingly.
		'''
		if len(self.current_display) == 5:
			return
		self.current_display += f'{value}'
		self.display_lbl.display(self.current_display)

	# Calculations---------------------------
	# Each operation is triggered by the operation buttons on the ui
	# The functions will call get num function to initiate operation and pass the operation character (= - x /)
	def add(self):
		self.get_num1('+')
	def subtract(self):
		self.get_num1('-')

	def multiply(self):
		self.get_num1('x')

	def divide(self):
		self.get_num1('/')
	#-----------------------------------------

	def get_num1(self, operation):
		'''
		Function will take a char that represents the user's choice of operation and store it in current operation attribute.
		It takes the value on screen entered by user and gives that value to num1. The screen is the clear for user to enter num2.
		'''
		self.current_display = ''
		self.current_operation = operation
		self.num1 = float(self.display_lbl.value())
		self.display_lbl.display(0)

	def get_answer(self):
		'''
		The get answer function is triggered by the user clicking on the equal sign.
		It takes the value on screen and store it in num2.
		An appropriate calculation is then done after checking what the char in current operation is. 
		Operation is then logged on to a file.
		'''
		self.current_display = ''
		self.num2 = float(self.display_lbl.value())
		if self.current_operation == '+':
			result = self.num1 + self.num2
		elif self.current_operation == '-':
			result = self.num1 - self.num2
		elif self.current_operation == 'x':
			result = self.num1 * self.num2
		else:
			result = self.num1 / self.num2
		# If result's length does not fit on screen, zeros are displayed to use as error reporting.
		if result > 99999:
			self.display_lbl.display('000000')
			return
		# Handling result, displaying answer on screen and logging calculation to file.
		self.display_lbl.display(result)
		self.log_to_file(result)

	def log_to_file(self,result):
		'''
		Function will use exception handling to handle errors when logging calculation to file.
		Function will show a message box with an error if operation is not successful.
		'''
		try:
			f = open('math_log.txt', 'a')
			f.write(f'{self.num1} {self.current_operation} {self.num2} = {result}\n')
		# Handling errors-----
		except:
			QMessageBox.critical(
           			 self,
            		'Error Report',
            		'Error logging calculation to file.'
        		)
		finally:
			f.close()

	def open_log(self):
		'''
		Function will use exception handling to handle errors when opening log file.
		Function will show a message box with an error if operation is not successful.
		'''
		try:
			# Displaying log to user.
			log = ''
			f = open('math_log.txt', 'r')
			for line in f:
				log += line
			QMessageBox.information(
           		 self,
           		'log report',
           		log
       		)
       	# Handling errors-----
		except:
			QMessageBox.critical(
           		 self,
           		'Error Report',
           		'Error opening log file.'
       		)

	# Experimental extra functionality to the calculator app---
	def back_space(self):
		self.current_display = self.current_display[:-1] 
		self.display_lbl.display(self.current_display)

	def clear_screen(self):
		self.current_display = '' 
		self.display_lbl.display(self.current_display)
	#----------------------------------------------------------

# Main
if __name__ == '__main__':
	app = QApplication(sys.argv)  # Creating the QApplication
	widget = Calculator()		  # Creating an instance of the Calculator class
	widget.setWindowTitle('Calculator by Obert Gwamure')
	widget.show()

	sys.exit(app.exec())		# Executing the program.

#========================= Compulsory Task 1 ==============================#