
# Job interview test assignment 

These tasks are meant for you to exercise your python skills and to provide a basis for discussion during the job interview

Specially consider aspects like readability, design, robustness, and maintainability (how easy it is to expand the script) in your solution.

We suggest you spend 1-2 hours on the exercise and solve what you can reach.

Infinite amount of solutions exist.

Enjoy, we hope it is a fun one!

## Warm-up exercise
A number of rolls with a dice are recorded as a string of digits, eg "15366611166266346666666416633"

Write a python function that counts how many times two consecutive 6s (not 3 or more 6s) has been observed. In "3366256664" there is one match.

## Exercise 2a
The MAN universe is a 2D space, of size 12x12 with a total of 5000 employees
The main office, headquarters, is located in CPH (codename=HQ) where 2000 workers develop towards decarbonization of shipping in the universe
There are additional 10 satellite-offices at the main world-trade harbours where the field workers are located.

CPH is located in coordinates (7,9), the location of the remaining offices can be found in attached .man file

The offices have an ID. The ID is an integer equal to the position of an list of offices ordered by number of employees
The amount of employees in each satellite-office is inverse proportional to the distance to the headquarters.

For the sake of the exercise, the amount of employees can be a decimal float

Print smallest office, name and country to the screen

Fallback! - If you have problems with this part of the exercise, please use the amount of fallback_employees from the company_locations.man for the next steps

## Exercise 2b
HR department would like to get a CSV table with all the offices, with following structure
ID, codename, and number of employees, rounded up to the closest 10th

## Exercise 2c
Make a plot with the locations of the offices, tagging them with "ID,codename=number employees" 
and representing its size with a circle, centered in the office location, 
if 1500 employees is a circle of diameter 1.2 and the circle area is proportional to the number of employees

Save the plot as image

## Exercise 2d
As usual, the annual winter party is held at the company's HQ.

The publications department will send the invitations, for their graphics software they would like a dict structure 
supporting an easy loop through the invitation creator application
To allocate budget, they also want to know the amount of employees per location

"""
Dear employee of office A, B
the winter party is near, it will be celebrated on C,D location
you will get reimbursed E dkk for the travelled distance to the party!
"""

A is the name of the city where office is located
B is the country
C, D are the x,y coordinates of the party location
E is the travel reimbursement provided the company covers 100 dkk per unit distance

Create an output file in a common file-sharing format containing data A->E + number of employees/office for this dict data type.

## Exercise 2e
If the dinner cost 500dkk per employee, what is the total cost for the company

## Exercise 2f
You are moved to a publications department, as they didn't have time and the party is approaching, thus they need the invitations, which you will prepare the text.

Make a script that reads the file generated in exercise 2d with the info for the invitation, and define an invitation class with the inputs as class variables
and a generate invitation class method which write the invitations text to a ascii-file per office

## Exercise 2g
After complains from the employees of the far-away locations that always travel to CPH for , top management, being rational, has decided that next winter party will be at a location, where the accumulated travel distance by all employees is the lowest optimal.
Where should the winter party take place? Print out the coordinates in the format given in the other file.

