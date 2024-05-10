01.Problem: Day of the week
Write a program that reads an integer entered by the user and prints the day of the week (in English), 
in the range [1...7], or prints "Error" in case the entered number is invalid.

input	output
1	Monday
2	Tuesday
3   	Wednesday
4	Thursday
5	Friday
6	Saturday
7	Sunday
-1	Error

02.Problem: Weekend or working day
Write a program that reads the day of the week (text), in English - entered by the user. If the day is working, it prints on the console - "Working day", if it is a holiday - "Weekend". If a text other than a day of the week is entered, "Error" will be printed.

input	  output
Monday	  Working day

input	  output
Sunday	  Weekend

input	  output
April 	  Error

03.Class animal
Write a program that prints the class of the animal according to its name entered by the user.
1. dog -> mammal
2. crocodile, tortoise, snake -> reptile
3. others -> unknown

input	 output
dog	 mammal
snake	 reptile
cat	 unknown

04. Problem: Personal titels
Write a console program that reads the age (real number) and gender ('m' or 'f') entered by the user and prints an address from among the following:
• "Mr." – male (gender 'm') aged 16 or over
• "Master" – boy (gender 'm') under 16 years old
• "Ms." – female (gender 'f') aged 16 or over
• "Miss" – girl (gender 'f') under 16 years old

input	output	input	output	input	output	input	output
12              17      Mr.     25      Ms.	13.5
f	Miss	m               f               m       Master

05.Problem: Small shop
An enterprising Bulgarian opens neighborhood shops in several cities and sells at different prices depending on the city:

city / product	coffee	water	beer	sweets	peanuts
  Sofia 	0.50	0.80	1.20	1.45	1.60
  Plovdiv	0.40	0.70	1.15	1.30	1.50
  Varna	        0.45    0.70	1.10	1.35	1.55
  
Write a program that reads a product (text), a city (text), and a quantity (decimal number) entered by the user, 
and calculates and prints how much the corresponding quantity of the selected product costs in the specified city.

06.Problem: Number in range 
Write a program that checks if the number entered by the user is in the interval [-100, 100] and is different from 0 and outputs
"Yes" if it meets the conditions or "No" if it does not.

input	output		input	output		input	output
-25	Yes		0	No		25	Yes

07.Problem: Working hours
To write a program that reads the hour of the day (integer) and the day of the week (text) - entered by the user and checks whether 
the office of a company is open, with the working hours of the office being from 10 a.m. to 6 p.m., from Monday to Saturday inclusive

Sample input and output
input	output		input	output		input	output
11      open            19      closed          11      closed
Monday			Friday                  Sunday

08.Problem: Cinema ticket
To write a program that reads the day of the week (text) - entered by the user and prints on the console the price 
of a movie ticket according to the day of the week:

Monday	Tuesday	 Wednesday	Thursday	Friday	Saturday	Sunday
12	12	 14		14		12      16              16

Sample input output
input	output		input	output		input	output
Monday	12		Friday	12		Sunday	16

09.Problem: Fruit or vegetable
To write a program that reads a product name entered by the user and checks whether it is a fruit or a vegetable.
• "fruit" has the following possible values: banana, apple, kiwi, cherry, lemon and grapes;
• Vegetables have the following possible values: tomato, cucumber, pepper and carrot;
• All others are "unknown".
Display "fruit", "vegetable" or "unknown" according to the product entered.

Sample input and output
input	output		input	output		input	output		input	output
banana	fruit		apple	fruit		tomato	vegetable	water	unknown

10.Problem: Invalid number
A given number is valid if it is in the range [100…200] or is 0. Write a program that reads an integer entered by 
the user and prints "invalid" if the entered number is not valid.

input	output		input	output		                input	output		input	output
75	invalid		150	(There is no way out)		220	invalid		199	(There is no way out)

input	output		input	output		                input	output		                input	output
-1	invalid		100	(There is no way out)		200	(There is no way out)		0	(There is no way out)

11.Problem: Fruit shop
The fruit shop operates at the following prices on working days:

fruit	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
price   2.50	1.20	0.85	1.45	        2.70	5.50	        3.85

On Saturdays and Sundays, the store operates at higher prices:

fruit	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
price   2.70	1.25	0.90	1.60	        3.00	5.60	        4.20

Write a program that reads from the console the following three variables entered by the user and calculates the price according to the prices in the tables above:
• fruit - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
• day of the week - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
• quantity (real number).
Print the result rounded to 2 decimal places. Invalid day of the week or invalid fruit name to print "error".

input	output		input	output	     input	output		   input	output		input	output
apple   2.40            orange  2.70         kiwi       6.75               grapes       2.10            tomato  error
Sunday                  Tuesday              Monday                        Saturday                     Monday
3                       2                    2.5                           0.5                          0.5

12.Problem: Trade comissions
A company gives the following commissions to its salespeople according to the city in which they work and the volume of sales:

city	0 ≤ s ≤ 500	500 < s ≤ 1 000	  1 000 < s ≤ 10 000	s > 10 000
Sofia	    5%	              7%	         8%	        12%
Varna	  4.5%	            7.5%	        10%	        13%
Varna	  4.5%	            7.5%	        10%	        13%

Write a console program that reads city name (text) and sales volume (real number) entered by the user and calculates and outputs
the trade commission amount according to the above table. Output the result formatted to 2 decimal places. Invalid city or sales 
volume (negative number) to print "error".

input	output		input	 output		                input	output		input	   output
Sofia                   Plovdiv  27.50                          Varna   387.45          Kaspichan  error
1500	120.00		499.99                                  3874.50                 -50
			
			
	









			
	


			
		




