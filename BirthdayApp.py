#!/usr/bin/env python3
#Ruth Waiganjo Kamilimu Python Assignment-BirthdayApp

import datetime

def birthday():

	print("---------------------------------------\n"+"\tBirthday APP\n"+"---------------------------------------\n")

	year=int(input('What year were you born [YYY]?'))
	month=int(input('What month were you born [MM]?'))
	day=int(input('What day were you born [DD]?'))

	print("It looks like you were born on",month,"/",day,"/",year)
	
	today = datetime.date.today()
	birthday = datetime.date(today.year,month,day)
	delta =  birthday-today

	

	if delta.days < 0:
		print("looks like your birthday was", (-1 *delta.days), 'days ago')

	elif delta.days > 0: 
		print("looks like your birthday is in", delta.days,'days\nHope you are looking forward to it')	


	



birthday()	