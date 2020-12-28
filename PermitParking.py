from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date, timedelta
import time
import json
import jsonlines

#switch-statement function
'''
carList = {
	1: 'Camry 2019',
	2: 'Camry 2010',
	3: 'Lexus',
	4: 'Minivan'
}
'''
# TODO finish adding in dictionaries by line
with jsonlines.open('cars.json') as f:
	for item in f:
		print(item["1"])

print(carList)
#print(carList[2])

#with open('cars.json', 'r') as f:
#	carList = json.load(line)
#	f.write("\n")

print("Welcome to amoshet's Permit Parking Script!")
print("Which car would you like to register for street parking?")

#prints list of available cars
count = 1
for i in range(len(carList)):
	print(str(count) + ". " + carList[count])
	count += 1

print(str(count) + ". Add New Car")

#asks user to select car
car = int(input("Please select car by number: "))

#TODO search how to ask a user for data once, and then save that information.
#TODO implement running on startup or at specific time
num = "2015558888"

addr = "201 YourStreet Street"
#changes car, car color, and license plate based on number selected (this is sample info)

if (carList[car] == "Camry 2019"):
	car = "Toyota Camry"
	carColor = "Silver"
	licensePlate = "N80AVG"
	Camry2019 = {
		"car": car,
		"carColor": carColor,
		"licensePlate": licensePlate
	}
	with open('cars.json', 'a') as w:
		json.dump(Camry2019, w)
		w.write("\n")
'''	
if (car == carList.index('Camry 2010')):
	car = "Toyota Camry"
	carColor = "Grey"
	licensePlate = "DRAOQY"
	
if (car == carList.index('Lexus')):
	car = "Lexus IS350"
	carColor = "White"
	licensePlate = "Q8MG5B"
	
if (car == carList.index('Minivan')):
	car = "Honda Odyssey"
	carColor = "Grey"
	licensePlate = "KGCD0Z"
'''	
if (car == count):
	car = input("What is your car's Make and Model? (Ex: Toyota Corolla): ")
	carColor = input("What color is your car? (Ex: Red): " )
	licensePlate = input("And what is your license plate? (Ex: LBJ3M7): " )
	
	carList(car) 

#splits phone number for form
ph1 = num[:3]
ph2 = num[3:7]
ph3 = num[6:]

#TODO Add check that time isn't past midnight. If it is, subtract 1 for the day.
#gets date from system and splits it for the input fields
t = date.today()
date = t.strftime("%m/%d/%Y")
dateSplit = date.split('/')
#todays date split for the form
d1 = dateSplit[0]
d2 = dateSplit[1]
d3 = dateSplit[2]

#tomorrows date
t2 = t + timedelta(days=1)
date2 = t2.strftime("%m/%d/%Y")
dateSplit2 = date2.split('/')
d4 = dateSplit2[0]
d5 = dateSplit2[1]
d6 = dateSplit2[2]

#sets options to disable random error(s)
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#starts browser
browser =  webdriver.Chrome(ChromeDriverManager().install(), options=options)  # webdriver.Chrome(options=options)
browser.get('https://www.oradellpolice.com/overnight-parking-2')

#sets list
info = [ph1, ph2, ph3, addr, car, carColor, licensePlate, d1, d2, d3, d4, d5, d6] 
elem = browser.find_elements_by_class_name('field-element')
#iterates through input fields and fills them
for i in range(len(elem)):
	elem[i].send_keys(info[i])

#submits form after 3 seconds and closes page
#time.sleep(3)
#submitForm = browser.find_element_by_class_name('button')
#submitForm.submit()
#time.sleep(3)
#browser.quit()