def sgpa_cal_ee_cse(username,password):
	from robobrowser import RoboBrowser
	import re
	import os
	from bs4 import BeautifulSoup
	# Create browser object
	browser = RoboBrowser()
	# Base URL for all Aryabhatta links
	base_url = "http://intra.iitj.ac.in:8080/Aryabhatta_New/"
	# reports link
	reports = "http://intra.iitj.ac.in:8080/Aryabhatta_New/transcript.do"
	# Open login page
	browser.open(base_url)
	form = browser.get_form()
	# username="tyagi.6"
	# password="tyagi.6329"

	# Fill login form
	form['userid'].value = username
	form['password'].value = password
	# Submit form
	browser.submit_form(form)

	# Open main page after login
	browser.open(base_url)

	# Open transcripts page and scrap the details
	browser.open(reports)
	browser.select(".bs-example")
	browser.select("table", {"border": "1"})
	course_name = []
	grade = []
	credit = []
	browser.parsed()
	rows = browser.select("tr")
	for i in range(4, 10):
	 course_name.append(rows[i].select("td")[1].get_text())
	for i in range(4, 10):
	 grade.append(rows[i].select("td")[3].get_text())

	#delete the communication-skill grade
	del course_name[3]
	del grade[3]

	sum = 0


	def grade_points(str):
				if(str == "A*"):
					return 10
				elif(str == "A"):
					return 10
				elif(str == 'A-'):
					return 9
				elif(str == 'B'):
					return 8
				elif(str == 'B-'):
					return 7
				elif(str == 'C'):
					return 6
				elif(str == 'C-'):
					return 5
				elif(str == 'D'):
					return 4
				elif(str == 'E'):
					return 2
				elif(str == 'F'):
					return 0


	credit = [4, 4, 4, 4, 1]
	p = 0
	for i in grade:
		sum += credit[p]*grade_points(i)
		p += 1
	sgpa = sum/17
	return sgpa
def sgpa_cal_me_bb(username,password):
	from robobrowser import RoboBrowser
	import re
	import os
	from bs4 import BeautifulSoup
	# Create browser object
	browser = RoboBrowser()
	# username='swami.2'
	# password='swami.2427'
	# Base URL for all Aryabhatta links
	base_url = "http://intra.iitj.ac.in:8080/Aryabhatta_New/"
	# reports link
	reports = "http://intra.iitj.ac.in:8080/Aryabhatta_New/transcript.do"
	# Open login page
	browser.open(base_url)
	form = browser.get_form()

	# Fill login form
	form['userid'].value = username
	form['password'].value = password
	# Submit form
	browser.submit_form(form)

	# Open main page after login
	browser.open(base_url)

	# Open transcripts page and scrap the details
	browser.open(reports)
	browser.select(".bs-example")
	browser.select("table", {"border": "1"})
	course_name = []
	grade = []
	credit = []
	browser.parsed()
	rows = browser.select("tr")
	for i in range(4, 15):
	 course_name.append(rows[i].select("td")[1].get_text())
	for i in range(4, 15):
	 grade.append(rows[i].select("td")[3].get_text())
	# print(grade)
	del course_name[6:9]
	del course_name[2]
	del grade[6:9]
	del grade[2]
	# print(course_name)
	# print(grade)

	sum = 0


	def grade_points(str):
				if(str == "A*"):
					return 10
				elif(str == "A"):
					return 10
				elif(str == 'A-'):
					return 9
				elif(str == 'B'):
					return 8
				elif(str == 'B-'):
					return 7
				elif(str == 'C'):
					return 6
				elif(str == 'C-'):
					return 5
				elif(str == 'D'):
					return 4
				elif(str == 'E'):
					return 2
				elif(str == 'F'):
					return 0


	credit = [3, 1, 4,3, 1,3,1]
	p = 0
	for i in grade:
		sum += credit[p]*grade_points(i)
		p += 1
	sgpa = sum/16
	return "Your SGPA is", sgpa

import PySimpleGUI as sg

sg.change_look_and_feel('DarkAmber')    # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text("Welcome to the results portal",size=(30,3),pad=(10,0), font=('Helvetica 30'))],[sg.Text("Make sure you are connected to the IIT-J internet(Refer ReadMe)",font=('Helvetica 15'),pad=(0,30))],
            [sg.Text('Enter your LDAP-ID',pad=(8,0),font=('Helvetica 15')), sg.InputText()],[sg.Text("Enter your password",font=('Helvetica 15')),sg.InputText('', password_char='*')],[sg.Text("Choose your branch-",font="arial 13")]
            ,[sg.Button("EE/CSE"),sg.Button("ME/BB")],[sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    elif event in('EE/CSE'):
        username=values[0]
        password=values[1]
        sg.Popup('Your SGPA is: ',sgpa_cal_ee_cse(username,password))
    elif event in('ME/BB'):
        username=values[0]
        password=values[1]
        sg.Popup('Your SGPA is:',sgpa_cal_me_bb(username,password))
Window.close()
