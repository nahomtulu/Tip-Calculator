#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

bil_total = input("Welcome to the Tip Calculator \nWhat was the total bill? $")

percent_tip = input("What is the total percentage you would like to give? 10, 12, or 15? ")

num_ppl = input("How many people would liek ot split the bill? ")

bil_total = float(bil_total) 
percent_tip = int(percent_tip)
num_ppl = int(num_ppl)

pay = ((bil_total * (percent_tip / 100) +bil_total) / num_ppl)

pay = round(pay,2)

print(f"each person should pay ${pay}")