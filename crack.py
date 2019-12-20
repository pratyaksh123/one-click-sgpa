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

	# Fill login form
	form['userid'].value = username
	form['password'].value = password
	# Submit form
	browser.submit_form(form)

	# Open main page after login
	browser.open(base_url)

	# Open transcripts page and scrap the details
	browser.open(reports)
	browser.select("bs-example")
	grade = []
	credit = []
	browser.parsed()
	table=browser.find("table",{"border":"1"})
	rows = table.select("tr")
	for i in range(2,len(rows)-4):
		grade.append(rows[i].select("td")[3].get_text())
		credit.append(rows[i].select("td")[2].get_text())
	
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
				elif(str=='S'):
					return 0
				elif(str=='I'):
					return 0
				elif(str=='X'):
					return 0
				elif(str=='W'):
					return 0
				elif(str=='U'):
					return 0
	def fakka(str):
		if(str == "I"):
					return "With regret, it is to inform you that you have on or more I grades(incomplete) in the respective courses"
		elif(str=="U"):
			return "With regret, it is to inform you that you have on or more U grades(Unsatifactory) in the respective courses"
		elif(str=="W"):
			return "You have opted to widthdraw from some courses"

	p = 0
	for i in grade:
	 	sum += float(credit[p])*grade_points(i)
	 	p += 1
	sgpa = sum/17
	return sgpa
	#check for fakka 
	for i in grades:
		return fakka(i)


def sgpa_cal_me_bb(username,password):
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

	# Fill login form
	form['userid'].value = username
	form['password'].value = password
	# Submit form
	browser.submit_form(form)

	# Open main page after login
	browser.open(base_url)

	# Open transcripts page and scrap the details
	browser.open(reports)
	browser.select("bs-example")
	grade = []
	credit = []
	browser.parsed()
	table=browser.find("table",{"border":"1"})
	rows = table.select("tr")
	for i in range(2,len(rows)-4):
	 	grade.append(rows[i].select("td")[3].get_text())
	 	credit.append(rows[i].select("td")[2].get_text())
	
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
				elif(str=='S'):
					return 0
				elif(str=='I'):
					return 0
				elif(str=='X'):
					return 0
				elif(str=='W'):
					return 0
				elif(str=='U'):
					return 0
	def fakka(str):
		if(str == "I"):
					return "With regret, it is to inform you that you have on or more I grades(incomplete) in the respective courses"
		elif(str=="U"):
			return "With regret, it is to inform you that you have on or more U grades(Unsatifactory) in the respective courses"
		elif(str=="W"):
			return "You have opted to widthdraw from some courses"

	p = 0
	for i in grade:
	 	sum += float(credit[p])*grade_points(i)
	 	p += 1
	sgpa = sum/16
	return sgpa
	#check for fakka 
	for i in grades:
		return fakka

#crack the password
def cracker(rollno,ldap):
    #define the refrence variables
    if(rollno[3]=='E'):
        ref=329
        ref_roll=67
    elif(rollno[3]=='C'):
        ref=251
        ref_roll=89
    elif(rollno[3]=='M'):
        ref=427
        ref_roll=72
    elif(rollno[3]=='B'):
        pass

    d=int(rollno[-3:])-ref_roll
    new=d+ref
    password=ldap+str(new)
    username=ldap
    return password


import PySimpleGUI as sg

sg.change_look_and_feel('DarkAmber')    # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text("Welcome to the results portal",size=(30,3),pad=(10,0), font=('Helvetica 30'))],[sg.Text("Make sure you are connected to the IIT-J internet(Refer ReadMe)",font=('Helvetica 15'),pad=(0,30))],
            [sg.Text("Enter the person's ROLL-NO",pad=(8,0),font=('Helvetica 12')), sg.InputText()],[sg.Text("Enter the person's Ldap-ID",font=('Helvetica 12')),sg.InputText()],[sg.Text("Choose branch-",font="arial 13")]
            ,[sg.Button("EE/CSE"),sg.Button("ME/BB")],[sg.Button('Cancel')] ]

# # Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    elif event in('EE/CSE'):
        sg.Popup('Your SGPA is: ',sgpa_cal_ee_cse(values[1],cracker(values[0],values[1])))
    elif event in('ME/BB'):
        sg.Popup('Your SGPA is:',sgpa_cal_me_bb(values[1],cracker(values[0],values[1])))
Window.close()

