import io

cars = ["BMW", "Lexus", "Audi", "Volkswagen", "Jag", "Bentley"]
f = open("newfile.txt", 'w')

for car in cars:
	print("I own a " + car)
	f.write(car + '\n')
	

